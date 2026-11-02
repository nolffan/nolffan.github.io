---
layout: default

hero:
  kicker: Classified · For preservation purposes
  title: The LithTech games, rebuilt from source.
  lede: >-
    We reconstruct Monolith's early-2000s games and their engine so that
    every executable and DLL compiles back to the exact bytes that shipped,
    with the original compilers. Then we build a *modern* edition on top:
    widescreen, controllers, open-source middleware, and the retail bugs
    fixed.

approach:
  title: The approach
  cards:
    - title: Byte for byte
      text: >-
        Each function is written so the period compiler — Visual C++ 6,
        .NET 2003, Intel C/C++ — turns it into exactly the retail machine
        code. A scoreboard checks every one, and the build fails if a
        matching function ever stops matching.
    - title: Two builds
      text: >-
        **Legacy** is the game as it shipped, bugs and all — a faithful
        record. **Modern** is the same source with fixes and new features,
        kept behind a define so the legacy build keeps matching.
    - title: No game data
      text: >-
        The repositories contain source only. Public releases come with
        install scripts that copy the data out of *your own* disc images,
        checking every file against verified redump.org checksums.
    - title: Plays today
      text: >-
        Builds run under Wine and Proton on Linux and the Steam Deck, on
        macOS through CrossOver, and natively on Windows.

footer: >-
  Not made or supported by Monolith Productions. No game data is hosted
  here — you need your own copies of the games.
---

## Get involved

Every repository builds with one `make` on Linux with Docker: the period
compilers, the retail game fetch and the install all come along as
submodules. The `guides/` walk through the method — from reading the retail
machine code to the compiler quirks that decide the last few bytes — and
`make progress` shows where things stand.

Found a bug in the original games along the way? Each project keeps a
`RETAIL_BUGS.md`.

## With thanks

**Monolith Productions**, for the games and for releasing their source;
**LithTech, Inc. / Touchdown Entertainment** for the Jupiter engine;
[StenApp](https://github.com/StenApp) for an in-depth knowledge of all things
NOLF and LithTech; **HeyThereCoffeee (haekb)** for the NOLF and NOLF 2
Modernizers; ChthonVII and Daniel Gibson; OpenMiles, FFmpeg, Wine, Proton,
DXVK and OpenSpy; and redump.org and archive.org for keeping the discs.
