# Estadísticas de EmuDeck

Actualizado: 2026-10-15 03:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 37 | 282 | 316 | 340 |
| linux-arm | 2 | 44 | 45 | 49 |
| windows | 2 | 56 | 61 | 69 |

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
| Instalaciones early | 275 | 304 | 332 |
| Con CloudSync | 394 | 452 | 522 |
| % con CloudSync | | | 157% |

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
| pcsx2 | 849 | 15 | 98 | 778 | 873 | 962 |
| azahar | 759 | 66 | 92 | 739 | 827 | 917 |
| duckstation | 820 | 64 | 32 | 738 | 825 | 916 |
| esde | 698 | 59 | 143 | 709 | 793 | 900 |
| ryujinx | 717 | 66 | 94 | 704 | 788 | 877 |
| rpcs3 | 760 | 64 | 33 | 698 | 776 | 857 |
| cemu | 766 | 65 | 22 | 695 | 775 | 853 |
| xenia | 695 | 55 | 68 | 668 | 747 | 818 |
| srm | 654 | 48 | 63 | 628 | 704 | 765 |
| shadps4 | 648 | 56 | 57 | 603 | 684 | 761 |
| vita3k | 686 | 56 | 14 | 614 | 682 | 756 |
| cloudsync | 382 | 16 | 144 | 410 | 470 | 542 |
| dolphin | 334 | 46 | 39 | 350 | 384 | 419 |
| ra | 335 | 47 | 32 | 346 | 381 | 414 |
| ppsspp | 301 | 43 | 68 | 348 | 379 | 412 |
| melonds | 289 | 35 | 24 | 286 | 317 | 348 |
| xemu | 283 | 36 | 25 | 288 | 314 | 344 |
| mgba | 297 | 23 | 21 | 278 | 313 | 341 |
| primehack | 248 | 37 | 24 | 260 | 283 | 309 |
| supermodel | 249 | 43 | 7 | 256 | 277 | 299 |
| model2 | 245 | 46 | 4 | 251 | 273 | 295 |
| scummvm | 241 | 32 | 12 | 238 | 260 | 285 |
| bigpemu | 209 | 3 | 5 | 179 | 197 | 217 |
| armsx2 | 69 | 67 | 0 | 112 | 125 | 136 |
| flycast | 68 | 10 | 5 | 69 | 78 | 83 |
| rmg | 60 | 17 | 0 | 65 | 71 | 77 |
| mame | 42 | 2 | 9 | 47 | 49 | 53 |
| eden | 31 | 6 | 0 | 29 | 29 | 37 |
| pegasus | 7 | 0 | 5 | 7 | 8 | 12 |
| yuzu | 6 | 0 | 0 | 6 | 6 | 6 |
| ares | 3 | 1 | 0 | 3 | 4 | 4 |
| citron | 2 | 0 | 0 | 2 | 2 | 2 |
