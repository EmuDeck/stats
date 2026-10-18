# Estadísticas de EmuDeck

Actualizado: 2026-10-18 05:38 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 33 | 244 | 399 | 431 |
| linux-arm | 3 | 32 | 61 | 64 |
| windows | 11 | 49 | 83 | 95 |

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
| Instalaciones early | 236 | 388 | 425 |
| Con CloudSync | 327 | 558 | 629 |
| % con CloudSync | | | 148% |

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
| pcsx2 | 1113 | 18 | 123 | 703 | 1144 | 1254 |
| duckstation | 1077 | 79 | 42 | 677 | 1093 | 1198 |
| azahar | 990 | 81 | 124 | 666 | 1088 | 1195 |
| ryujinx | 954 | 82 | 125 | 652 | 1064 | 1161 |
| esde | 903 | 70 | 181 | 618 | 1033 | 1154 |
| rpcs3 | 1005 | 81 | 40 | 643 | 1028 | 1126 |
| cemu | 992 | 80 | 29 | 626 | 1012 | 1101 |
| xenia | 900 | 67 | 91 | 611 | 973 | 1058 |
| srm | 875 | 66 | 100 | 595 | 960 | 1041 |
| shadps4 | 860 | 66 | 86 | 579 | 920 | 1012 |
| vita3k | 905 | 70 | 23 | 578 | 910 | 998 |
| cloudsync | 456 | 17 | 177 | 333 | 577 | 650 |
| dolphin | 422 | 57 | 48 | 296 | 485 | 527 |
| ppsspp | 388 | 53 | 86 | 292 | 479 | 527 |
| ra | 416 | 58 | 47 | 283 | 479 | 521 |
| mgba | 397 | 33 | 26 | 255 | 419 | 456 |
| melonds | 365 | 43 | 33 | 253 | 403 | 441 |
| xemu | 357 | 47 | 33 | 246 | 399 | 437 |
| primehack | 314 | 45 | 33 | 205 | 355 | 392 |
| supermodel | 311 | 52 | 8 | 212 | 342 | 371 |
| model2 | 307 | 55 | 5 | 205 | 338 | 367 |
| scummvm | 304 | 40 | 18 | 198 | 327 | 362 |
| bigpemu | 267 | 3 | 7 | 151 | 252 | 277 |
| armsx2 | 82 | 87 | 0 | 93 | 158 | 169 |
| flycast | 81 | 13 | 6 | 52 | 94 | 100 |
| rmg | 79 | 20 | 0 | 52 | 93 | 99 |
| mame | 49 | 2 | 9 | 23 | 55 | 60 |
| eden | 52 | 7 | 0 | 45 | 49 | 59 |
| pegasus | 9 | 0 | 10 | 13 | 16 | 19 |
| yuzu | 6 | 0 | 0 | 4 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
