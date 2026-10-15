# Estadísticas de EmuDeck

Actualizado: 2026-10-15 20:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 37 | 282 | 316 | 358 |
| linux-arm | 2 | 44 | 45 | 50 |
| windows | 2 | 56 | 61 | 72 |

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
| Instalaciones early | 275 | 304 | 345 |
| Con CloudSync | 394 | 452 | 534 |
| % con CloudSync | | | 155% |

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
| pcsx2 | 886 | 15 | 103 | 778 | 873 | 1004 |
| azahar | 798 | 67 | 97 | 739 | 827 | 962 |
| duckstation | 855 | 65 | 34 | 738 | 825 | 954 |
| esde | 725 | 60 | 152 | 709 | 793 | 937 |
| ryujinx | 755 | 69 | 99 | 704 | 788 | 923 |
| rpcs3 | 798 | 67 | 33 | 698 | 776 | 898 |
| cemu | 804 | 68 | 22 | 695 | 775 | 894 |
| xenia | 727 | 56 | 72 | 668 | 747 | 855 |
| srm | 697 | 49 | 67 | 628 | 704 | 813 |
| shadps4 | 684 | 57 | 61 | 603 | 684 | 802 |
| vita3k | 717 | 57 | 16 | 614 | 682 | 790 |
| cloudsync | 390 | 16 | 149 | 410 | 470 | 555 |
| dolphin | 349 | 48 | 41 | 350 | 384 | 438 |
| ppsspp | 315 | 44 | 71 | 348 | 379 | 430 |
| ra | 347 | 48 | 33 | 346 | 381 | 428 |
| melonds | 302 | 36 | 25 | 286 | 317 | 363 |
| mgba | 318 | 23 | 21 | 278 | 313 | 362 |
| xemu | 295 | 37 | 26 | 288 | 314 | 358 |
| primehack | 263 | 38 | 25 | 260 | 283 | 326 |
| supermodel | 261 | 44 | 8 | 256 | 277 | 313 |
| model2 | 255 | 47 | 4 | 251 | 273 | 306 |
| scummvm | 252 | 33 | 12 | 238 | 260 | 297 |
| bigpemu | 223 | 3 | 6 | 179 | 197 | 232 |
| armsx2 | 73 | 70 | 0 | 112 | 125 | 143 |
| flycast | 73 | 10 | 5 | 69 | 78 | 88 |
| rmg | 67 | 17 | 0 | 65 | 71 | 84 |
| mame | 44 | 2 | 9 | 47 | 49 | 55 |
| eden | 33 | 6 | 0 | 29 | 29 | 39 |
| pegasus | 9 | 0 | 6 | 7 | 8 | 15 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 2 | 2 | 3 |
