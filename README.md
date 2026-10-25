# Estadísticas de EmuDeck

Actualizado: 2026-10-25 21:37 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 15016 | 94480 |
| Linux ARM | 202 | 1156 |
| Windows | 3877 | 24584 |
| Mac | 0 | 1 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2046**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272, 12219, 13039, 15016]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186, 138, 153, 202]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183, 3270, 3317, 3877]
```

```mermaid
xychart-beta
    title "Arranques Mac"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Arranques"
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 22 | 196 | 595 | 649 |
| linux-arm | 7 | 35 | 96 | 101 |
| windows | 9 | 76 | 159 | 169 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32, 23, 42, 22]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6, 2, 6, 7]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11, 11, 2, 9]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757, 793, 843, 881]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 595 | 96 | 159 | 850 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 216 | 604 | 656 |
| Con CloudSync | 304 | 862 | 964 |
| % con CloudSync | | | 147% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34, 25, 37, 24]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25, 49, 43, 31]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1782 | 22 | 199 | 684 | 1828 | 2003 |
| duckstation | 1704 | 137 | 84 | 662 | 1755 | 1925 |
| azahar | 1563 | 152 | 196 | 659 | 1747 | 1911 |
| ryujinx | 1527 | 147 | 205 | 651 | 1715 | 1879 |
| esde | 1443 | 113 | 314 | 657 | 1690 | 1870 |
| rpcs3 | 1608 | 137 | 82 | 628 | 1656 | 1827 |
| cemu | 1574 | 140 | 65 | 612 | 1624 | 1779 |
| srm | 1424 | 128 | 225 | 665 | 1625 | 1777 |
| xenia | 1452 | 111 | 168 | 600 | 1573 | 1731 |
| shadps4 | 1362 | 115 | 144 | 548 | 1468 | 1621 |
| vita3k | 1421 | 123 | 53 | 544 | 1454 | 1597 |
| cloudsync | 685 | 26 | 289 | 319 | 896 | 1000 |
| ra | 624 | 89 | 98 | 268 | 747 | 811 |
| ppsspp | 575 | 85 | 149 | 266 | 745 | 809 |
| dolphin | 625 | 92 | 86 | 254 | 739 | 803 |
| mgba | 634 | 51 | 48 | 250 | 669 | 733 |
| xemu | 541 | 75 | 64 | 225 | 624 | 680 |
| melonds | 536 | 72 | 63 | 214 | 617 | 671 |
| primehack | 468 | 69 | 67 | 200 | 555 | 604 |
| supermodel | 455 | 83 | 15 | 170 | 512 | 553 |
| scummvm | 443 | 61 | 41 | 173 | 500 | 545 |
| model2 | 448 | 86 | 7 | 163 | 501 | 541 |
| bigpemu | 441 | 10 | 11 | 170 | 422 | 462 |
| armsx2 | 135 | 155 | 0 | 109 | 267 | 290 |
| flycast | 121 | 15 | 17 | 50 | 144 | 153 |
| rmg | 118 | 26 | 0 | 41 | 134 | 144 |
| mame | 67 | 2 | 15 | 23 | 78 | 84 |
| eden | 73 | 9 | 0 | 23 | 72 | 82 |
| pegasus | 15 | 0 | 12 | 7 | 23 | 27 |
| yuzu | 8 | 0 | 2 | 4 | 10 | 10 |
| ares | 7 | 1 | 0 | 3 | 7 | 8 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
