---
order: 4
slug: lithtools
title: lithtools
subtitle: Tools for the LithTech games and their files
repo: lithtools

# `gallery_uncropped: true` shows the screenshots whole, instead of cropped
# to 16:9 as the game screenshots are: these are of applications.
gallery_uncropped: true
gallery:
  - src: /img/lithtools-lithrez-studio.png
    caption: LithRez Studio
    alt: "LithRez Studio: No One Lives Forever 2's GAME.REZ open, previewing Cate Archer's model with its pieces, sockets and skins"
  - src: /img/lithtools-blender.png
    caption: The Blender extension
    alt: "Blender: No One Lives Forever 2's mime model imported with its LODs, and the LithTech Animations panel"

# A project with `tools` is shown as a grid of cards instead of the
# progress panel. Each card shows `icon` (an image) or else `glyph` (a
# letter); `progress` adds a bar.
tools:
  - title: lithrez & LithRez Studio
    icon: /img/lithrez-studio.png
    text: >-
      A command-line tool whose classic commands behave like Monolith's
      LITHREZ and write byte-identical `.rez` archives; and a Qt 6 successor
      to WinRez LT Studio with texture, model and sound previews and a
      string-table editor. Linux, macOS and Windows.
  - title: Blender extension
    glyph: B
    text: >-
      Imports and exports LithTech models — `.abc`, `.ltb` and the PS2's
      `.ltb` — and DTX textures.
  - title: Talon tools, decompiled
    glyph: T
    progress: 56.9
    text: >-
      DEdit, ModelEdit, the world processors and the 3ds Max and Maya
      plug-ins from NOLF and AvP2, reconstructed as C++ that compiles to the
      shipped binaries. **56.9%** byte-identical so far.
  - title: Jupiter tools
    glyph: J
    text: >-
      The tools of NOLF 2, Contract J.A.C.K. and Tron 2.0 — DEdit, ModelEdit,
      FxED, the packers — built from Jupiter Build 69's source.

footnote: >-
  Plus an inventory of every public LithTech tools release, and a map of
  which format versions each game and tool reads and writes.
---

For NOLF, Aliens versus Predator 2, NOLF 2, Contract J.A.C.K., Tron 2.0 and
the rest of that era: modern, cross-platform tools for the files these games
ship — and the original development tools, archived and reconstructed for
research.
