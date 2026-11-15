---
order: 1
slug: nolf
nav: NOLF
title: No One Lives Forever
subtitle: The Operative · Game of the Year Edition · 2000/2001
engine: LithTech 2.2
repo: nolfsrc
status: Playable
status_kind: good

gallery:
  - { src: /img/nolf-01-main-menu.jpg, caption: "The main menu", alt: "The main menu" }
  - { src: /img/nolf-02-unity-headquarters.jpg, caption: "UNITY headquarters", alt: "UNITY headquarters" }
  - { src: /img/nolf-03-morocco-rooftops.jpg, caption: "Misfortune in Morocco", alt: "Misfortune in Morocco: the rooftops of Marrakech" }
  - { src: /img/nolf-04-morocco-alley.jpg, caption: "Misfortune in Morocco", alt: "Misfortune in Morocco: a guard in an alley, with his shadow" }
  - { src: /img/nolf-05-berlin-by-night.jpg, caption: "Berlin by Night", alt: "Berlin by Night" }
  - { src: /img/nolf-06-plane.jpg, caption: "Unexpected Turbulence", alt: "Unexpected Turbulence: on board the plane" }
  - { src: /img/nolf-07-fireplace.jpg, caption: "The Dive", alt: "The Dive: a room with a fireplace" }
  - { src: /img/nolf-08-alpine-village.jpg, caption: "Alpine Intrigue", alt: "Alpine Intrigue: a village in the German Alps" }
gallery_caption: >-
  The modern build at 1920×1080: Direct3D 9 with antialiasing, model
  shadows, 32-bit textures and 16× anisotropic filtering.

# From the Progress table in nolfsrc's README.
progress:
  total: 84.9
  note: 17,946 of 19,855 functions · retail GOTY 1.004
  bars:
    - { name: Object.lto, pct: 98.9 }
    - { name: CShell.dll, pct: 98.8 }
    - { name: NOLF.exe, pct: 98.0 }
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
- High frame rates that play correctly
- Open-source audio and video, with [OpenMiles](https://github.com/maci0/openmiles) and FFmpeg
- Fixes and features from the NOLF Modernizer, reimplemented in source
- Bundled DirectMusic, so the music plays under Wine and Proton
- Multiplayer backed by [OpenSpy](https://openspy.net)
