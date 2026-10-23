# Estadísticas de EmuDeck

Actualizado: 2026-10-23 04:16 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12219 | 95615 |
| Linux ARM | 138 | 1095 |
| Windows | 3270 | 25184 |
| Mac | 1 | 1 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2120**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272, 12219]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186, 138]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183, 3270]
```

```mermaid
xychart-beta
    title "Arranques Mac"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Arranques"
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 23 | 192 | 531 | 559 |
| linux-arm | 2 | 33 | 83 | 88 |
| windows | 11 | 79 | 148 | 156 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32, 23]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6, 2]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11, 11]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757, 793]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 531 | 83 | 148 | 762 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 212 | 543 | 576 |
| Con CloudSync | 312 | 788 | 864 |
| % con CloudSync | | | 150% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34, 25]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25, 49]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1507 | 20 | 182 | 664 | 1612 | 1709 |
| duckstation | 1455 | 114 | 71 | 643 | 1542 | 1640 |
| azahar | 1335 | 121 | 177 | 629 | 1534 | 1633 |
| esde | 1221 | 93 | 283 | 624 | 1484 | 1597 |
| ryujinx | 1295 | 118 | 176 | 617 | 1494 | 1589 |
| rpcs3 | 1357 | 113 | 73 | 603 | 1450 | 1543 |
| cemu | 1339 | 115 | 56 | 579 | 1424 | 1510 |
| srm | 1203 | 101 | 183 | 635 | 1421 | 1487 |
| xenia | 1224 | 96 | 147 | 573 | 1384 | 1467 |
| shadps4 | 1150 | 95 | 131 | 540 | 1291 | 1376 |
| vita3k | 1214 | 100 | 47 | 533 | 1278 | 1361 |
| cloudsync | 607 | 25 | 261 | 320 | 815 | 893 |
| ra | 536 | 78 | 90 | 259 | 666 | 704 |
| ppsspp | 494 | 74 | 134 | 254 | 660 | 702 |
| dolphin | 541 | 80 | 79 | 243 | 658 | 700 |
| mgba | 539 | 43 | 42 | 241 | 592 | 624 |
| melonds | 468 | 63 | 57 | 206 | 547 | 588 |
| xemu | 461 | 65 | 55 | 208 | 546 | 581 |
| primehack | 402 | 61 | 57 | 179 | 486 | 520 |
| supermodel | 395 | 75 | 12 | 156 | 454 | 482 |
| model2 | 390 | 78 | 7 | 156 | 447 | 475 |
| scummvm | 385 | 54 | 35 | 163 | 442 | 474 |
| bigpemu | 378 | 7 | 10 | 147 | 365 | 395 |
| armsx2 | 118 | 125 | 0 | 90 | 228 | 243 |
| flycast | 104 | 14 | 13 | 40 | 124 | 131 |
| rmg | 102 | 26 | 0 | 41 | 123 | 128 |
| eden | 72 | 7 | 0 | 40 | 71 | 79 |
| mame | 59 | 2 | 14 | 18 | 69 | 75 |
| pegasus | 11 | 0 | 11 | 6 | 20 | 22 |
| ares | 5 | 1 | 0 | 2 | 6 | 6 |
| yuzu | 6 | 0 | 0 | 0 | 6 | 6 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
