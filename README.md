# Estadísticas de EmuDeck

Actualizado: 2026-10-19 04:17 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 16587 | 99603 |
| Linux ARM | 180 | 1059 |
| Windows | 4479 | 26137 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2010**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 29 | 212 | 428 | 457 |
| linux-arm | 2 | 31 | 63 | 67 |
| windows | 20 | 59 | 103 | 116 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 428 | 63 | 103 | 594 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 221 | 427 | 460 |
| Con CloudSync | 323 | 618 | 701 |
| % con CloudSync | | | 152% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1203 | 18 | 146 | 701 | 1262 | 1367 |
| duckstation | 1162 | 83 | 50 | 667 | 1197 | 1295 |
| azahar | 1069 | 85 | 140 | 660 | 1191 | 1294 |
| esde | 974 | 74 | 213 | 633 | 1138 | 1261 |
| ryujinx | 1032 | 86 | 139 | 648 | 1166 | 1257 |
| rpcs3 | 1084 | 84 | 50 | 642 | 1129 | 1218 |
| cemu | 1066 | 84 | 37 | 617 | 1104 | 1187 |
| xenia | 970 | 70 | 109 | 599 | 1065 | 1149 |
| srm | 947 | 68 | 132 | 616 | 1076 | 1147 |
| shadps4 | 925 | 69 | 103 | 573 | 1012 | 1097 |
| vita3k | 982 | 74 | 28 | 573 | 998 | 1084 |
| cloudsync | 501 | 17 | 207 | 329 | 640 | 725 |
| dolphin | 452 | 60 | 57 | 272 | 526 | 569 |
| ppsspp | 412 | 56 | 100 | 264 | 522 | 568 |
| ra | 442 | 61 | 56 | 262 | 521 | 559 |
| mgba | 426 | 34 | 32 | 265 | 462 | 492 |
| melonds | 390 | 46 | 40 | 234 | 438 | 476 |
| xemu | 381 | 49 | 39 | 224 | 434 | 469 |
| primehack | 335 | 47 | 39 | 197 | 387 | 421 |
| supermodel | 329 | 55 | 9 | 191 | 367 | 393 |
| model2 | 324 | 58 | 6 | 185 | 361 | 388 |
| scummvm | 321 | 42 | 21 | 180 | 354 | 384 |
| bigpemu | 295 | 3 | 8 | 157 | 278 | 306 |
| armsx2 | 89 | 91 | 0 | 89 | 165 | 180 |
| flycast | 86 | 13 | 10 | 49 | 102 | 109 |
| rmg | 84 | 21 | 0 | 54 | 99 | 105 |
| eden | 59 | 7 | 0 | 50 | 58 | 66 |
| mame | 52 | 2 | 10 | 20 | 58 | 64 |
| pegasus | 9 | 0 | 10 | 13 | 17 | 19 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
