# Estadísticas de EmuDeck

Actualizado: 2026-10-22 23:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12272 | 96577 |
| Linux ARM | 186 | 1104 |
| Windows | 3183 | 25269 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2120**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465, 12272]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135, 186]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116, 3183]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 32 | 192 | 508 | 552 |
| linux-arm | 6 | 36 | 81 | 86 |
| windows | 11 | 76 | 137 | 154 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26, 32]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6, 6]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8, 11]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708, 757]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 508 | 81 | 137 | 726 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 214 | 518 | 565 |
| Con CloudSync | 287 | 739 | 849 |
| % con CloudSync | | | 150% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24, 34]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33, 25]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1484 | 19 | 180 | 658 | 1531 | 1683 |
| duckstation | 1433 | 111 | 70 | 638 | 1463 | 1614 |
| azahar | 1315 | 118 | 173 | 633 | 1460 | 1606 |
| esde | 1202 | 92 | 278 | 605 | 1398 | 1572 |
| ryujinx | 1273 | 115 | 171 | 633 | 1421 | 1559 |
| rpcs3 | 1334 | 110 | 71 | 604 | 1380 | 1515 |
| cemu | 1318 | 113 | 54 | 570 | 1345 | 1485 |
| srm | 1189 | 98 | 180 | 642 | 1346 | 1467 |
| xenia | 1202 | 94 | 143 | 572 | 1319 | 1439 |
| shadps4 | 1130 | 94 | 128 | 548 | 1232 | 1352 |
| vita3k | 1195 | 98 | 46 | 536 | 1218 | 1339 |
| cloudsync | 602 | 24 | 252 | 296 | 766 | 878 |
| ra | 529 | 76 | 89 | 248 | 629 | 694 |
| ppsspp | 487 | 72 | 131 | 248 | 627 | 690 |
| dolphin | 534 | 78 | 75 | 244 | 628 | 687 |
| mgba | 529 | 42 | 41 | 246 | 559 | 612 |
| melonds | 458 | 62 | 54 | 206 | 523 | 574 |
| xemu | 454 | 64 | 53 | 209 | 523 | 571 |
| primehack | 395 | 59 | 56 | 180 | 463 | 510 |
| supermodel | 388 | 74 | 12 | 160 | 437 | 474 |
| model2 | 383 | 77 | 7 | 159 | 432 | 467 |
| scummvm | 378 | 53 | 34 | 163 | 423 | 465 |
| bigpemu | 369 | 5 | 9 | 147 | 344 | 383 |
| armsx2 | 115 | 122 | 0 | 90 | 215 | 237 |
| flycast | 103 | 14 | 12 | 40 | 118 | 129 |
| rmg | 101 | 26 | 0 | 46 | 117 | 127 |
| eden | 72 | 7 | 0 | 41 | 70 | 79 |
| mame | 58 | 2 | 13 | 17 | 66 | 73 |
| pegasus | 11 | 0 | 11 | 11 | 19 | 22 |
| ares | 5 | 1 | 0 | 1 | 5 | 6 |
| yuzu | 6 | 0 | 0 | 0 | 6 | 6 |
| citron | 4 | 0 | 0 | 2 | 4 | 4 |
