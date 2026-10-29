# Estadísticas de EmuDeck

Actualizado: 2026-10-29 06:18 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 11883 | 92549 |
| Linux ARM | 196 | 1109 |
| Windows | 3272 | 24601 |
| Mac | 2 | 3 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2310**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272, 12219, 13039, 15016, 15683, 12702, 12007, 11883]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186, 138, 153, 202, 129, 144, 147, 196]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183, 3270, 3317, 3877, 4147, 3496, 3222, 3272]
```

```mermaid
xychart-beta
    title "Arranques Mac"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Arranques"
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 28 | 206 | 714 | 745 |
| linux-arm | 13 | 39 | 120 | 124 |
| windows | 7 | 56 | 193 | 209 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32, 23, 42, 22, 38, 33, 20, 28]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6, 2, 6, 7, 4, 1, 6, 13]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11, 11, 2, 9, 3, 12, 12, 7]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757, 793, 843, 881, 926, 972, 1010, 1058]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 714 | 120 | 193 | 1027 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 207 | 725 | 764 |
| Con CloudSync | 326 | 1065 | 1142 |
| % con CloudSync | | | 149% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22", "10-23", "10-24", "10-25", "10-26", "10-27", "10-28"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34, 25, 37, 24, 33, 27, 24, 37]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25, 49, 43, 31, 40, 80, 23, 60]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 2045 | 22 | 243 | 669 | 2200 | 2310 |
| duckstation | 1954 | 167 | 103 | 658 | 2121 | 2224 |
| azahar | 1785 | 184 | 245 | 650 | 2110 | 2214 |
| esde | 1650 | 151 | 381 | 661 | 2059 | 2182 |
| ryujinx | 1743 | 175 | 247 | 645 | 2066 | 2165 |
| rpcs3 | 1844 | 169 | 101 | 639 | 2019 | 2114 |
| cemu | 1797 | 170 | 87 | 620 | 1965 | 2054 |
| srm | 1627 | 151 | 266 | 616 | 1962 | 2044 |
| xenia | 1665 | 135 | 211 | 598 | 1917 | 2011 |
| shadps4 | 1560 | 142 | 190 | 560 | 1792 | 1892 |
| vita3k | 1631 | 148 | 68 | 538 | 1756 | 1847 |
| cloudsync | 788 | 40 | 353 | 336 | 1102 | 1181 |
| ppsspp | 663 | 104 | 189 | 280 | 907 | 956 |
| dolphin | 721 | 120 | 108 | 273 | 901 | 949 |
| ra | 718 | 111 | 115 | 273 | 902 | 944 |
| mgba | 715 | 53 | 57 | 235 | 794 | 825 |
| xemu | 622 | 92 | 81 | 232 | 755 | 795 |
| melonds | 605 | 88 | 77 | 207 | 730 | 770 |
| primehack | 538 | 88 | 80 | 207 | 670 | 706 |
| supermodel | 519 | 100 | 19 | 171 | 608 | 638 |
| scummvm | 503 | 75 | 54 | 174 | 597 | 632 |
| model2 | 511 | 104 | 8 | 160 | 592 | 623 |
| bigpemu | 488 | 10 | 14 | 146 | 490 | 512 |
| armsx2 | 150 | 195 | 0 | 120 | 335 | 345 |
| flycast | 133 | 17 | 19 | 44 | 162 | 169 |
| rmg | 130 | 27 | 0 | 35 | 152 | 157 |
| eden | 82 | 9 | 3 | 16 | 86 | 94 |
| mame | 71 | 2 | 17 | 20 | 86 | 90 |
| pegasus | 19 | 0 | 12 | 9 | 28 | 31 |
| ares | 9 | 1 | 0 | 5 | 10 | 10 |
| yuzu | 8 | 0 | 2 | 4 | 10 | 10 |
| citron | 5 | 0 | 0 | 1 | 5 | 5 |
