# Estadísticas de EmuDeck

Actualizado: 2026-10-21 00:35 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 26 | 197 | 476 | 498 |
| linux-arm | 6 | 32 | 75 | 78 |
| windows | 8 | 67 | 126 | 133 |

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
| Instalaciones early | 204 | 484 | 508 |
| Con CloudSync | 329 | 714 | 778 |
| % con CloudSync | | | 153% |

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
| pcsx2 | 1326 | 19 | 160 | 673 | 1426 | 1505 |
| duckstation | 1283 | 97 | 54 | 641 | 1356 | 1434 |
| azahar | 1176 | 103 | 153 | 634 | 1351 | 1432 |
| esde | 1071 | 87 | 239 | 616 | 1302 | 1397 |
| ryujinx | 1134 | 103 | 152 | 633 | 1318 | 1389 |
| rpcs3 | 1196 | 99 | 54 | 617 | 1277 | 1349 |
| cemu | 1174 | 100 | 42 | 583 | 1249 | 1316 |
| xenia | 1073 | 87 | 126 | 576 | 1221 | 1286 |
| srm | 1041 | 83 | 153 | 602 | 1224 | 1277 |
| shadps4 | 1018 | 82 | 115 | 568 | 1147 | 1215 |
| vita3k | 1080 | 87 | 33 | 553 | 1132 | 1200 |
| cloudsync | 546 | 20 | 241 | 338 | 741 | 807 |
| ppsspp | 446 | 66 | 113 | 252 | 592 | 625 |
| ra | 483 | 69 | 67 | 252 | 588 | 619 |
| dolphin | 486 | 70 | 61 | 250 | 586 | 617 |
| mgba | 473 | 37 | 35 | 243 | 521 | 545 |
| melonds | 421 | 55 | 44 | 217 | 491 | 520 |
| xemu | 415 | 58 | 42 | 213 | 488 | 515 |
| primehack | 363 | 53 | 46 | 191 | 437 | 462 |
| supermodel | 357 | 66 | 9 | 178 | 410 | 432 |
| model2 | 353 | 69 | 7 | 173 | 407 | 429 |
| scummvm | 349 | 49 | 25 | 173 | 398 | 423 |
| bigpemu | 328 | 4 | 8 | 154 | 320 | 340 |
| armsx2 | 97 | 106 | 0 | 87 | 194 | 203 |
| flycast | 92 | 14 | 10 | 37 | 110 | 116 |
| rmg | 89 | 23 | 0 | 42 | 107 | 112 |
| eden | 69 | 7 | 0 | 47 | 68 | 76 |
| mame | 56 | 2 | 10 | 15 | 63 | 68 |
| pegasus | 9 | 0 | 10 | 11 | 17 | 19 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 1 | 5 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
