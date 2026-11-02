---
order: 2
slug: nolf2
nav: NOLF 2
title: No One Lives Forever 2
subtitle: A Spy in H.A.R.M.'s Way · version 1.3 · 2002
repo: nolf2src

gallery:
  - { src: /img/nolf2-menu.png, caption: The main menu, alt: "The main menu, running from this build" }
  - { src: /img/nolf2-ingame.png, caption: In game, alt: "In game, running from this build" }

# From the Progress table in nolf2src's README.
progress:
  total: 98.1
  note: 29,261 of 32,894 functions · retail 1.3, engine included
  bars:
    - { name: ClientFx.fxd, pct: 100 }
    - { name: ServerDir.dll, pct: 99.5 }
    - { name: CShell.dll, pct: 99.0 }
    - { name: snddrv.dll, pct: 98.8 }
    - { name: NOLF2Srv.exe, pct: 98.8 }
    - { name: NOLF2.exe, pct: 98.7 }
    - { name: Object.lto, pct: 98.7 }
    - { name: server.dll, pct: 97.5 }
    - { name: Lithtech.exe, pct: 95.9 }
---

The game code is Monolith's public source release of 1.3, the game's last
update, compiled with Visual C++ 6 SP5 as retail was. Where the release
differs from what actually shipped, the retail code is reconstructed in place
and marked `RETAIL:`.

The engine — `Lithtech.exe` and `server.dll` — is built from the 2006
LithTech Jupiter source, back-ported to 2002. The sound driver and message DLL
are reconstructed from the retail binaries, and the server directory from
Monolith's Titan code. Nothing of the retail engine remains in the game
directory.

#### Modern build

- Widescreen with field of view, up to 8× AA and 16× AF, DPI-aware
- XInput controllers; A skips cut-scenes
- Unrestricted frame rates — 240 by default, up to 300 or unlimited — with
  AI, movement, weather and effects behaving as they do at 60;
  multiplayer stays at 60
- Our own Bink player on FFmpeg — no RAD binaries
- NOLF 2 Modernizer fixes, reimplemented in source
- Multiplayer restored: with Sierra's CD-key servers gone, retail can no
  longer join an Internet server or one by address; the modern build drops
  the key check so those work again, and servers are hardened against
  crashes
