# Estadísticas de EmuDeck

Actualizado: 2026-10-13 14:46 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13994 | 94860 |
| Linux ARM | 143 | 1309 |
| Windows | 3719 | 25538 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1416**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 36 | 252 | 252 | 289 |
| linux-arm | 4 | 36 | 36 | 42 |
| windows | 6 | 50 | 50 | 57 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 252 | 36 | 50 | 338 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 245 | 245 | 283 |
| Con CloudSync | 336 | 336 | 419 |
| % con CloudSync | | | 148% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39]
    line [58, 69, 55, 49, 64, 41]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 687 | 12 | 82 | 657 | 657 | 781 |
| duckstation | 670 | 49 | 26 | 622 | 622 | 745 |
| azahar | 617 | 51 | 75 | 623 | 623 | 743 |
| esde | 566 | 46 | 123 | 592 | 592 | 735 |
| ryujinx | 581 | 52 | 78 | 600 | 600 | 711 |
| cemu | 625 | 50 | 18 | 582 | 582 | 693 |
| rpcs3 | 611 | 49 | 28 | 572 | 572 | 688 |
| xenia | 562 | 44 | 54 | 557 | 557 | 660 |
| srm | 539 | 39 | 48 | 534 | 534 | 626 |
| shadps4 | 519 | 49 | 44 | 511 | 511 | 612 |
| vita3k | 554 | 44 | 13 | 506 | 506 | 611 |
| cloudsync | 308 | 13 | 118 | 354 | 354 | 439 |
| dolphin | 281 | 39 | 29 | 294 | 294 | 349 |
| ppsspp | 256 | 36 | 56 | 300 | 300 | 348 |
| ra | 283 | 39 | 26 | 302 | 302 | 348 |
| xemu | 237 | 29 | 22 | 248 | 248 | 288 |
| mgba | 245 | 22 | 20 | 233 | 233 | 287 |
| melonds | 237 | 28 | 18 | 240 | 240 | 283 |
| primehack | 204 | 30 | 21 | 222 | 222 | 255 |
| model2 | 200 | 39 | 3 | 205 | 205 | 242 |
| supermodel | 199 | 36 | 5 | 207 | 207 | 240 |
| scummvm | 199 | 26 | 12 | 202 | 202 | 237 |
| bigpemu | 169 | 3 | 2 | 136 | 136 | 174 |
| armsx2 | 54 | 52 | 0 | 88 | 88 | 106 |
| flycast | 63 | 9 | 5 | 60 | 60 | 77 |
| rmg | 52 | 16 | 0 | 52 | 52 | 68 |
| mame | 41 | 2 | 9 | 39 | 39 | 52 |
| eden | 24 | 3 | 0 | 12 | 12 | 27 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
