---
order: 3
slug: nolf2
nav: NOLF 2
title: No One Lives Forever 2
subtitle: A Spy in H.A.R.M.'s Way · version 1.3 · 2002
engine: LithTech Jupiter
repo: nolf2src
status: Playable
status_kind: good

gallery:
  - { src: /img/nolf2-00-main-menu.jpg, caption: "The main menu", alt: "The main menu" }
  - { src: /img/nolf2-01-ninja.jpg, caption: "Japan", alt: "A ninja runs across a Japanese courtyard at night, seen over a crossbow" }
  - { src: /img/nolf2-02-hurricane.jpg, caption: "Serenity Valley", alt: "A cut-scene: the Serenity Valley trailer court sign under a storm sky" }
  - { src: /img/nolf2-03-katana-fight.jpg, caption: "Isako", alt: "A katana fight with Isako in a trailer" }
  - { src: /img/nolf2-04-kate.jpg, caption: "Oh, hello, Cate", alt: "A cut-scene in a night street: Oh, hello, Cate." }
  - { src: /img/nolf2-05-unity.jpg, caption: "UNITY headquarters", alt: "A cut-scene: a briefing at UNITY headquarters" }
  - { src: /img/nolf2-06-lava.jpg, caption: "The lava cave", alt: "A cut-scene: catwalks over a lava cave" }
  - { src: /img/nolf2-07-india.jpg, caption: "Calcutta", alt: "A street in Calcutta, seen over a pistol" }

# From the Progress table in nolf2src's README.
progress:
  total: 98.1
  note: 29,261 of 32,894 functions · retail 1.3, engine included
  bars:
    - { name: CShell.dll, pct: 99.0 }
    - { name: NOLF2.exe, pct: 98.7 }
    - { name: Object.lto, pct: 98.7 }
    - { name: server.dll, pct: 97.5 }
    - { name: Lithtech.exe, pct: 95.9 }
---

The game code is Monolith's public source release of 1.3, the game's last
update, compiled with Visual C++ 6 SP5 as retail was.

The engine — `Lithtech.exe` and `server.dll` — is built from the 2006
LithTech Jupiter source, back-ported to 2002. The sound driver and message DLL
are reconstructed from the retail binaries, and the server directory from
Monolith's Titan code. Nothing of the retail engine remains in the game
directory.

#### Modern build

- Widescreen and FOV, up to 8× AA and 16× AF
- XInput controller support
- High frame rates that play correctly
- Our own Bink player on FFmpeg — no RAD binaries
- NOLF 2 Modernizer fixes, reimplemented in source
