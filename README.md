# Estadísticas de EmuDeck

Actualizado: 2026-10-18 02:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 33 | 244 | 399 | 430 |
| linux-arm | 3 | 32 | 61 | 64 |
| windows | 11 | 49 | 83 | 93 |

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
| Instalaciones early | 236 | 388 | 422 |
| Con CloudSync | 327 | 558 | 627 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 1102 | 18 | 121 | 703 | 1144 | 1241 |
| duckstation | 1066 | 79 | 41 | 677 | 1093 | 1186 |
| azahar | 980 | 80 | 120 | 666 | 1088 | 1180 |
| ryujinx | 944 | 81 | 123 | 652 | 1064 | 1148 |
| esde | 894 | 70 | 178 | 618 | 1033 | 1142 |
| rpcs3 | 995 | 81 | 39 | 643 | 1028 | 1115 |
| cemu | 982 | 80 | 28 | 626 | 1012 | 1090 |
| xenia | 892 | 67 | 89 | 611 | 973 | 1048 |
| srm | 862 | 65 | 96 | 595 | 960 | 1023 |
| shadps4 | 851 | 65 | 84 | 579 | 920 | 1000 |
| vita3k | 897 | 69 | 21 | 578 | 910 | 987 |
| cloudsync | 455 | 17 | 176 | 333 | 577 | 648 |
| dolphin | 421 | 57 | 47 | 296 | 485 | 525 |
| ppsspp | 386 | 53 | 84 | 292 | 479 | 523 |
| ra | 415 | 58 | 45 | 283 | 479 | 518 |
| mgba | 389 | 32 | 26 | 255 | 419 | 447 |
| melonds | 364 | 43 | 32 | 253 | 403 | 439 |
| xemu | 356 | 47 | 32 | 246 | 399 | 435 |
| primehack | 313 | 45 | 31 | 205 | 355 | 389 |
| supermodel | 310 | 52 | 8 | 212 | 342 | 370 |
| model2 | 306 | 55 | 5 | 205 | 338 | 366 |
| scummvm | 303 | 40 | 17 | 198 | 327 | 360 |
| bigpemu | 263 | 3 | 6 | 151 | 252 | 272 |
| armsx2 | 81 | 87 | 0 | 93 | 158 | 168 |
| flycast | 81 | 13 | 6 | 52 | 94 | 100 |
| rmg | 78 | 20 | 0 | 52 | 93 | 98 |
| mame | 49 | 2 | 9 | 23 | 55 | 60 |
| eden | 50 | 7 | 0 | 45 | 49 | 57 |
| pegasus | 9 | 0 | 9 | 13 | 16 | 18 |
| yuzu | 6 | 0 | 0 | 4 | 6 | 6 |
| ares | 3 | 1 | 0 | 2 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
