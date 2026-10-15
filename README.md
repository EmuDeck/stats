# Estadísticas de EmuDeck

Actualizado: 2026-10-15 22:13 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux-arm | 2 | 44 | 45 | 51 |
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
| Instalaciones early | 275 | 304 | 349 |
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
| pcsx2 | 894 | 15 | 105 | 778 | 873 | 1014 |
| azahar | 805 | 68 | 99 | 739 | 827 | 972 |
| duckstation | 862 | 66 | 34 | 738 | 825 | 962 |
| esde | 731 | 60 | 153 | 709 | 793 | 944 |
| ryujinx | 765 | 70 | 100 | 704 | 788 | 935 |
| rpcs3 | 805 | 68 | 33 | 698 | 776 | 906 |
| cemu | 809 | 69 | 22 | 695 | 775 | 900 |
| xenia | 731 | 57 | 74 | 668 | 747 | 862 |
| srm | 703 | 50 | 72 | 628 | 704 | 825 |
| shadps4 | 689 | 57 | 63 | 603 | 684 | 809 |
| vita3k | 724 | 58 | 16 | 614 | 682 | 798 |
| cloudsync | 393 | 16 | 151 | 410 | 470 | 560 |
| dolphin | 350 | 49 | 42 | 350 | 384 | 441 |
| ppsspp | 316 | 45 | 73 | 348 | 379 | 434 |
| ra | 348 | 49 | 33 | 346 | 381 | 430 |
| melonds | 303 | 37 | 25 | 286 | 317 | 365 |
| mgba | 320 | 24 | 21 | 278 | 313 | 365 |
| xemu | 296 | 38 | 26 | 288 | 314 | 360 |
| primehack | 264 | 39 | 25 | 260 | 283 | 328 |
| supermodel | 262 | 45 | 8 | 256 | 277 | 315 |
| model2 | 256 | 48 | 4 | 251 | 273 | 308 |
| scummvm | 253 | 34 | 12 | 238 | 260 | 299 |
| bigpemu | 224 | 3 | 6 | 179 | 197 | 233 |
| armsx2 | 73 | 71 | 0 | 112 | 125 | 144 |
| flycast | 73 | 10 | 5 | 69 | 78 | 88 |
| rmg | 67 | 18 | 0 | 65 | 71 | 85 |
| mame | 44 | 2 | 9 | 47 | 49 | 55 |
| eden | 33 | 6 | 0 | 29 | 29 | 39 |
| pegasus | 9 | 0 | 7 | 7 | 8 | 16 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 3 | 0 | 0 | 2 | 2 | 3 |
