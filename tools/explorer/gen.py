#!/usr/bin/env python3
"""Generate the data for the binary explorer (explorer/): retail beside ours.

For every image target of a project (progress/targets.py), every function
the scoreboard enumerates in the retail binary is written out with the
retail disassembly beside our build's disassembly of the function the
scoreboard paired with it, aligned instruction by instruction, every byte
classed as identical, filled in by the linker (a relocation in our object:
the two layouts differ, so these never compare), or different.

The function list, statuses and pairings are the scoreboard's own
(ext/tools/progress.py: score_target, PLACED_SYMS, SMALL_SYMS, NEAR_PAIRS),
so the viewer cannot disagree with `make progress`.

Usage:
  gen.py --repo ~/src/nolfsrc --title "No One Lives Forever" [--subdir DIR]
         [--github nolffan/nolfsrc] [--site .] [--only lithtech.exe,...]

It writes, in the site (--site, default the current directory):
  explorer/<repo>/data/      the functions, one directory per binary
  explorer/<repo>/index.html the page (the explorer layout)
  _data/explorer/<repo>.json what the homepage shows of it

--subdir is where the project sits in the repository when that is not its
top (lithtools: legacy/talon). Run it after `make` in the project: it reads
the project's build outputs. Runtime and third-party functions are listed,
but their disassembly is left out: they are not ours to write.
"""
import argparse
import difflib
import glob
import gzip
import json
import os
import re
import shutil
import subprocess
import sys
import time

CHUNK = 40          # functions a chunk file holds


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--subdir", default="")
    ap.add_argument("--github", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--site", default=".")
    ap.add_argument("--only", default="")
    ap.add_argument("--pages-only", action="store_true",
                    help="rewrite only the page and the homepage summary, "
                         "from the data already generated")
    ap.add_argument("--unpushed", action="store_true",
                    help="allow a HEAD that is not on any remote branch yet "
                         "(the GitHub links will not work until it is)")
    a = ap.parse_args()

    repo = os.path.abspath(os.path.expanduser(a.repo))
    pname = os.path.basename(repo)
    github = a.github or "nolffan/" + pname
    site = os.path.abspath(a.site)
    out_root = os.path.join(site, "explorer", pname, "data")
    proj = os.path.join(repo, a.subdir) if a.subdir else repo
    prefix = a.subdir.strip("/") + "/" if a.subdir else ""
    for t in (os.path.join(proj, "ext", "tools"), os.path.join(proj, "tools"),
              os.path.join(repo, "ext", "tools"), os.path.join(repo, "tools")):
        if os.path.exists(os.path.join(t, "progress.py")):
            tools = t
            break
    if a.pages_only:
        write_pages(site, pname, json.load(open(os.path.join(out_root, "manifest.json"))),
                    a.title)
        return
    os.environ["TOOLS_PROJECT"] = proj
    sys.path.insert(0, tools)
    sys.dont_write_bytecode = True
    os.chdir(proj)
    import progress                                     # noqa: E402
    import asmweb                                       # noqa: E402
    from exedump import Pe                              # noqa: E402
    from msvcdemangle import demangle                   # noqa: E402

    commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    # Every source link names this commit, so GitHub must have it.
    subprocess.run(["git", "fetch", "-q"], capture_output=True)
    remote = subprocess.run(["git", "branch", "-r", "--contains", commit],
                            capture_output=True, text=True).stdout.strip()
    if not remote and not a.unpushed:
        sys.exit("gen.py: %s (HEAD of %s) is not on any remote branch, so "
                 "its GitHub links would 404: push it first, or pass "
                 "--unpushed" % (commit[:7], repo))
    sources = SourceIndex(proj)
    only = {s.strip().lower() for s in a.only.split(",") if s.strip()}

    binaries = []
    for tgt in progress.TARGETS:
        if tgt["kind"] != "image":
            continue
        label = tgt["label"]
        if only and label.lower() not in only and tgt["stem"] not in only:
            continue
        t0 = time.time()
        print("%s: scoring" % label, file=sys.stderr, flush=True)
        rows, ours = progress.score_target(tgt)
        placed = {ad: s for (lb, ad), s in progress.PLACED_SYMS.items() if lb == label}
        small = {ad: s for (lb, ad), s in progress.SMALL_SYMS.items() if lb == label}
        near = {ad: s for (lb, ad, _sz, s, _e) in progress.NEAR_PAIRS if lb == label}

        funcs = {}
        layout = {}
        objpaths = {}
        ope = None
        if ours:
            objs = progress.image_objs(tgt, ours)
            for o in objs:
                objpaths[os.path.basename(o).lower()] = o
            funcs = progress._load_objs(objs)[0]
            layout = progress._our_layout(progress.our_map(ours)) or {}
            ope = Pe(os.path.join(proj, ours))
        rpe = Pe(os.path.join(proj, tgt["shipped"]))

        print("%s: disassembling" % label, file=sys.stderr, flush=True)
        rdis = Disasm(asmweb, rpe)
        odis = Disasm(asmweb, ope) if ope else None

        fns = []
        for (_lb, name, size, status) in rows:
            if not name.startswith("sub_"):
                continue
            addr = int(name[4:], 16)
            sym = placed.get(addr) or small.get(addr) or near.get(addr) or ""
            fns.append((addr, size, status, sym))
        fns.sort()

        index, chunk, ci = [], [], 0
        # start the binary's directory afresh: a binary with fewer chunks
        # than last time would otherwise keep the old ones
        shutil.rmtree(os.path.join(out_root, tgt["stem"]), ignore_errors=True)
        os.makedirs(os.path.join(out_root, tgt["stem"]))
        stats = {}
        for (addr, size, status, sym) in fns:
            mod, _, mangled = sym.partition(":")
            sig = (demangle(mangled) if mangled else "") or ""
            listed_only = status in ("crt", "middleware", "encrypted")
            r_ins = [] if listed_only else rdis.function(addr, size)
            entry = {"a": addr, "n": size, "s": status}
            body = {"a": addr}
            o_ins, mask, oaddr = [], set(), None
            if sym and sym in funcs and odis and not listed_only:
                code, mask = funcs[sym]
                oaddr = layout.get((mod.lower(), mangled))
                if oaddr is not None:
                    o_ins = odis.function(oaddr, len(code))
            rows_out, same, total = align(r_ins, o_ins, mask)
            entry["p"] = round(100.0 * same / total) if total and o_ins else None
            short = shortname(sig, mangled, addr)
            entry["f"] = short
            if mangled:
                entry["m"] = mangled
            if sig and sig != short:
                entry["g"] = sig
            if mod:
                entry["u"] = mod
            if oaddr is not None:
                entry["o"] = oaddr
            src = sources.find(mod, objpaths, sig, mangled) if mod else None
            if src:
                entry["l"] = prefix + src
            entry["c"] = ci
            body["r"] = rows_out
            index.append(entry)
            chunk.append(body)
            stats[status] = stats.get(status, 0) + 1
            if len(chunk) == CHUNK:
                write_gz(os.path.join(out_root, tgt["stem"], "c%d.json" % ci), chunk)
                chunk, ci = [], ci + 1
        if chunk:
            write_gz(os.path.join(out_root, tgt["stem"], "c%d.json" % ci), chunk)
        write_gz(os.path.join(out_root, tgt["stem"], "index.json"), {
            "label": label, "stem": tgt["stem"], "shipped": tgt["shipped"],
            "ours": ours, "functions": index})
        binaries.append(summary(label, tgt["stem"], index, stats))
        print("%s: %d functions, %.0fs" % (label, len(index), time.time() - t0),
              file=sys.stderr, flush=True)

    manifest_path = os.path.join(out_root, "manifest.json")
    old = {}
    if os.path.exists(manifest_path) and only:
        old = {b["label"]: b for b in json.load(open(manifest_path))["binaries"]}
    for b in binaries:
        old[b["label"]] = b
    order = [t["label"] for t in progress.TARGETS if t["kind"] == "image"]
    manifest = {
        "name": pname, "title": a.title or pname, "github": github,
        "commit": commit, "generated": time.strftime("%Y-%m-%d"),
        "binaries": [old[l] for l in order if l in old]}
    write_json(manifest_path, manifest)
    write_pages(site, pname, manifest, a.title)


def write_pages(site, pname, manifest, title=""):
    """The project's page (the explorer layout), and what the homepage shows
    of it (_data/explorer/<repo>.json: no per-binary strips)."""
    manifest["name"] = pname
    if title:
        manifest["title"] = title
    os.makedirs(os.path.join(site, "explorer", pname), exist_ok=True)
    with open(os.path.join(site, "explorer", pname, "index.html"), "w") as f:
        f.write("---\nlayout: explorer\ntitle: %s\nproject: %s\n---\n"
                % (json.dumps(manifest["title"]), pname))
    os.makedirs(os.path.join(site, "_data", "explorer"), exist_ok=True)
    home = dict(manifest)
    home["binaries"] = [{k: v for k, v in b.items() if k != "strip"}
                        for b in manifest["binaries"]]
    home["strip"] = combined_strip(manifest["binaries"])
    with open(os.path.join(site, "_data", "explorer", pname + ".json"), "w") as f:
        json.dump(home, f, indent=1)
    write_json(os.path.join(site, "explorer", pname, "data", "manifest.json"), manifest)


LISTED_ONLY = ("crt", "middleware", "encrypted")
STRIP = 96          # cells in a binary's strip on the homepage


def summary(label, stem, index, stats):
    """A binary as the homepage shows it: its byte-identical share of our
    code (the scoreboard's: identical functions only) and a strip of STRIP
    cells over its code, each the identical share of that slice, 0-9."""
    app = [f for f in index if f["s"] not in LISTED_ONLY]
    total = sum(f["n"] for f in app) or 1
    same = sum(f["n"] for f in app if f["s"] == "identical")
    cells = [[0, 0] for _ in range(STRIP)]
    at = 0
    for f in app:
        for k in range(f["n"]):
            c = cells[min(STRIP - 1, (at + k) * STRIP // total)]
            c[1] += 1
            c[0] += f["s"] == "identical"
        at += f["n"]
    strip = "".join(str(min(9, int(10 * s / n))) if n else "-" for s, n in cells)
    return {"label": label, "stem": stem, "functions": len(app),
            "bytes": total, "identical": round(100.0 * same / total, 1),
            "stats": stats, "strip": strip}


def combined_strip(binaries):
    """One strip for a project: its binaries' strips, each given cells in
    proportion to its size."""
    total = sum(b["bytes"] for b in binaries) or 1
    out = ""
    for b in binaries:
        n = max(1, round(STRIP * 2 * b["bytes"] / total))
        out += "".join(b["strip"][i * len(b["strip"]) // n] for i in range(n))
    return out


def write_gz(path, obj):
    """path + ".gz": the data files are gzipped (about 6:1), and the page
    unpacks them. mtime 0, so the same data makes the same bytes."""
    with open(path + ".gz", "wb") as f:
        f.write(gzip.compress(json.dumps(obj, separators=(",", ":")).encode(),
                              9, mtime=0))


def write_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, separators=(",", ":"))


def shortname(sig, mangled, addr):
    if sig:
        head = sig.split("(")[0].strip()
        tick = head.find("`")
        if tick >= 0:
            # Foo::`scalar deleting destructor', `vector deleting destructor'
            return head[head.rfind(" ", 0, tick) + 1:]
        # drop the return type and calling convention: the qualified name is
        # the last space-separated word that is not inside a template
        depth, cut = 0, 0
        for i, ch in enumerate(head):
            if ch == "<":
                depth += 1
            elif ch == ">":
                depth -= 1
            elif ch == " " and depth == 0:
                cut = i + 1
        return head[cut:] or head
    return mangled or "sub_%x" % addr


class Disasm:
    """objdump over a whole .text once; functions sliced out of it, or
    disassembled on their own where the slice does not start on an
    instruction boundary."""

    def __init__(self, asmweb, pe):
        self.asmweb, self.pe = asmweb, pe
        tva, tvs, _ = pe.secs[".text"]
        self.rows = asmweb.disassemble(pe, tva, tva + tvs)
        self.addrs = [r[0] for r in self.rows]
        self.at = {a: i for i, a in enumerate(self.addrs)}

    def function(self, addr, size):
        i = self.at.get(addr)
        out = []
        if i is not None:
            end = addr + size
            while i < len(self.rows) and self.rows[i][0] < end:
                out.append(self.rows[i])
                i += 1
            if out and out[-1][0] + len(out[-1][1]) // 2 == end:
                return [fmt(r) for r in out]
        return [fmt(r) for r in self.asmweb.disassemble(self.pe, addr, addr + size)
                if addr <= r[0] < addr + size]


def fmt(r):
    addr, raw, text, note = r
    return (addr, raw, text, " ".join(note))


NUM = re.compile(r"0x[0-9a-f]+|\b[0-9a-f]{6,8}\b")


def norm(text):
    return NUM.sub("#", text)


def align(r_ins, o_ins, mask):
    """Rows [r_addr, r_hex, r_text, r_note, o_addr, o_hex, o_text, o_note,
    classes] with None for a gap, and (bytes that agree, bytes in all).
    classes has one letter per byte of the longer side: s (same), r (a
    relocation in our object: the linker fills it, so it cannot compare),
    d (different)."""
    rows = []
    same = total = 0
    if not o_ins:
        for r in r_ins:
            rows.append([r[0], r[1], r[2], r[3] or None])
        return rows, 0, sum(len(r[1]) // 2 for r in r_ins)
    ooff = []
    off = 0
    for o in o_ins:
        ooff.append(off)
        off += len(o[1]) // 2
    sm = difflib.SequenceMatcher(None, [norm(r[2]) for r in r_ins],
                                 [norm(o[2]) for o in o_ins], autojunk=False)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            pairs += [(i1 + k, j1 + k) for k in range(i2 - i1)]
        else:
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                pairs.append((i1 + k if i1 + k < i2 else None,
                              j1 + k if j1 + k < j2 else None))
    for (i, j) in pairs:
        r = r_ins[i] if i is not None else None
        o = o_ins[j] if j is not None else None
        rb = bytes.fromhex(r[1]) if r else b""
        ob = bytes.fromhex(o[1]) if o else b""
        cls = []
        for k in range(max(len(rb), len(ob))):
            if k < len(rb) and k < len(ob):
                if ooff[j] + k in mask:
                    cls.append("r")
                elif rb[k] == ob[k]:
                    cls.append("s")
                else:
                    cls.append("d")
            else:
                cls.append("d")
        same += sum(1 for c in cls if c != "d")
        total += len(cls)
        rows.append([r[0] if r else None, r[1] if r else None,
                     r[2] if r else None, (r[3] or None) if r else None,
                     o[0] if o else None, o[1] if o else None,
                     o[2] if o else None, (o[3] or None) if o else None,
                     "".join(cls)])
    return rows, same, total


class SourceIndex:
    """Where a function of ours is defined: the source file of its object
    (the one nearest the object, by path) and the line its name is defined
    on, as "path#Lline"."""

    EXT = (".cpp", ".c", ".cxx", ".cc", ".asm")

    def __init__(self, repo):
        self.repo = repo
        self.by_stem = {}
        for p in glob.glob(os.path.join(repo, "src", "**", "*"), recursive=True):
            if p.lower().endswith(self.EXT) and os.path.isfile(p):
                rel = os.path.relpath(p, repo)
                stem = os.path.splitext(os.path.basename(p))[0].lower()
                self.by_stem.setdefault(stem, []).append(rel)
        self.lines = {}
        self.cache = {}

    def find(self, mod, objpaths, sig, mangled):
        member = mod
        lib = ""
        m = re.match(r"(.*)\((.*)\)$", mod)
        if m:
            lib, member = m.group(1), m.group(2)
        stem = os.path.splitext(os.path.basename(member))[0].lower()
        cands = self.by_stem.get(stem, [])
        if not cands:
            return None
        near_to = objpaths.get(os.path.basename(member).lower(), "")
        if lib:
            near_to = "src/lithshared/" + lib
        path = max(cands, key=lambda c: (common(c, near_to), -len(c)))
        line = self.line(path, sig, mangled)
        return path + ("#L%d" % line if line else "")

    def line(self, path, sig, mangled):
        if path not in self.lines:
            try:
                self.lines[path] = open(os.path.join(self.repo, path),
                                        errors="replace").read().split("\n")
            except OSError:
                self.lines[path] = []
        text = self.lines[path]
        qual = shortname(sig, mangled, 0) if sig else ""
        if not qual and mangled:
            m = re.match(r"\?([A-Za-z_]\w*)@([A-Za-z_]\w*)@@", mangled)
            qual = "%s::%s" % (m.group(2), m.group(1)) if m else \
                mangled.lstrip("_?").split("@")[0]
        if not qual:
            return None
        qual = re.sub(r"<.*>", "", qual)
        pats = [re.compile(r"(?<![\w:])" + re.escape(qual) + r"\s*\(")]
        last = qual.split("::")[-1]
        if last != qual and not last.startswith(("operator", "`")):
            pats.append(re.compile(r"^[\w\s\*&:<>,]*\b" + re.escape(last) + r"\s*\("))
        for pat in pats:
            for i, l in enumerate(text):
                s = l.strip()
                if pat.search(l) and not s.endswith(";") and \
                        not s.startswith(("//", "*", "return", "if", "else")):
                    return i + 1
        return None


def common(a, b):
    a, b = a.lower().split("/"), b.lower().split("/")
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


if __name__ == "__main__":
    main()
