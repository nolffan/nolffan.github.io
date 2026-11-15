---
order: 2
slug: avp2
nav: AvP2
title: Aliens versus Predator 2
subtitle: With the Primal Hunt expansion · 2001/2002
engine: LithTech Talon
repo: avp2src
status: Work in progress · playable
status_kind: warn

gallery:
  - { src: /img/avp2-main-menu.jpg, caption: "The main menu", alt: "The main menu of Aliens versus Predator 2" }
  - { src: /img/avp2-space-ship.jpg, caption: "The USS Verloc", alt: "The opening of the Marine campaign: the USS Verloc approaches the orbit of LV-1201" }
  - { src: /img/avp2-marine.jpg, caption: "The Marine campaign", alt: "The Marine campaign: marines outside a building in a canyon at night" }
  - { src: /img/avp2-predator.jpg, caption: "The Predator campaign", alt: "The Predator campaign, seen through a vision mode of the Predator" }
  - { src: /img/avp2ph-alien-1.jpg, caption: "Primal Hunt: the Alien campaign", alt: "Primal Hunt's Alien campaign: an alien in a hive, with more beyond" }
  - { src: /img/avp2ph-alien-2.jpg, caption: "Primal Hunt: the Alien campaign", alt: "Primal Hunt's Alien campaign: aliens in a corridor, seen through the Alien's vision" }
  - { src: /img/avp2ph-corporate-1.jpg, caption: "Primal Hunt: the Corporate campaign", alt: "Primal Hunt's Corporate campaign: a soldier fires a flamethrower down a corridor" }
  - { src: /img/avp2ph-corporate-2.jpg, caption: "Primal Hunt: the Corporate campaign", alt: "Primal Hunt's Corporate campaign: soldiers fight aliens with flamethrowers" }

# From the table in avp2src's progress/README.md.
progress:
  total: 91.7
  note: 50,472 of 55,918 functions · AvP2 1.0.9.6 and Primal Hunt 1.0.2.2
  bars:
    - { name: PrimalHunt.exe, pct: 99.3 }
    - { name: CShell.dll, pct: 98.6 }
    - { name: Object.lto, pct: 98.2 }
    - { name: PHObject.lto, pct: 95.2 }
    - { name: AVP2.exe, pct: 94.6 }
    - { name: PHCShell.dll, pct: 94.4 }
    - { name: server.dll, pct: 84.6 }
    - { name: lithtech.exe, pct: 79.0 }
    - { name: d3d.ren, pct: 56.2 }
---

Both games — Aliens versus Predator 2 and Third Law's expansion, Primal
Hunt — each with its own engine, launcher, dedicated server and game DLLs,
compiled from source with the Visual C++ 6 builds that made them.

Monolith released AvP2's game code, but never the engine, and Primal Hunt's
code was never released at all. AvP2's engine grew out of NOLF's, so it
starts from our NOLF reconstruction, and Primal Hunt's game code from
Monolith's AvP2 source, each brought to what the retail binaries are,
function by function.

#### Modern build

- Widescreen and FOV, with an option to keep 4:3 cinematics
- Borderless window mode
- XInput controller support
- Raw mouse input
- High frame rates that play correctly
- Open-source audio and video, with [OpenMiles](https://github.com/maci0/openmiles) and FFmpeg
- Multiplayer backed by [OpenSpy](https://openspy.net)
- Every retail bug found so far, fixed
