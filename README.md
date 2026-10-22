# Estadísticas de EmuDeck

Actualizado: 2026-10-22 09:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 32 | 192 | 508 | 535 |
| linux-arm | 6 | 36 | 81 | 84 |
| windows | 11 | 76 | 137 | 152 |

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
| Instalaciones early | 214 | 518 | 550 |
| Con CloudSync | 287 | 739 | 812 |
| % con CloudSync | | | 148% |

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
| pcsx2 | 1439 | 19 | 178 | 658 | 1531 | 1636 |
| azahar | 1277 | 116 | 171 | 633 | 1460 | 1564 |
| duckstation | 1387 | 109 | 68 | 638 | 1463 | 1564 |
| esde | 1174 | 89 | 273 | 605 | 1398 | 1536 |
| ryujinx | 1235 | 111 | 168 | 633 | 1421 | 1514 |
| rpcs3 | 1299 | 106 | 67 | 604 | 1380 | 1472 |
| cemu | 1276 | 110 | 52 | 570 | 1345 | 1438 |
| srm | 1150 | 96 | 174 | 642 | 1346 | 1420 |
| xenia | 1168 | 92 | 141 | 572 | 1319 | 1401 |
| shadps4 | 1100 | 90 | 127 | 548 | 1232 | 1317 |
| vita3k | 1166 | 96 | 43 | 536 | 1218 | 1305 |
| cloudsync | 572 | 24 | 245 | 296 | 766 | 841 |
| ppsspp | 472 | 71 | 129 | 248 | 627 | 672 |
| ra | 514 | 75 | 80 | 248 | 629 | 669 |
| dolphin | 518 | 76 | 74 | 244 | 628 | 668 |
| mgba | 510 | 42 | 40 | 246 | 559 | 592 |
| melonds | 445 | 61 | 53 | 206 | 523 | 559 |
| xemu | 443 | 63 | 52 | 209 | 523 | 558 |
| primehack | 383 | 58 | 55 | 180 | 463 | 496 |
| supermodel | 378 | 72 | 11 | 160 | 437 | 461 |
| model2 | 373 | 75 | 7 | 159 | 432 | 455 |
| scummvm | 369 | 52 | 34 | 163 | 423 | 455 |
| bigpemu | 356 | 5 | 8 | 147 | 344 | 369 |
| armsx2 | 111 | 118 | 0 | 90 | 215 | 229 |
| flycast | 99 | 14 | 11 | 40 | 118 | 124 |
| rmg | 97 | 25 | 0 | 46 | 117 | 122 |
| eden | 71 | 7 | 0 | 41 | 70 | 78 |
| mame | 57 | 2 | 13 | 17 | 66 | 72 |
| pegasus | 11 | 0 | 11 | 11 | 19 | 22 |
| ares | 5 | 1 | 0 | 1 | 5 | 6 |
| yuzu | 6 | 0 | 0 | 0 | 6 | 6 |
| citron | 4 | 0 | 0 | 2 | 4 | 4 |
