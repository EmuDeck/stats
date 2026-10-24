# Estadísticas de EmuDeck

Actualizado: 2026-10-24 18:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 207 | 573 | 612 |
| linux-arm | 6 | 31 | 89 | 99 |
| windows | 2 | 78 | 150 | 160 |

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
| Instalaciones early | 224 | 580 | 618 |
| Con CloudSync | 327 | 831 | 912 |
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
| pcsx2 | 1660 | 21 | 188 | 690 | 1716 | 1869 |
| duckstation | 1590 | 130 | 81 | 677 | 1654 | 1801 |
| azahar | 1466 | 143 | 185 | 659 | 1642 | 1794 |
| ryujinx | 1417 | 142 | 191 | 654 | 1609 | 1750 |
| esde | 1341 | 107 | 299 | 643 | 1570 | 1747 |
| rpcs3 | 1490 | 130 | 76 | 638 | 1556 | 1696 |
| cemu | 1466 | 133 | 60 | 625 | 1532 | 1659 |
| srm | 1313 | 121 | 204 | 653 | 1515 | 1638 |
| xenia | 1344 | 107 | 159 | 606 | 1486 | 1610 |
| shadps4 | 1263 | 108 | 135 | 567 | 1387 | 1506 |
| vita3k | 1324 | 117 | 50 | 560 | 1372 | 1491 |
| cloudsync | 645 | 25 | 278 | 339 | 862 | 948 |
| ppsspp | 543 | 83 | 140 | 271 | 709 | 766 |
| ra | 586 | 87 | 93 | 275 | 717 | 766 |
| dolphin | 589 | 90 | 83 | 261 | 709 | 762 |
| mgba | 580 | 48 | 46 | 249 | 629 | 674 |
| xemu | 508 | 74 | 59 | 227 | 595 | 641 |
| melonds | 508 | 70 | 60 | 222 | 593 | 638 |
| primehack | 442 | 68 | 61 | 200 | 527 | 571 |
| supermodel | 432 | 81 | 15 | 175 | 494 | 528 |
| model2 | 426 | 84 | 7 | 171 | 486 | 517 |
| scummvm | 419 | 59 | 37 | 181 | 480 | 515 |
| bigpemu | 415 | 9 | 11 | 169 | 395 | 435 |
| armsx2 | 127 | 145 | 0 | 99 | 245 | 272 |
| flycast | 118 | 14 | 16 | 50 | 140 | 148 |
| rmg | 110 | 26 | 0 | 42 | 130 | 136 |
| mame | 64 | 2 | 15 | 23 | 76 | 81 |
| eden | 73 | 7 | 0 | 38 | 72 | 80 |
| pegasus | 13 | 0 | 12 | 7 | 21 | 25 |
| yuzu | 7 | 0 | 1 | 1 | 7 | 8 |
| ares | 6 | 1 | 0 | 3 | 7 | 7 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
