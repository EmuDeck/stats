# Estadísticas de EmuDeck

Actualizado: 2026-10-18 23:11 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 16093 | 99141 |
| Linux ARM | 158 | 1074 |
| Windows | 4200 | 26065 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1915**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 33 | 244 | 399 | 448 |
| linux-arm | 3 | 32 | 61 | 65 |
| windows | 11 | 49 | 83 | 110 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 399 | 61 | 83 | 543 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 236 | 388 | 448 |
| Con CloudSync | 327 | 558 | 681 |
| % con CloudSync | | | 152% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1176 | 18 | 138 | 703 | 1144 | 1332 |
| duckstation | 1138 | 80 | 47 | 677 | 1093 | 1265 |
| azahar | 1046 | 82 | 133 | 666 | 1088 | 1261 |
| ryujinx | 1011 | 83 | 134 | 652 | 1064 | 1228 |
| esde | 954 | 71 | 202 | 618 | 1033 | 1227 |
| rpcs3 | 1062 | 81 | 48 | 643 | 1028 | 1191 |
| cemu | 1047 | 81 | 35 | 626 | 1012 | 1163 |
| srm | 928 | 67 | 124 | 595 | 960 | 1119 |
| xenia | 949 | 67 | 103 | 611 | 973 | 1119 |
| shadps4 | 907 | 67 | 98 | 579 | 920 | 1072 |
| vita3k | 956 | 71 | 27 | 578 | 910 | 1054 |
| cloudsync | 491 | 17 | 197 | 333 | 577 | 705 |
| dolphin | 440 | 58 | 55 | 296 | 485 | 553 |
| ppsspp | 403 | 54 | 94 | 292 | 479 | 551 |
| ra | 433 | 59 | 55 | 283 | 479 | 547 |
| mgba | 417 | 34 | 31 | 255 | 419 | 482 |
| melonds | 381 | 44 | 38 | 253 | 403 | 463 |
| xemu | 372 | 47 | 38 | 246 | 399 | 457 |
| primehack | 327 | 45 | 37 | 205 | 355 | 409 |
| supermodel | 323 | 53 | 9 | 212 | 342 | 385 |
| model2 | 318 | 56 | 5 | 205 | 338 | 379 |
| scummvm | 315 | 40 | 20 | 198 | 327 | 375 |
| bigpemu | 285 | 3 | 7 | 151 | 252 | 295 |
| armsx2 | 85 | 88 | 0 | 93 | 158 | 173 |
| flycast | 85 | 13 | 9 | 52 | 94 | 107 |
| rmg | 83 | 20 | 0 | 52 | 93 | 103 |
| eden | 59 | 7 | 0 | 45 | 49 | 66 |
| mame | 51 | 2 | 9 | 23 | 55 | 62 |
| pegasus | 9 | 0 | 10 | 13 | 16 | 19 |
| yuzu | 6 | 0 | 0 | 4 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 4 | 0 | 0 | 3 | 3 | 4 |
