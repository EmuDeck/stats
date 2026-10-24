# Estadísticas de EmuDeck

Actualizado: 2026-10-24 10:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 207 | 573 | 605 |
| linux-arm | 6 | 31 | 89 | 94 |
| windows | 2 | 78 | 150 | 158 |

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
| Instalaciones early | 224 | 580 | 609 |
| Con CloudSync | 327 | 831 | 903 |
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
| pcsx2 | 1620 | 21 | 185 | 690 | 1716 | 1826 |
| duckstation | 1557 | 123 | 78 | 677 | 1654 | 1758 |
| azahar | 1431 | 135 | 182 | 659 | 1642 | 1748 |
| esde | 1310 | 105 | 292 | 643 | 1570 | 1707 |
| ryujinx | 1384 | 133 | 188 | 654 | 1609 | 1705 |
| rpcs3 | 1459 | 122 | 75 | 638 | 1556 | 1656 |
| cemu | 1435 | 129 | 59 | 625 | 1532 | 1623 |
| srm | 1283 | 114 | 192 | 653 | 1515 | 1589 |
| xenia | 1316 | 105 | 153 | 606 | 1486 | 1574 |
| shadps4 | 1237 | 107 | 133 | 567 | 1387 | 1477 |
| vita3k | 1298 | 112 | 49 | 560 | 1372 | 1459 |
| cloudsync | 635 | 25 | 277 | 339 | 862 | 937 |
| ra | 580 | 83 | 92 | 275 | 717 | 755 |
| ppsspp | 536 | 78 | 138 | 271 | 709 | 752 |
| dolphin | 582 | 85 | 82 | 261 | 709 | 749 |
| mgba | 568 | 47 | 45 | 249 | 629 | 660 |
| melonds | 501 | 68 | 59 | 222 | 593 | 628 |
| xemu | 500 | 70 | 58 | 227 | 595 | 628 |
| primehack | 435 | 67 | 59 | 200 | 527 | 561 |
| supermodel | 426 | 81 | 14 | 175 | 494 | 521 |
| model2 | 420 | 84 | 7 | 171 | 486 | 511 |
| scummvm | 413 | 59 | 36 | 181 | 480 | 508 |
| bigpemu | 402 | 8 | 10 | 169 | 395 | 420 |
| armsx2 | 122 | 137 | 0 | 99 | 245 | 259 |
| flycast | 118 | 14 | 16 | 50 | 140 | 148 |
| rmg | 109 | 26 | 0 | 42 | 130 | 135 |
| eden | 73 | 7 | 0 | 38 | 72 | 80 |
| mame | 64 | 2 | 14 | 23 | 76 | 80 |
| pegasus | 12 | 0 | 12 | 7 | 21 | 24 |
| ares | 6 | 1 | 0 | 3 | 7 | 7 |
| yuzu | 7 | 0 | 0 | 1 | 7 | 7 |
| citron | 4 | 0 | 0 | 1 | 4 | 4 |
