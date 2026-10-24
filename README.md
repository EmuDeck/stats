# Estadísticas de EmuDeck

Actualizado: 2026-10-24 01:47 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13039 | 95557 |
| Linux ARM | 153 | 1112 |
| Windows | 3317 | 24907 |
| Mac | 0 | 1 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2061**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272, 12219, 13039]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186, 138, 153]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183, 3270, 3317]
```

```mermaid
xychart-beta
    title "Arranques Mac"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Arranques"
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 42 | 207 | 573 | 596 |
| linux-arm | 6 | 31 | 89 | 92 |
| windows | 2 | 78 | 150 | 157 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32, 23, 42]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6, 2, 6]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11, 11, 2]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757, 793, 843]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 573 | 89 | 150 | 812 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 224 | 580 | 604 |
| Con CloudSync | 327 | 831 | 896 |
| % con CloudSync | | | 148% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34, 25, 37]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25, 49, 43]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1589 | 20 | 184 | 690 | 1716 | 1793 |
| duckstation | 1529 | 122 | 78 | 677 | 1654 | 1729 |
| azahar | 1407 | 132 | 181 | 659 | 1642 | 1720 |
| ryujinx | 1364 | 130 | 183 | 654 | 1609 | 1677 |
| esde | 1279 | 102 | 286 | 643 | 1570 | 1667 |
| rpcs3 | 1433 | 119 | 75 | 638 | 1556 | 1627 |
| cemu | 1412 | 127 | 59 | 625 | 1532 | 1598 |
| srm | 1265 | 112 | 189 | 653 | 1515 | 1566 |
| xenia | 1294 | 104 | 149 | 606 | 1486 | 1547 |
| shadps4 | 1216 | 105 | 132 | 567 | 1387 | 1453 |
| vita3k | 1278 | 110 | 49 | 560 | 1372 | 1437 |
| cloudsync | 630 | 25 | 274 | 339 | 862 | 929 |
| ra | 572 | 82 | 92 | 275 | 717 | 746 |
| ppsspp | 527 | 77 | 136 | 271 | 709 | 740 |
| dolphin | 573 | 84 | 81 | 261 | 709 | 738 |
| mgba | 562 | 46 | 45 | 249 | 629 | 653 |
| melonds | 494 | 67 | 59 | 222 | 593 | 620 |
| xemu | 493 | 69 | 58 | 227 | 595 | 620 |
| primehack | 429 | 65 | 59 | 200 | 527 | 553 |
| supermodel | 421 | 80 | 13 | 175 | 494 | 514 |
| model2 | 416 | 83 | 7 | 171 | 486 | 506 |
| scummvm | 409 | 58 | 36 | 181 | 480 | 503 |
| bigpemu | 396 | 7 | 10 | 169 | 395 | 413 |
| armsx2 | 120 | 135 | 0 | 99 | 245 | 255 |
| flycast | 116 | 14 | 15 | 50 | 140 | 145 |
| rmg | 108 | 26 | 0 | 42 | 130 | 134 |
| eden | 73 | 7 | 0 | 38 | 72 | 80 |
| mame | 64 | 2 | 14 | 23 | 76 | 80 |
| pegasus | 11 | 0 | 12 | 7 | 21 | 23 |
| ares | 6 | 1 | 0 | 3 | 7 | 7 |
| yuzu | 7 | 0 | 0 | 1 | 7 | 7 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
