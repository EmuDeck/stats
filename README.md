# Estadísticas de EmuDeck

Actualizado: 2026-10-17 00:36 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13097 | 98306 |
| Linux ARM | 136 | 1138 |
| Windows | 3594 | 26063 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1812**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 27 | 246 | 366 | 387 |
| linux-arm | 8 | 38 | 58 | 61 |
| windows | 3 | 50 | 72 | 79 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 366 | 58 | 72 | 496 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 249 | 356 | 379 |
| Con CloudSync | 322 | 504 | 573 |
| % con CloudSync | | | 151% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 972 | 18 | 110 | 710 | 1026 | 1100 |
| azahar | 876 | 78 | 105 | 682 | 983 | 1059 |
| duckstation | 936 | 77 | 37 | 683 | 977 | 1050 |
| ryujinx | 834 | 78 | 110 | 656 | 955 | 1022 |
| esde | 795 | 66 | 158 | 639 | 927 | 1019 |
| rpcs3 | 874 | 76 | 34 | 649 | 918 | 984 |
| cemu | 871 | 76 | 23 | 631 | 907 | 970 |
| xenia | 796 | 63 | 79 | 621 | 880 | 938 |
| srm | 760 | 64 | 87 | 600 | 862 | 911 |
| shadps4 | 751 | 64 | 69 | 580 | 820 | 884 |
| vita3k | 791 | 67 | 17 | 579 | 812 | 875 |
| cloudsync | 418 | 16 | 160 | 331 | 523 | 594 |
| dolphin | 380 | 54 | 43 | 307 | 448 | 477 |
| ra | 377 | 55 | 38 | 295 | 442 | 470 |
| ppsspp | 344 | 51 | 74 | 303 | 438 | 469 |
| mgba | 347 | 32 | 22 | 271 | 380 | 401 |
| melonds | 329 | 41 | 28 | 258 | 371 | 398 |
| xemu | 321 | 44 | 28 | 259 | 368 | 393 |
| primehack | 282 | 43 | 26 | 214 | 327 | 351 |
| supermodel | 281 | 50 | 8 | 222 | 319 | 339 |
| model2 | 277 | 53 | 5 | 216 | 315 | 335 |
| scummvm | 271 | 38 | 13 | 204 | 299 | 322 |
| bigpemu | 235 | 3 | 6 | 167 | 226 | 244 |
| armsx2 | 73 | 82 | 0 | 98 | 146 | 155 |
| flycast | 78 | 12 | 5 | 62 | 90 | 95 |
| rmg | 72 | 20 | 0 | 56 | 88 | 92 |
| mame | 46 | 2 | 9 | 29 | 53 | 57 |
| eden | 37 | 7 | 0 | 32 | 34 | 44 |
| pegasus | 9 | 0 | 7 | 11 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 5 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
