# Estadísticas de EmuDeck

Actualizado: 2026-10-20 21:38 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12882 | 98491 |
| Linux ARM | 162 | 1078 |
| Windows | 3342 | 25760 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2032**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 22 | 198 | 450 | 494 |
| linux-arm | 6 | 33 | 69 | 78 |
| windows | 15 | 68 | 118 | 132 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 450 | 69 | 118 | 637 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 215 | 460 | 504 |
| Con CloudSync | 345 | 681 | 776 |
| % con CloudSync | | | 154% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1313 | 19 | 159 | 698 | 1355 | 1491 |
| duckstation | 1271 | 97 | 53 | 668 | 1290 | 1421 |
| azahar | 1164 | 103 | 151 | 658 | 1281 | 1418 |
| esde | 1060 | 87 | 237 | 641 | 1233 | 1384 |
| ryujinx | 1123 | 103 | 151 | 654 | 1254 | 1377 |
| rpcs3 | 1183 | 99 | 53 | 639 | 1211 | 1335 |
| cemu | 1162 | 100 | 41 | 605 | 1187 | 1303 |
| xenia | 1059 | 87 | 125 | 596 | 1153 | 1271 |
| srm | 1030 | 83 | 153 | 622 | 1156 | 1266 |
| shadps4 | 1006 | 82 | 114 | 575 | 1086 | 1202 |
| vita3k | 1068 | 87 | 32 | 567 | 1073 | 1187 |
| cloudsync | 544 | 20 | 241 | 350 | 704 | 805 |
| ppsspp | 441 | 66 | 112 | 260 | 560 | 619 |
| ra | 478 | 69 | 66 | 256 | 558 | 613 |
| dolphin | 481 | 70 | 60 | 266 | 560 | 611 |
| mgba | 467 | 37 | 34 | 261 | 494 | 538 |
| melonds | 416 | 55 | 43 | 225 | 465 | 514 |
| xemu | 410 | 58 | 41 | 215 | 463 | 509 |
| primehack | 359 | 53 | 45 | 191 | 413 | 457 |
| supermodel | 352 | 66 | 9 | 181 | 388 | 427 |
| model2 | 348 | 69 | 7 | 180 | 385 | 424 |
| scummvm | 344 | 49 | 24 | 173 | 375 | 417 |
| bigpemu | 324 | 4 | 8 | 170 | 306 | 336 |
| armsx2 | 97 | 106 | 0 | 95 | 183 | 203 |
| flycast | 89 | 14 | 10 | 45 | 105 | 113 |
| rmg | 86 | 23 | 0 | 52 | 104 | 109 |
| eden | 69 | 7 | 0 | 52 | 64 | 76 |
| mame | 54 | 2 | 10 | 22 | 61 | 66 |
| pegasus | 9 | 0 | 10 | 13 | 17 | 19 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 1 | 5 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
