---
order: 5
slug: tron20
nav: Tron 2.0
title: Tron 2.0
subtitle: Update 2 (v1.030) · 2003
repo: tron20src
status: Work in progress · not yet playable

# From the table in tron20src's progress/README.md.
progress:
  total: 64.7
  note: 26,340 of 37,327 functions · retail Update 2
  bars:
    - { name: Tron.exe, pct: 99.0 }
    - { name: server.dll, pct: 97.4 }
    - { name: Lithtech.exe, pct: 95.7 }
    - { name: CShell.dll, pct: 56.0 }
    - { name: Object.lto, pct: 48.6 }
---

Monolith never released Tron 2.0's source. It was built from the same tree
as NOLF 2, so this project starts from NOLF 2's source release, the Tron
code in the 2006 LithTech Jupiter distribution, and our NOLF 2 engine — and
brings each function to what the retail binaries are, compiled with Visual
C++ 6 under Wine.

The engine is already well along; the game code is where the work is now.

#### Planned for the modern build

- Widescreen and FOV, up to 8× AA and 16× AF
- XInput controller support
- Raw mouse input
- High frame rates that play correctly
- Our own Bink player on FFmpeg
