# Estadísticas de EmuDeck

Actualizado: 2026-10-16 02:44 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 23 | 263 | 339 | 364 |
| linux-arm | 5 | 38 | 50 | 53 |
| windows | 8 | 53 | 69 | 78 |

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
| Instalaciones early | 263 | 331 | 360 |
| Con CloudSync | 349 | 476 | 543 |
| % con CloudSync | | | 151% |

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
| pcsx2 | 910 | 16 | 109 | 729 | 948 | 1035 |
| azahar | 818 | 72 | 103 | 706 | 905 | 993 |
| duckstation | 877 | 70 | 37 | 702 | 899 | 984 |
| esde | 746 | 62 | 156 | 671 | 860 | 964 |
| ryujinx | 779 | 73 | 102 | 684 | 877 | 954 |
| rpcs3 | 820 | 71 | 34 | 670 | 847 | 925 |
| cemu | 821 | 72 | 23 | 669 | 845 | 916 |
| xenia | 744 | 59 | 78 | 641 | 811 | 881 |
| srm | 710 | 52 | 78 | 608 | 786 | 840 |
| shadps4 | 702 | 59 | 67 | 588 | 751 | 828 |
| vita3k | 738 | 61 | 17 | 593 | 745 | 816 |
| cloudsync | 395 | 16 | 153 | 364 | 495 | 564 |
| dolphin | 356 | 51 | 43 | 325 | 415 | 450 |
| ppsspp | 321 | 47 | 74 | 322 | 406 | 442 |
| ra | 353 | 51 | 37 | 312 | 407 | 441 |
| mgba | 329 | 26 | 21 | 273 | 351 | 376 |
| melonds | 308 | 39 | 26 | 268 | 341 | 373 |
| xemu | 301 | 40 | 27 | 269 | 338 | 368 |
| primehack | 269 | 41 | 26 | 240 | 307 | 336 |
| supermodel | 267 | 47 | 8 | 241 | 298 | 322 |
| model2 | 261 | 50 | 4 | 231 | 291 | 315 |
| scummvm | 258 | 36 | 13 | 225 | 279 | 307 |
| bigpemu | 228 | 3 | 6 | 180 | 218 | 237 |
| armsx2 | 73 | 75 | 0 | 109 | 138 | 148 |
| flycast | 73 | 11 | 5 | 62 | 84 | 89 |
| rmg | 67 | 19 | 0 | 60 | 82 | 86 |
| mame | 44 | 2 | 9 | 34 | 51 | 55 |
| eden | 33 | 7 | 0 | 31 | 31 | 40 |
| pegasus | 9 | 0 | 7 | 13 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
