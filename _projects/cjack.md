---
order: 3
slug: cjack
title: Contract J.A.C.K.
subtitle: Between NOLF and NOLF 2 · version 1.1 (Europe) · 2003
repo: cjacksrc

# From the Progress table in cjacksrc's README.
progress:
  total: 96.4
  note: 27,763 of 29,566 functions · retail 1.1
  bars:
    - { name: ClientFx.fxd, pct: 99.9 }
    - { name: SndDrv.dll, pct: 99.7 }
    - { name: ContractJack.exe, pct: 99.2 }
    - { name: ContractJackServer.exe, pct: 99.0 }
    - { name: server.dll, pct: 97.2 }
    - { name: Object.lto, pct: 96.9 }
    - { name: Lithtech.exe, pct: 96.7 }
    - { name: GameSpy.dll, pct: 95.3 }
    - { name: CShell.dll, pct: 94.4 }
---

Monolith never released Contract J.A.C.K.'s source. But its binaries show it
was built from the same tree as NOLF 2 — so this project starts from NOLF 2's
game source and the LithTech Jupiter engine, and brings each function to what
the retail binaries are, compiled with Visual C++ .NET 2003 under Wine.

The newest of the three, and already well along: the launcher, dedicated
server, sound driver and client effects are all above 99%.

#### Modern build

- Unrestricted frame rates — 240 by default, or unlimited — with AI,
  movement, vehicles and effects behaving as they do at 60; multiplayer
  stays at 60
- Intro movies through our FFmpeg-based Bink player
- Speech (MP3) decoded in our own `SndDrv.dll` — no codec to install
- Multiplayer without GameSpy's dead CD-key servers, so clients can join
  again; the Internet server list, through
  [OpenSpy](https://openspy.net), is to come
