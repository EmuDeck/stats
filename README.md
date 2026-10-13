# Estadísticas de EmuDeck

Actualizado: 2026-10-13 17:13 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 292 |
| linux-arm | 4 | 36 | 36 | 46 |
| windows | 6 | 50 | 50 | 62 |

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
| Instalaciones early | 245 | 245 | 293 |
| Con CloudSync | 336 | 336 | 433 |
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
| pcsx2 | 699 | 12 | 87 | 657 | 657 | 798 |
| azahar | 628 | 56 | 81 | 623 | 623 | 765 |
| duckstation | 681 | 54 | 26 | 622 | 622 | 761 |
| esde | 576 | 47 | 124 | 592 | 592 | 747 |
| ryujinx | 585 | 58 | 83 | 600 | 600 | 726 |
| cemu | 633 | 56 | 18 | 582 | 582 | 707 |
| rpcs3 | 621 | 54 | 28 | 572 | 572 | 703 |
| xenia | 571 | 48 | 59 | 557 | 557 | 678 |
| srm | 551 | 43 | 53 | 534 | 534 | 647 |
| shadps4 | 525 | 50 | 47 | 511 | 511 | 622 |
| vita3k | 560 | 48 | 13 | 506 | 506 | 621 |
| cloudsync | 319 | 13 | 121 | 354 | 354 | 453 |
| ppsspp | 259 | 40 | 61 | 300 | 300 | 360 |
| dolphin | 283 | 43 | 29 | 294 | 294 | 355 |
| ra | 286 | 43 | 26 | 302 | 302 | 355 |
| xemu | 239 | 33 | 22 | 248 | 248 | 294 |
| melonds | 240 | 32 | 20 | 240 | 240 | 292 |
| mgba | 250 | 22 | 20 | 233 | 233 | 292 |
| primehack | 206 | 34 | 23 | 222 | 222 | 263 |
| model2 | 202 | 43 | 3 | 205 | 205 | 248 |
| supermodel | 201 | 40 | 5 | 207 | 207 | 246 |
| scummvm | 201 | 30 | 12 | 202 | 202 | 243 |
| bigpemu | 172 | 3 | 2 | 136 | 136 | 177 |
| armsx2 | 55 | 57 | 0 | 88 | 88 | 112 |
| flycast | 63 | 9 | 5 | 60 | 60 | 77 |
| rmg | 52 | 16 | 0 | 52 | 52 | 68 |
| mame | 41 | 2 | 9 | 39 | 39 | 52 |
| eden | 26 | 3 | 0 | 12 | 12 | 29 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
