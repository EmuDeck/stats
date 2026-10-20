# Estadísticas de EmuDeck

Actualizado: 2026-10-20 10:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12882 | 98491 |
| Linux ARM | 162 | 1078 |
| Windows | 3342 | 25760 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **2032**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181, 13097, 16093, 16587, 12882]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147, 136, 158, 180, 162]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355, 3594, 4200, 4479, 3342]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 22 | 198 | 450 | 484 |
| linux-arm | 6 | 33 | 69 | 75 |
| windows | 15 | 68 | 118 | 130 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23, 27, 33, 29, 22]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5, 8, 3, 2, 6]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8, 3, 11, 20, 15]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489, 527, 574, 625, 668]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 450 | 69 | 118 | 637 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 215 | 460 | 498 |
| Con CloudSync | 345 | 681 | 758 |
| % con CloudSync | | | 152% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27, 25, 32, 39, 33]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24, 28, 54, 60, 63]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 1290 | 19 | 157 | 698 | 1355 | 1466 |
| duckstation | 1250 | 95 | 53 | 668 | 1290 | 1398 |
| azahar | 1142 | 99 | 149 | 658 | 1281 | 1390 |
| esde | 1042 | 85 | 230 | 641 | 1233 | 1357 |
| ryujinx | 1104 | 99 | 148 | 654 | 1254 | 1351 |
| rpcs3 | 1165 | 96 | 53 | 639 | 1211 | 1314 |
| cemu | 1143 | 97 | 40 | 605 | 1187 | 1280 |
| xenia | 1042 | 83 | 121 | 596 | 1153 | 1246 |
| srm | 1013 | 78 | 147 | 622 | 1156 | 1238 |
| shadps4 | 989 | 78 | 113 | 575 | 1086 | 1180 |
| vita3k | 1046 | 84 | 31 | 567 | 1073 | 1161 |
| cloudsync | 536 | 20 | 231 | 350 | 704 | 787 |
| ppsspp | 433 | 64 | 110 | 260 | 560 | 607 |
| ra | 470 | 67 | 65 | 256 | 558 | 602 |
| dolphin | 474 | 67 | 59 | 266 | 560 | 600 |
| mgba | 461 | 36 | 34 | 261 | 494 | 531 |
| melonds | 408 | 52 | 42 | 225 | 465 | 502 |
| xemu | 402 | 56 | 41 | 215 | 463 | 499 |
| primehack | 352 | 51 | 43 | 191 | 413 | 446 |
| supermodel | 345 | 63 | 9 | 181 | 388 | 417 |
| model2 | 341 | 66 | 7 | 180 | 385 | 414 |
| scummvm | 337 | 47 | 23 | 173 | 375 | 407 |
| bigpemu | 320 | 4 | 8 | 170 | 306 | 332 |
| armsx2 | 97 | 103 | 0 | 95 | 183 | 200 |
| flycast | 88 | 14 | 10 | 45 | 105 | 112 |
| rmg | 86 | 22 | 0 | 52 | 104 | 108 |
| eden | 65 | 7 | 0 | 52 | 64 | 72 |
| mame | 54 | 2 | 10 | 22 | 61 | 66 |
| pegasus | 9 | 0 | 10 | 13 | 17 | 19 |
| yuzu | 6 | 0 | 0 | 2 | 6 | 6 |
| ares | 4 | 1 | 0 | 1 | 5 | 5 |
| citron | 4 | 0 | 0 | 3 | 4 | 4 |
