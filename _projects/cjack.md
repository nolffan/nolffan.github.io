---
order: 4
slug: cjack
title: Contract J.A.C.K.
subtitle: A prequel to NOLF 2 · version 1.1 (Europe) · 2003
engine: LithTech Jupiter
repo: cjacksrc
status: Playable
status_kind: good

gallery:
  - { src: /img/cjack-00-main-menu.jpg, caption: "The main menu", alt: "The main menu" }
  - { src: /img/cjack-01-scene-one.jpg, caption: "The first mission", alt: "Two mobsters in a hotel room: 'Shut your hole before I shovel dirt in it, Marvin.'" }
  - { src: /img/cjack-02-shooting.jpg, caption: "A shoot-out", alt: "A shoot-out with mobsters in a hotel apartment, seen over a Tommy gun" }
  - { src: /img/cjack-03-car.jpg, caption: "The garage", alt: "A car in a garage, seen over a Tommy gun" }
  - { src: /img/cjack-04-malta.jpg, caption: "Malta", alt: "Ruins in Malta, seen over a pistol" }
  - { src: /img/cjack-05-dimitri.jpg, caption: "A job offer", alt: "A cut-scene: 'Bravo. You've passed the test. Now, then, I have a job for you.'" }
  - { src: /img/cjack-06-damage.jpg, caption: "In the snow", alt: "A firefight among shipping containers in the snow, seen over a pistol" }
  - { src: /img/cjack-07-machine-gun.jpg, caption: "The rail yard", alt: "A snowy rail yard at night, seen over a submachine gun" }

# From the Progress table in cjacksrc's README.
progress:
  total: 96.4
  note: 27,763 of 29,566 functions · retail 1.1
  bars:
    - { name: ContractJack.exe, pct: 99.2 }
    - { name: server.dll, pct: 97.2 }
    - { name: Object.lto, pct: 96.9 }
    - { name: Lithtech.exe, pct: 96.7 }
    - { name: CShell.dll, pct: 94.4 }
---

Monolith never released Contract J.A.C.K.'s source. But its binaries show it
was built from the same tree as NOLF 2 — so this project starts from NOLF 2's
game source and the LithTech Jupiter engine, and brings each function to what
the retail binaries are, compiled with Visual C++ .NET 2003 under Wine.

#### Modern build

- Widescreen and FOV
- XInput controller support
- High frame rates that play correctly
- Intro movies through our FFmpeg-based Bink player
- Speech plays with no codec to install
- NOLF 2 Modernizer fixes, carried over
