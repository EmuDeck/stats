# Estadísticas de EmuDeck

Actualizado: 2026-10-16 00:35 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13181 | 98292 |
| Linux ARM | 147 | 1179 |
| Windows | 3355 | 25977 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1731**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 23 | 263 | 339 | 361 |
| linux-arm | 5 | 38 | 50 | 53 |
| windows | 8 | 53 | 69 | 77 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 339 | 50 | 69 | 458 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 263 | 331 | 356 |
| Con CloudSync | 349 | 476 | 541 |
| % con CloudSync | | | 152% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 904 | 16 | 108 | 729 | 948 | 1028 |
| azahar | 813 | 71 | 102 | 706 | 905 | 986 |
| duckstation | 872 | 69 | 36 | 702 | 899 | 977 |
| esde | 741 | 61 | 154 | 671 | 860 | 956 |
| ryujinx | 774 | 73 | 102 | 684 | 877 | 949 |
| rpcs3 | 813 | 71 | 34 | 670 | 847 | 918 |
| cemu | 817 | 72 | 23 | 669 | 845 | 912 |
| xenia | 740 | 59 | 76 | 641 | 811 | 875 |
| srm | 709 | 52 | 76 | 608 | 786 | 837 |
| shadps4 | 696 | 58 | 65 | 588 | 751 | 819 |
| vita3k | 734 | 61 | 17 | 593 | 745 | 812 |
| cloudsync | 393 | 16 | 153 | 364 | 495 | 562 |
| dolphin | 352 | 51 | 43 | 325 | 415 | 446 |
| ppsspp | 318 | 47 | 74 | 322 | 406 | 439 |
| ra | 350 | 51 | 35 | 312 | 407 | 436 |
| mgba | 328 | 26 | 21 | 273 | 351 | 375 |
| melonds | 305 | 39 | 26 | 268 | 341 | 370 |
| xemu | 298 | 40 | 27 | 269 | 338 | 365 |
| primehack | 266 | 41 | 26 | 240 | 307 | 333 |
| supermodel | 264 | 47 | 8 | 241 | 298 | 319 |
| model2 | 258 | 50 | 4 | 231 | 291 | 312 |
| scummvm | 255 | 36 | 13 | 225 | 279 | 304 |
| bigpemu | 228 | 3 | 6 | 180 | 218 | 237 |
| armsx2 | 73 | 74 | 0 | 109 | 138 | 147 |
| flycast | 73 | 11 | 5 | 62 | 84 | 89 |
| rmg | 67 | 19 | 0 | 60 | 82 | 86 |
| mame | 44 | 2 | 9 | 34 | 51 | 55 |
| eden | 33 | 6 | 0 | 31 | 31 | 39 |
| pegasus | 9 | 0 | 7 | 13 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
