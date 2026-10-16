# Estadísticas de EmuDeck

Actualizado: 2026-10-16 09:41 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13181 | 98292 |
| Linux ARM | 147 | 1179 |
| Windows | 3355 | 25977 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1731**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483, 13181]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169, 147]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334, 3355]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 23 | 263 | 339 | 371 |
| linux-arm | 5 | 38 | 50 | 54 |
| windows | 8 | 53 | 69 | 78 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37, 23]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2, 5]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2, 8]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453, 489]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 339 | 50 | 69 | 458 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 263 | 331 | 364 |
| Con CloudSync | 349 | 476 | 549 |
| % con CloudSync | | | 151% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14", "10-15"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24, 27]
    line [58, 69, 55, 49, 64, 41, 49, 67, 24]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 928 | 16 | 109 | 729 | 948 | 1053 |
| azahar | 831 | 73 | 103 | 706 | 905 | 1007 |
| duckstation | 895 | 71 | 37 | 702 | 899 | 1003 |
| esde | 759 | 63 | 156 | 671 | 860 | 978 |
| ryujinx | 792 | 74 | 105 | 684 | 877 | 971 |
| rpcs3 | 835 | 72 | 34 | 670 | 847 | 941 |
| cemu | 834 | 73 | 23 | 669 | 845 | 930 |
| xenia | 759 | 60 | 79 | 641 | 811 | 898 |
| srm | 725 | 53 | 79 | 608 | 786 | 857 |
| shadps4 | 712 | 60 | 67 | 588 | 751 | 839 |
| vita3k | 751 | 62 | 17 | 593 | 745 | 830 |
| cloudsync | 400 | 16 | 154 | 364 | 495 | 570 |
| dolphin | 363 | 53 | 43 | 325 | 415 | 459 |
| ppsspp | 328 | 48 | 74 | 322 | 406 | 450 |
| ra | 359 | 53 | 37 | 312 | 407 | 449 |
| mgba | 334 | 31 | 21 | 273 | 351 | 386 |
| melonds | 314 | 40 | 26 | 268 | 341 | 380 |
| xemu | 308 | 41 | 27 | 269 | 338 | 376 |
| primehack | 273 | 42 | 26 | 240 | 307 | 341 |
| supermodel | 272 | 48 | 8 | 241 | 298 | 328 |
| model2 | 266 | 51 | 4 | 231 | 291 | 321 |
| scummvm | 263 | 37 | 13 | 225 | 279 | 313 |
| bigpemu | 230 | 3 | 6 | 180 | 218 | 239 |
| armsx2 | 73 | 77 | 0 | 109 | 138 | 150 |
| flycast | 75 | 12 | 5 | 62 | 84 | 92 |
| rmg | 70 | 20 | 0 | 60 | 82 | 90 |
| mame | 46 | 2 | 9 | 34 | 51 | 57 |
| eden | 33 | 7 | 0 | 31 | 31 | 40 |
| pegasus | 9 | 0 | 7 | 13 | 14 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 3 | 3 | 3 |
