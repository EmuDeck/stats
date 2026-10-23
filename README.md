# Estadísticas de EmuDeck

Actualizado: 2026-10-23 23:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 23 | 192 | 531 | 594 |
| linux-arm | 2 | 33 | 83 | 91 |
| windows | 11 | 79 | 148 | 157 |

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
| Instalaciones early | 212 | 543 | 602 |
| Con CloudSync | 312 | 788 | 895 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 1584 | 20 | 184 | 664 | 1612 | 1788 |
| duckstation | 1526 | 120 | 76 | 643 | 1542 | 1722 |
| azahar | 1404 | 130 | 181 | 629 | 1534 | 1715 |
| ryujinx | 1363 | 128 | 183 | 617 | 1494 | 1674 |
| esde | 1275 | 99 | 286 | 624 | 1484 | 1660 |
| rpcs3 | 1428 | 118 | 75 | 603 | 1450 | 1621 |
| cemu | 1410 | 124 | 59 | 579 | 1424 | 1593 |
| srm | 1261 | 110 | 189 | 635 | 1421 | 1560 |
| xenia | 1291 | 103 | 149 | 573 | 1384 | 1543 |
| shadps4 | 1214 | 103 | 132 | 540 | 1291 | 1449 |
| vita3k | 1277 | 107 | 49 | 533 | 1278 | 1433 |
| cloudsync | 629 | 25 | 274 | 320 | 815 | 928 |
| ra | 571 | 81 | 92 | 259 | 666 | 744 |
| ppsspp | 527 | 76 | 136 | 254 | 660 | 739 |
| dolphin | 573 | 83 | 81 | 243 | 658 | 737 |
| mgba | 560 | 46 | 44 | 241 | 592 | 650 |
| melonds | 494 | 66 | 59 | 206 | 547 | 619 |
| xemu | 493 | 68 | 58 | 208 | 546 | 619 |
| primehack | 427 | 64 | 59 | 179 | 486 | 550 |
| supermodel | 421 | 79 | 13 | 156 | 454 | 513 |
| model2 | 416 | 82 | 7 | 156 | 447 | 505 |
| scummvm | 409 | 57 | 36 | 163 | 442 | 502 |
| bigpemu | 396 | 7 | 10 | 147 | 365 | 413 |
| armsx2 | 120 | 133 | 0 | 90 | 228 | 253 |
| flycast | 116 | 14 | 15 | 40 | 124 | 145 |
| rmg | 108 | 26 | 0 | 41 | 123 | 134 |
| eden | 73 | 7 | 0 | 40 | 71 | 80 |
| mame | 64 | 2 | 14 | 18 | 69 | 80 |
| pegasus | 11 | 0 | 12 | 6 | 20 | 23 |
| ares | 6 | 1 | 0 | 2 | 6 | 7 |
| yuzu | 7 | 0 | 0 | 0 | 6 | 7 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
