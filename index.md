---
layout: default

hero:
  kicker: Classified · For preservation purposes
  title: The LithTech games, rebuilt from source.
  lede: >-
    We reconstruct Monolith's early-2000s games and their engine so that
    every executable and DLL compiles back to the exact bytes that shipped,
    with the original compilers. Then we build a *modern* edition on top:
    widescreen, controllers, restored multiplayer, open-source middleware,
    and the retail bugs fixed.

approach:
  title: The approach
  cards:
    - title: Byte for byte
      text: >-
        Each function is written so the period compiler — Visual C++ 6,
        .NET 2003, Intel C/C++ — turns it into exactly the retail machine
        code. A scoreboard checks every one, and the build fails if a
        matching function ever stops matching.
    - title: Two builds
      text: >-
        **Legacy** is the game as it shipped, bugs and all — a faithful
        record. **Modern** is the same source with fixes and new features,
        kept behind a define so the legacy build keeps matching.
    - title: No game data
      text: >-
        The repositories contain source only. Public releases come with
        install scripts that copy the data out of *your own* disc images,
        checking every file against verified redump.org checksums.
    - title: Plays today
      text: >-
        Builds run under Wine and Proton on Linux and the Steam Deck, on
        macOS through CrossOver, and natively on Windows.

footer: >-
  Not made or supported by Monolith Productions. No game data is hosted
  here — you need your own copies of the games.
---

## With thanks

1. **Monolith Productions**, for the games, and for releasing their source.
2. **LithTech, Inc.** (later **Touchdown Entertainment**), for the Jupiter
   engine.
3. [**StenApp**](https://github.com/StenApp), for an in-depth knowledge of
   all things NOLF and LithTech.
4. **HeyThereCoffeee (haekb)**, for the
   [NOLF](https://github.com/haekb/nolf1-modernizer) and
   [NOLF 2](https://github.com/haekb/nolf2-modernizer) Modernizers.
5. [**ChthonVII**](https://github.com/ChthonVII/nolf1-modernizer) and
   **Daniel Gibson**, for their Modernizer fixes.
6. [**OpenSpy**](https://openspy.net), whose master server brings the
   internet server lists back to life.
7. [**OpenMiles**](https://github.com/maci0/openmiles), the open
   reimplementation of the Miles Sound System.
8. [**FFmpeg**](https://ffmpeg.org), which our Bink player is built on.
9. **Wine**, **Proton** and **DXVK**, which run the games on Linux and the
   Steam Deck.
10. **redump.org** and **archive.org**, for verifying and keeping the discs.
