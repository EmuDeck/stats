# Estadísticas de EmuDeck

Actualizado: 2026-10-26 03:20 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 15683 | 93576 |
| Linux ARM | 129 | 1105 |
| Windows | 4147 | 24252 |
| Mac | 0 | 1 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2055**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272, 12219, 13039, 15016, 15683]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186, 138, 153, 202, 129]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183, 3270, 3317, 3877, 4147]
```

```mermaid
xychart-beta
    title "Arranques Mac"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Arranques"
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 38 | 205 | 633 | 659 |
| linux-arm | 4 | 37 | 100 | 103 |
| windows | 3 | 59 | 162 | 172 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32, 23, 42, 22, 38]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6, 2, 6, 7, 4]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11, 11, 2, 9, 3]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757, 793, 843, 881, 926]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 633 | 100 | 162 | 895 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 210 | 637 | 667 |
| Con CloudSync | 284 | 902 | 972 |
| % con CloudSync | | | 146% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34, 25, 37, 24, 33]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25, 49, 43, 31, 40]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1813 | 22 | 204 | 682 | 1944 | 2039 |
| duckstation | 1732 | 140 | 86 | 671 | 1868 | 1958 |
| azahar | 1589 | 155 | 200 | 662 | 1853 | 1944 |
| ryujinx | 1550 | 149 | 212 | 662 | 1828 | 1911 |
| esde | 1466 | 117 | 323 | 652 | 1790 | 1906 |
| rpcs3 | 1634 | 140 | 84 | 644 | 1773 | 1858 |
| cemu | 1597 | 143 | 68 | 624 | 1728 | 1808 |
| srm | 1441 | 132 | 228 | 668 | 1744 | 1801 |
| xenia | 1477 | 114 | 172 | 620 | 1685 | 1763 |
| shadps4 | 1387 | 117 | 147 | 556 | 1568 | 1651 |
| vita3k | 1445 | 126 | 55 | 549 | 1547 | 1626 |
| cloudsync | 690 | 28 | 290 | 296 | 936 | 1008 |
| ra | 635 | 92 | 100 | 269 | 790 | 827 |
| ppsspp | 584 | 87 | 152 | 263 | 785 | 823 |
| dolphin | 635 | 94 | 88 | 255 | 781 | 817 |
| mgba | 642 | 51 | 48 | 253 | 715 | 741 |
| xemu | 550 | 77 | 66 | 227 | 661 | 693 |
| melonds | 542 | 74 | 65 | 211 | 649 | 681 |
| primehack | 475 | 71 | 69 | 199 | 586 | 615 |
| supermodel | 462 | 85 | 15 | 171 | 538 | 562 |
| scummvm | 449 | 63 | 43 | 173 | 527 | 555 |
| model2 | 454 | 88 | 7 | 165 | 526 | 549 |
| bigpemu | 444 | 10 | 11 | 166 | 444 | 465 |
| armsx2 | 137 | 159 | 0 | 118 | 283 | 296 |
| flycast | 122 | 16 | 18 | 47 | 149 | 156 |
| rmg | 120 | 27 | 0 | 43 | 142 | 147 |
| eden | 81 | 9 | 0 | 16 | 74 | 90 |
| mame | 67 | 2 | 15 | 22 | 80 | 84 |
| pegasus | 15 | 0 | 12 | 8 | 25 | 27 |
| yuzu | 8 | 0 | 2 | 4 | 10 | 10 |
| ares | 7 | 1 | 0 | 4 | 8 | 8 |
| citron | 4 | 0 | 0 | 0 | 4 | 4 |
