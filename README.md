# Estadísticas de EmuDeck

Actualizado: 2026-10-15 00:35 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 37 | 282 | 316 | 337 |
| linux-arm | 2 | 44 | 45 | 48 |
| windows | 2 | 56 | 61 | 68 |

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
| Instalaciones early | 275 | 304 | 327 |
| Con CloudSync | 394 | 452 | 519 |
| % con CloudSync | | | 159% |

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
| pcsx2 | 837 | 15 | 97 | 778 | 873 | 949 |
| azahar | 749 | 64 | 91 | 739 | 827 | 904 |
| duckstation | 808 | 62 | 31 | 738 | 825 | 901 |
| esde | 690 | 57 | 140 | 709 | 793 | 887 |
| ryujinx | 704 | 64 | 90 | 704 | 788 | 858 |
| rpcs3 | 751 | 62 | 32 | 698 | 776 | 845 |
| cemu | 756 | 62 | 22 | 695 | 775 | 840 |
| xenia | 686 | 54 | 68 | 668 | 747 | 808 |
| srm | 647 | 47 | 60 | 628 | 704 | 754 |
| shadps4 | 640 | 56 | 54 | 603 | 684 | 750 |
| vita3k | 679 | 54 | 14 | 614 | 682 | 747 |
| cloudsync | 380 | 16 | 143 | 410 | 470 | 539 |
| dolphin | 330 | 45 | 38 | 350 | 384 | 413 |
| ppsspp | 300 | 42 | 68 | 348 | 379 | 410 |
| ra | 333 | 45 | 31 | 346 | 381 | 409 |
| melonds | 286 | 34 | 24 | 286 | 317 | 344 |
| xemu | 280 | 35 | 24 | 288 | 314 | 339 |
| mgba | 291 | 23 | 21 | 278 | 313 | 335 |
| primehack | 247 | 36 | 24 | 260 | 283 | 307 |
| supermodel | 248 | 42 | 7 | 256 | 277 | 297 |
| model2 | 244 | 45 | 4 | 251 | 273 | 293 |
| scummvm | 240 | 31 | 12 | 238 | 260 | 283 |
| bigpemu | 207 | 3 | 5 | 179 | 197 | 215 |
| armsx2 | 69 | 65 | 0 | 112 | 125 | 134 |
| flycast | 68 | 10 | 5 | 69 | 78 | 83 |
| rmg | 58 | 17 | 0 | 65 | 71 | 75 |
| mame | 42 | 2 | 9 | 47 | 49 | 53 |
| eden | 31 | 6 | 0 | 29 | 29 | 37 |
| pegasus | 6 | 0 | 4 | 7 | 8 | 10 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 2 | 0 | 0 | 2 | 2 | 2 |
