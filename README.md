# Estadísticas de EmuDeck

Actualizado: 2026-10-15 23:10 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13483 | 97678 |
| Linux ARM | 169 | 1222 |
| Windows | 3334 | 25880 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1663**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168, 13483]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126, 169]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456, 3334]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 37 | 282 | 316 | 359 |
| linux-arm | 2 | 44 | 45 | 53 |
| windows | 2 | 56 | 61 | 74 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27, 37]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7, 2]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9, 2]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412, 453]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 316 | 45 | 61 | 422 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 275 | 304 | 351 |
| Con CloudSync | 394 | 452 | 539 |
| % con CloudSync | | | 154% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13", "10-14"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35, 24]
    line [58, 69, 55, 49, 64, 41, 49, 67]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 897 | 15 | 105 | 778 | 873 | 1017 |
| azahar | 807 | 70 | 99 | 739 | 827 | 976 |
| duckstation | 865 | 68 | 34 | 738 | 825 | 967 |
| esde | 734 | 61 | 153 | 709 | 793 | 948 |
| ryujinx | 767 | 72 | 101 | 704 | 788 | 940 |
| rpcs3 | 807 | 70 | 33 | 698 | 776 | 910 |
| cemu | 811 | 71 | 22 | 695 | 775 | 904 |
| xenia | 734 | 59 | 74 | 668 | 747 | 867 |
| srm | 706 | 51 | 72 | 628 | 704 | 829 |
| shadps4 | 691 | 58 | 63 | 603 | 684 | 812 |
| vita3k | 727 | 60 | 16 | 614 | 682 | 803 |
| cloudsync | 393 | 16 | 151 | 410 | 470 | 560 |
| dolphin | 350 | 51 | 42 | 350 | 384 | 443 |
| ppsspp | 316 | 47 | 73 | 348 | 379 | 436 |
| ra | 348 | 51 | 33 | 346 | 381 | 432 |
| mgba | 323 | 25 | 21 | 278 | 313 | 369 |
| melonds | 303 | 39 | 25 | 286 | 317 | 367 |
| xemu | 296 | 40 | 26 | 288 | 314 | 362 |
| primehack | 264 | 41 | 25 | 260 | 283 | 330 |
| supermodel | 262 | 47 | 8 | 256 | 277 | 317 |
| model2 | 256 | 50 | 4 | 251 | 273 | 310 |
| scummvm | 253 | 36 | 12 | 238 | 260 | 301 |
| bigpemu | 226 | 3 | 6 | 179 | 197 | 235 |
| armsx2 | 73 | 73 | 0 | 112 | 125 | 146 |
| flycast | 73 | 11 | 5 | 69 | 78 | 89 |
| rmg | 67 | 19 | 0 | 65 | 71 | 86 |
| mame | 44 | 2 | 9 | 47 | 49 | 55 |
| eden | 33 | 6 | 0 | 29 | 29 | 39 |
| pegasus | 9 | 0 | 7 | 7 | 8 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 2 | 2 | 3 |
