# Estadísticas de EmuDeck

Actualizado: 2026-10-19 17:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 29 | 212 | 428 | 466 |
| linux-arm | 2 | 31 | 63 | 70 |
| windows | 20 | 59 | 103 | 122 |

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
| Instalaciones early | 221 | 427 | 474 |
| Con CloudSync | 323 | 618 | 733 |
| % con CloudSync | | | 155% |

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
| pcsx2 | 1234 | 19 | 149 | 701 | 1262 | 1402 |
| duckstation | 1194 | 87 | 52 | 667 | 1197 | 1333 |
| azahar | 1095 | 90 | 141 | 660 | 1191 | 1326 |
| esde | 996 | 77 | 223 | 633 | 1138 | 1296 |
| ryujinx | 1055 | 91 | 141 | 648 | 1166 | 1287 |
| rpcs3 | 1110 | 89 | 51 | 642 | 1129 | 1250 |
| cemu | 1093 | 90 | 39 | 617 | 1104 | 1222 |
| srm | 974 | 72 | 135 | 616 | 1076 | 1181 |
| xenia | 993 | 75 | 112 | 599 | 1065 | 1180 |
| shadps4 | 946 | 72 | 105 | 573 | 1012 | 1123 |
| vita3k | 1003 | 77 | 30 | 573 | 998 | 1110 |
| cloudsync | 518 | 18 | 221 | 329 | 640 | 757 |
| dolphin | 461 | 63 | 58 | 272 | 526 | 582 |
| ppsspp | 420 | 59 | 102 | 264 | 522 | 581 |
| ra | 451 | 62 | 58 | 262 | 521 | 571 |
| mgba | 436 | 35 | 33 | 265 | 462 | 504 |
| melonds | 396 | 49 | 41 | 234 | 438 | 486 |
| xemu | 389 | 52 | 40 | 224 | 434 | 481 |
| primehack | 341 | 48 | 40 | 197 | 387 | 429 |
| supermodel | 334 | 58 | 9 | 191 | 367 | 401 |
| model2 | 330 | 61 | 7 | 185 | 361 | 398 |
| scummvm | 326 | 43 | 22 | 180 | 354 | 391 |
| bigpemu | 302 | 4 | 8 | 157 | 278 | 314 |
| armsx2 | 92 | 95 | 0 | 89 | 165 | 187 |
| flycast | 87 | 13 | 10 | 49 | 102 | 110 |
| rmg | 85 | 22 | 0 | 54 | 99 | 107 |
| eden | 65 | 7 | 0 | 50 | 58 | 72 |
| mame | 53 | 2 | 10 | 20 | 58 | 65 |
| pegasus | 9 | 0 | 10 | 13 | 17 | 19 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 2 | 4 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
