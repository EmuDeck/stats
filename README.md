# Estadísticas de EmuDeck

Actualizado: 2026-10-17 20:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 246 | 366 | 411 |
| linux-arm | 8 | 38 | 58 | 64 |
| windows | 3 | 50 | 72 | 87 |

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
| Instalaciones early | 249 | 356 | 403 |
| Con CloudSync | 322 | 504 | 616 |
| % con CloudSync | | | 153% |

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
| pcsx2 | 1055 | 18 | 117 | 710 | 1026 | 1190 |
| azahar | 948 | 80 | 114 | 682 | 983 | 1142 |
| duckstation | 1019 | 79 | 40 | 683 | 977 | 1138 |
| ryujinx | 904 | 81 | 119 | 656 | 955 | 1104 |
| esde | 858 | 70 | 172 | 639 | 927 | 1100 |
| rpcs3 | 950 | 81 | 38 | 649 | 918 | 1069 |
| cemu | 940 | 80 | 27 | 631 | 907 | 1047 |
| xenia | 854 | 67 | 85 | 621 | 880 | 1006 |
| srm | 830 | 65 | 91 | 600 | 862 | 986 |
| shadps4 | 814 | 65 | 74 | 580 | 820 | 953 |
| vita3k | 859 | 69 | 20 | 579 | 812 | 948 |
| cloudsync | 446 | 17 | 174 | 331 | 523 | 637 |
| dolphin | 401 | 57 | 46 | 307 | 448 | 504 |
| ppsspp | 365 | 53 | 80 | 303 | 438 | 498 |
| ra | 395 | 57 | 43 | 295 | 442 | 495 |
| mgba | 375 | 32 | 24 | 271 | 380 | 431 |
| melonds | 348 | 43 | 31 | 258 | 371 | 422 |
| xemu | 337 | 47 | 31 | 259 | 368 | 415 |
| primehack | 298 | 45 | 30 | 214 | 327 | 373 |
| supermodel | 295 | 52 | 8 | 222 | 319 | 355 |
| model2 | 291 | 55 | 5 | 216 | 315 | 351 |
| scummvm | 286 | 40 | 16 | 204 | 299 | 342 |
| bigpemu | 255 | 3 | 6 | 167 | 226 | 264 |
| armsx2 | 79 | 87 | 0 | 98 | 146 | 166 |
| flycast | 79 | 13 | 6 | 62 | 90 | 98 |
| rmg | 76 | 20 | 0 | 56 | 88 | 96 |
| mame | 47 | 2 | 9 | 29 | 53 | 58 |
| eden | 50 | 7 | 0 | 32 | 34 | 57 |
| pegasus | 9 | 0 | 9 | 11 | 14 | 18 |
| yuzu | 6 | 0 | 0 | 5 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
