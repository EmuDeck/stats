# Estadísticas de EmuDeck

Actualizado: 2026-10-17 01:21 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 246 | 366 | 388 |
| linux-arm | 8 | 38 | 58 | 61 |
| windows | 3 | 50 | 72 | 80 |

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
| Instalaciones early | 249 | 356 | 381 |
| Con CloudSync | 322 | 504 | 573 |
| % con CloudSync | | | 150% |

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
| pcsx2 | 976 | 18 | 111 | 710 | 1026 | 1105 |
| azahar | 879 | 78 | 106 | 682 | 983 | 1063 |
| duckstation | 940 | 77 | 38 | 683 | 977 | 1055 |
| ryujinx | 837 | 78 | 111 | 656 | 955 | 1026 |
| esde | 799 | 66 | 159 | 639 | 927 | 1024 |
| rpcs3 | 876 | 76 | 35 | 649 | 918 | 987 |
| cemu | 875 | 76 | 25 | 631 | 907 | 976 |
| xenia | 798 | 63 | 80 | 621 | 880 | 941 |
| srm | 763 | 64 | 87 | 600 | 862 | 914 |
| shadps4 | 753 | 64 | 70 | 580 | 820 | 887 |
| vita3k | 794 | 67 | 18 | 579 | 812 | 879 |
| cloudsync | 418 | 16 | 160 | 331 | 523 | 594 |
| dolphin | 381 | 54 | 44 | 307 | 448 | 479 |
| ra | 377 | 55 | 39 | 295 | 442 | 471 |
| ppsspp | 344 | 51 | 75 | 303 | 438 | 470 |
| mgba | 347 | 32 | 23 | 271 | 380 | 402 |
| melonds | 329 | 41 | 29 | 258 | 371 | 399 |
| xemu | 321 | 44 | 29 | 259 | 368 | 394 |
| primehack | 282 | 43 | 27 | 214 | 327 | 352 |
| supermodel | 281 | 50 | 8 | 222 | 319 | 339 |
| model2 | 277 | 53 | 5 | 216 | 315 | 335 |
| scummvm | 271 | 38 | 14 | 204 | 299 | 323 |
| bigpemu | 235 | 3 | 6 | 167 | 226 | 244 |
| armsx2 | 73 | 82 | 0 | 98 | 146 | 155 |
| flycast | 78 | 12 | 5 | 62 | 90 | 95 |
| rmg | 73 | 20 | 0 | 56 | 88 | 93 |
| mame | 46 | 2 | 9 | 29 | 53 | 57 |
| eden | 37 | 7 | 0 | 32 | 34 | 44 |
| pegasus | 9 | 0 | 7 | 11 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 5 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
