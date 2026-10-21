# Estadísticas de EmuDeck

Actualizado: 2026-10-21 23:38 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 26 | 197 | 476 | 529 |
| linux-arm | 6 | 32 | 75 | 84 |
| windows | 8 | 67 | 126 | 144 |

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
| Instalaciones early | 204 | 484 | 541 |
| Con CloudSync | 329 | 714 | 803 |
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
| pcsx2 | 1417 | 19 | 168 | 673 | 1426 | 1604 |
| duckstation | 1366 | 108 | 61 | 641 | 1356 | 1535 |
| azahar | 1256 | 115 | 163 | 634 | 1351 | 1534 |
| esde | 1151 | 88 | 250 | 616 | 1302 | 1489 |
| ryujinx | 1213 | 110 | 164 | 633 | 1318 | 1487 |
| rpcs3 | 1278 | 106 | 62 | 617 | 1277 | 1446 |
| cemu | 1250 | 109 | 48 | 583 | 1249 | 1407 |
| srm | 1132 | 96 | 165 | 602 | 1224 | 1393 |
| xenia | 1151 | 92 | 134 | 576 | 1221 | 1377 |
| shadps4 | 1084 | 89 | 122 | 568 | 1147 | 1295 |
| vita3k | 1146 | 96 | 38 | 553 | 1132 | 1280 |
| cloudsync | 564 | 24 | 244 | 338 | 741 | 832 |
| ppsspp | 466 | 71 | 121 | 252 | 592 | 658 |
| dolphin | 512 | 76 | 69 | 250 | 586 | 657 |
| ra | 508 | 75 | 74 | 252 | 588 | 657 |
| mgba | 501 | 42 | 37 | 243 | 521 | 580 |
| melonds | 440 | 61 | 49 | 217 | 491 | 550 |
| xemu | 437 | 63 | 48 | 213 | 488 | 548 |
| primehack | 379 | 58 | 50 | 191 | 437 | 487 |
| supermodel | 374 | 72 | 11 | 178 | 410 | 457 |
| model2 | 370 | 75 | 7 | 173 | 407 | 452 |
| scummvm | 364 | 52 | 30 | 173 | 398 | 446 |
| bigpemu | 349 | 5 | 8 | 154 | 320 | 362 |
| armsx2 | 107 | 117 | 0 | 87 | 194 | 224 |
| flycast | 98 | 14 | 11 | 37 | 110 | 123 |
| rmg | 96 | 25 | 0 | 42 | 107 | 121 |
| eden | 71 | 7 | 0 | 47 | 68 | 78 |
| mame | 56 | 2 | 12 | 15 | 63 | 70 |
| pegasus | 11 | 0 | 10 | 11 | 17 | 21 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 1 | 5 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
