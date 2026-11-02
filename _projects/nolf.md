---
order: 1
slug: nolf
nav: NOLF
title: No One Lives Forever
subtitle: The Operative · Game of the Year Edition · 2000/2001
repo: nolfsrc

gallery:
  - { src: /img/nolf-01-main-menu.jpg, caption: The main menu }
  - { src: /img/nolf-03-morocco-rooftops.jpg, caption: Misfortune in Morocco, alt: The rooftops of Marrakech }
  - { src: /img/nolf-05-berlin-by-night.jpg, caption: Berlin by Night }
  - { src: /img/nolf-08-alpine-village.jpg, caption: Alpine Intrigue, alt: A village in the German Alps }
gallery_caption: >-
  The modern build at 1920×1080: Direct3D 9 with antialiasing, model
  shadows, 32-bit textures and 16× anisotropic filtering.

# From the Progress table in nolfsrc's README.
progress:
  total: 84.9
  note: 17,946 of 19,855 functions · retail GOTY 1.003
  bars:
    - { name: NolfServ.exe, pct: 99.2 }
    - { name: Object.lto, pct: 98.9 }
    - { name: CShell.dll, pct: 98.8 }
    - { name: NOLF.exe, pct: 98.0 }
    - { name: libraries, pct: 97.7 }
    - { name: server.dll, pct: 85.5 }
    - { name: lithtech.exe, pct: 77.8 }
    - { name: d3d.ren, pct: 28.3 }
---

Every binary of the game — the LithTech engine (`lithtech.exe`,
`server.dll`, the `d3d.ren` renderer), the launcher, the dedicated server and
the three game DLLs — compiled from source with the original 2000-era
compilers.

Monolith never released the engine source, so `src/engine/` is a
reconstruction written to recompile to the retail machine code. The game code
is Monolith's own v1.003 source release, with the Game of the Year changes
reconstructed from the retail DLLs.

#### Modern build

- Direct3D 9 renderer, widescreen, AA and anisotropic filtering
- XInput controller support
- [OpenMiles](https://github.com/maci0/openmiles) and an FFmpeg-based Bink player replace proprietary middleware
- Fixes and features from the NOLF Modernizer, reimplemented in source
- Bundled DirectMusic, so the music plays under Wine and Proton
- Multiplayer restored: the internet server list works again through
  OpenSpy, and servers check passwords and no longer crash on a `%` in a
  name
