# Estadísticas de EmuDeck

Actualizado: 2026-10-13 00:44 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 277 |
| linux-arm | 4 | 36 | 36 | 39 |
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
| Instalaciones early | 245 | 245 | 271 |
| Con CloudSync | 336 | 336 | 400 |
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
| pcsx2 | 650 | 12 | 79 | 657 | 657 | 741 |
| azahar | 585 | 49 | 75 | 623 | 623 | 709 |
| duckstation | 632 | 47 | 24 | 622 | 622 | 703 |
| esde | 534 | 44 | 118 | 592 | 592 | 696 |
| ryujinx | 549 | 50 | 77 | 600 | 600 | 676 |
| cemu | 590 | 48 | 17 | 582 | 582 | 655 |
| rpcs3 | 579 | 46 | 23 | 572 | 572 | 648 |
| xenia | 528 | 42 | 53 | 557 | 557 | 623 |
| srm | 511 | 33 | 46 | 534 | 534 | 590 |
| shadps4 | 489 | 47 | 44 | 511 | 511 | 580 |
| vita3k | 523 | 42 | 11 | 506 | 506 | 576 |
| cloudsync | 292 | 13 | 115 | 354 | 354 | 420 |
| ppsspp | 243 | 34 | 55 | 300 | 300 | 332 |
| ra | 271 | 37 | 24 | 302 | 302 | 332 |
| dolphin | 265 | 36 | 25 | 294 | 294 | 326 |
| xemu | 227 | 27 | 22 | 248 | 248 | 276 |
| melonds | 226 | 26 | 18 | 240 | 240 | 270 |
| mgba | 220 | 21 | 18 | 233 | 233 | 259 |
| primehack | 199 | 28 | 21 | 222 | 222 | 248 |
| supermodel | 189 | 34 | 5 | 207 | 207 | 228 |
| model2 | 190 | 34 | 2 | 205 | 205 | 226 |
| scummvm | 188 | 26 | 12 | 202 | 202 | 226 |
| bigpemu | 155 | 3 | 2 | 136 | 136 | 160 |
| armsx2 | 47 | 50 | 0 | 88 | 88 | 97 |
| flycast | 52 | 8 | 5 | 60 | 60 | 65 |
| rmg | 43 | 14 | 0 | 52 | 52 | 57 |
| mame | 33 | 1 | 9 | 39 | 39 | 43 |
| eden | 20 | 3 | 0 | 12 | 12 | 23 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
