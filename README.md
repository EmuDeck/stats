# Estadísticas de EmuDeck

Actualizado: 2026-10-13 06:28 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 279 |
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
| Instalaciones early | 245 | 245 | 274 |
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
| pcsx2 | 664 | 12 | 81 | 657 | 657 | 757 |
| duckstation | 647 | 49 | 26 | 622 | 622 | 722 |
| azahar | 595 | 51 | 75 | 623 | 623 | 721 |
| esde | 548 | 46 | 120 | 592 | 592 | 714 |
| ryujinx | 562 | 52 | 78 | 600 | 600 | 692 |
| cemu | 603 | 50 | 18 | 582 | 582 | 671 |
| rpcs3 | 591 | 48 | 26 | 572 | 572 | 665 |
| xenia | 541 | 44 | 54 | 557 | 557 | 639 |
| srm | 525 | 36 | 47 | 534 | 534 | 608 |
| shadps4 | 499 | 48 | 44 | 511 | 511 | 591 |
| vita3k | 534 | 44 | 12 | 506 | 506 | 590 |
| cloudsync | 303 | 13 | 116 | 354 | 354 | 432 |
| ppsspp | 246 | 36 | 56 | 300 | 300 | 338 |
| ra | 273 | 39 | 26 | 302 | 302 | 338 |
| dolphin | 269 | 38 | 29 | 294 | 294 | 336 |
| xemu | 228 | 29 | 22 | 248 | 248 | 279 |
| melonds | 228 | 28 | 18 | 240 | 240 | 274 |
| mgba | 230 | 22 | 20 | 233 | 233 | 272 |
| primehack | 200 | 30 | 21 | 222 | 222 | 251 |
| supermodel | 190 | 35 | 5 | 207 | 207 | 230 |
| model2 | 191 | 35 | 3 | 205 | 205 | 229 |
| scummvm | 189 | 26 | 12 | 202 | 202 | 227 |
| bigpemu | 159 | 3 | 2 | 136 | 136 | 164 |
| armsx2 | 50 | 52 | 0 | 88 | 88 | 102 |
| flycast | 54 | 9 | 5 | 60 | 60 | 68 |
| rmg | 45 | 16 | 0 | 52 | 52 | 61 |
| mame | 35 | 2 | 9 | 39 | 39 | 46 |
| eden | 22 | 3 | 0 | 12 | 12 | 25 |
| pegasus | 5 | 0 | 2 | 4 | 4 | 7 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
