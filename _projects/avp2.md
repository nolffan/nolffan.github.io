---
order: 2
slug: avp2
nav: AvP2
title: Aliens versus Predator 2
subtitle: With the Primal Hunt expansion · 2001/2002
repo: avp2src
status: Work in progress · playable

# From the table in avp2src's progress/README.md.
progress:
  total: 91.7
  note: 50,472 of 55,918 functions · AvP2 1.0.9.6 and Primal Hunt 1.0.2.2
  bars:
    - { name: AVP2Serv.exe, pct: 99.6 }
    - { name: PrimalHunt.exe, pct: 99.3 }
    - { name: CShell.dll, pct: 98.6 }
    - { name: Object.lto, pct: 98.2 }
    - { name: PHObject.lto, pct: 95.2 }
    - { name: PHCShell.dll, pct: 94.4 }
    - { name: server.dll, pct: 84.6 }
    - { name: lithtech.exe, pct: 79.0 }
    - { name: d3d.ren, pct: 56.2 }
---

Both games — Aliens versus Predator 2 and Third Law's expansion, Primal
Hunt — each with its own engine, launcher, dedicated server and game DLLs,
compiled from source with the Visual C++ 6 builds that made them.

Monolith released AvP2's game code, but never the engine, and Primal Hunt's
code was never released at all. AvP2 runs on the same LithTech "Talon"
engine as NOLF, so its engine starts from our NOLF reconstruction, and
Primal Hunt's game code from Monolith's AvP2 source, each brought to what
the retail binaries are, function by function.

#### Modern build

- Widescreen and FOV, with an option to keep 4:3 cinematics
- Borderless window mode
- XInput controller support
- Raw mouse input
- High frame rates that play correctly
- Open-source audio and video, with [OpenMiles](https://github.com/maci0/openmiles) and FFmpeg
- Multiplayer backed by [OpenSpy](https://openspy.net)
- Every retail bug found so far, fixed
