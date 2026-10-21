# Estadísticas de EmuDeck

Actualizado: 2026-10-21 15:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12465 | 97788 |
| Linux ARM | 135 | 1087 |
| Windows | 3116 | 25420 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2069**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882, 12465]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162, 135]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342, 3116]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 26 | 197 | 476 | 519 |
| linux-arm | 6 | 32 | 75 | 84 |
| windows | 8 | 67 | 126 | 141 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22, 26]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6, 6]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15, 8]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668, 708]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 476 | 75 | 126 | 677 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 204 | 484 | 537 |
| Con CloudSync | 329 | 714 | 796 |
| % con CloudSync | | | 148% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33, 24]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63, 33]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1369 | 19 | 166 | 673 | 1426 | 1554 |
| azahar | 1215 | 114 | 161 | 634 | 1351 | 1490 |
| duckstation | 1322 | 107 | 58 | 641 | 1356 | 1487 |
| esde | 1109 | 88 | 247 | 616 | 1302 | 1444 |
| ryujinx | 1171 | 110 | 158 | 633 | 1318 | 1439 |
| rpcs3 | 1235 | 106 | 60 | 617 | 1277 | 1401 |
| cemu | 1210 | 108 | 46 | 583 | 1249 | 1364 |
| srm | 1087 | 94 | 160 | 602 | 1224 | 1341 |
| xenia | 1111 | 92 | 132 | 576 | 1221 | 1335 |
| shadps4 | 1052 | 88 | 120 | 568 | 1147 | 1260 |
| vita3k | 1113 | 95 | 36 | 553 | 1132 | 1244 |
| cloudsync | 558 | 23 | 244 | 338 | 741 | 825 |
| ppsspp | 459 | 71 | 119 | 252 | 592 | 649 |
| ra | 500 | 75 | 71 | 252 | 588 | 646 |
| dolphin | 502 | 76 | 66 | 250 | 586 | 644 |
| mgba | 489 | 41 | 36 | 243 | 521 | 566 |
| melonds | 434 | 61 | 47 | 217 | 491 | 542 |
| xemu | 428 | 63 | 45 | 213 | 488 | 536 |
| primehack | 375 | 58 | 49 | 191 | 437 | 482 |
| supermodel | 371 | 72 | 9 | 178 | 410 | 452 |
| model2 | 367 | 75 | 7 | 173 | 407 | 449 |
| scummvm | 361 | 52 | 29 | 173 | 398 | 442 |
| bigpemu | 341 | 5 | 8 | 154 | 320 | 354 |
| armsx2 | 103 | 116 | 0 | 87 | 194 | 219 |
| flycast | 94 | 14 | 11 | 37 | 110 | 119 |
| rmg | 90 | 25 | 0 | 42 | 107 | 115 |
| eden | 70 | 7 | 0 | 47 | 68 | 77 |
| mame | 56 | 2 | 12 | 15 | 63 | 70 |
| pegasus | 10 | 0 | 10 | 11 | 17 | 20 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 1 | 5 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
