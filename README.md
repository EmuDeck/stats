# Estadísticas de EmuDeck

Actualizado: 2026-10-16 22:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 23 | 263 | 339 | 386 |
| linux-arm | 5 | 38 | 50 | 61 |
| windows | 8 | 53 | 69 | 79 |

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
| Instalaciones early | 263 | 331 | 378 |
| Con CloudSync | 349 | 476 | 566 |
| % con CloudSync | | | 150% |

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
| pcsx2 | 970 | 17 | 110 | 729 | 948 | 1097 |
| azahar | 874 | 77 | 104 | 706 | 905 | 1055 |
| duckstation | 934 | 76 | 37 | 702 | 899 | 1047 |
| ryujinx | 832 | 77 | 109 | 684 | 877 | 1018 |
| esde | 792 | 66 | 156 | 671 | 860 | 1014 |
| rpcs3 | 873 | 75 | 34 | 670 | 847 | 982 |
| cemu | 869 | 75 | 23 | 669 | 845 | 967 |
| xenia | 795 | 62 | 79 | 641 | 811 | 936 |
| srm | 758 | 63 | 83 | 608 | 786 | 904 |
| shadps4 | 749 | 63 | 69 | 588 | 751 | 881 |
| vita3k | 789 | 66 | 17 | 593 | 745 | 872 |
| cloudsync | 412 | 16 | 159 | 364 | 495 | 587 |
| dolphin | 378 | 54 | 43 | 325 | 415 | 475 |
| ppsspp | 342 | 51 | 74 | 322 | 406 | 467 |
| ra | 375 | 55 | 37 | 312 | 407 | 467 |
| mgba | 347 | 32 | 21 | 273 | 351 | 400 |
| melonds | 328 | 41 | 27 | 268 | 341 | 396 |
| xemu | 320 | 44 | 28 | 269 | 338 | 392 |
| primehack | 281 | 43 | 26 | 240 | 307 | 350 |
| supermodel | 280 | 50 | 8 | 241 | 298 | 338 |
| model2 | 276 | 53 | 5 | 231 | 291 | 334 |
| scummvm | 270 | 38 | 13 | 225 | 279 | 321 |
| bigpemu | 235 | 3 | 6 | 180 | 218 | 244 |
| armsx2 | 73 | 81 | 0 | 109 | 138 | 154 |
| flycast | 78 | 12 | 5 | 62 | 84 | 95 |
| rmg | 72 | 20 | 0 | 60 | 82 | 92 |
| mame | 46 | 2 | 9 | 34 | 51 | 57 |
| eden | 35 | 7 | 0 | 31 | 31 | 42 |
| pegasus | 9 | 0 | 7 | 13 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
