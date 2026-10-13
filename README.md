# Estadísticas de EmuDeck

Actualizado: 2026-10-13 07:53 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 280 |
| linux-arm | 4 | 36 | 36 | 40 |
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
| Instalaciones early | 245 | 245 | 275 |
| Con CloudSync | 336 | 336 | 412 |
| % con CloudSync | | | 150% |

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
| pcsx2 | 667 | 12 | 81 | 657 | 657 | 760 |
| duckstation | 650 | 49 | 26 | 622 | 622 | 725 |
| azahar | 598 | 51 | 75 | 623 | 623 | 724 |
| esde | 550 | 46 | 120 | 592 | 592 | 716 |
| ryujinx | 564 | 52 | 78 | 600 | 600 | 694 |
| cemu | 606 | 50 | 18 | 582 | 582 | 674 |
| rpcs3 | 594 | 48 | 26 | 572 | 572 | 668 |
| xenia | 544 | 44 | 54 | 557 | 557 | 642 |
| srm | 527 | 36 | 48 | 534 | 534 | 611 |
| shadps4 | 502 | 48 | 44 | 511 | 511 | 594 |
| vita3k | 536 | 44 | 12 | 506 | 506 | 592 |
| cloudsync | 303 | 13 | 116 | 354 | 354 | 432 |
| ppsspp | 247 | 36 | 56 | 300 | 300 | 339 |
| ra | 274 | 39 | 26 | 302 | 302 | 339 |
| dolphin | 271 | 38 | 29 | 294 | 294 | 338 |
| xemu | 229 | 29 | 22 | 248 | 248 | 280 |
| melonds | 229 | 28 | 18 | 240 | 240 | 275 |
| mgba | 230 | 22 | 20 | 233 | 233 | 272 |
| primehack | 201 | 30 | 21 | 222 | 222 | 252 |
| supermodel | 191 | 35 | 5 | 207 | 207 | 231 |
| model2 | 192 | 35 | 3 | 205 | 205 | 230 |
| scummvm | 191 | 26 | 12 | 202 | 202 | 229 |
| bigpemu | 160 | 3 | 2 | 136 | 136 | 165 |
| armsx2 | 50 | 52 | 0 | 88 | 88 | 102 |
| flycast | 55 | 9 | 5 | 60 | 60 | 69 |
| rmg | 45 | 16 | 0 | 52 | 52 | 61 |
| mame | 35 | 2 | 9 | 39 | 39 | 46 |
| eden | 22 | 3 | 0 | 12 | 12 | 25 |
| pegasus | 5 | 0 | 2 | 4 | 4 | 7 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
