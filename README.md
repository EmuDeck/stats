# Estadísticas de EmuDeck

Actualizado: 2026-10-13 12:56 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 284 |
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
| Instalaciones early | 245 | 245 | 278 |
| Con CloudSync | 336 | 336 | 414 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 679 | 12 | 82 | 657 | 657 | 773 |
| duckstation | 661 | 49 | 26 | 622 | 622 | 736 |
| azahar | 609 | 51 | 75 | 623 | 623 | 735 |
| esde | 561 | 46 | 122 | 592 | 592 | 729 |
| ryujinx | 573 | 52 | 78 | 600 | 600 | 703 |
| cemu | 617 | 50 | 18 | 582 | 582 | 685 |
| rpcs3 | 603 | 49 | 27 | 572 | 572 | 679 |
| xenia | 554 | 44 | 54 | 557 | 557 | 652 |
| srm | 535 | 39 | 48 | 534 | 534 | 622 |
| shadps4 | 511 | 49 | 44 | 511 | 511 | 604 |
| vita3k | 546 | 44 | 13 | 506 | 506 | 603 |
| cloudsync | 304 | 13 | 117 | 354 | 354 | 434 |
| dolphin | 276 | 39 | 29 | 294 | 294 | 344 |
| ppsspp | 251 | 36 | 56 | 300 | 300 | 343 |
| ra | 278 | 39 | 26 | 302 | 302 | 343 |
| xemu | 232 | 29 | 22 | 248 | 248 | 283 |
| mgba | 238 | 22 | 20 | 233 | 233 | 280 |
| melonds | 232 | 28 | 18 | 240 | 240 | 278 |
| primehack | 203 | 30 | 21 | 222 | 222 | 254 |
| supermodel | 194 | 36 | 5 | 207 | 207 | 235 |
| model2 | 195 | 36 | 3 | 205 | 205 | 234 |
| scummvm | 194 | 26 | 12 | 202 | 202 | 232 |
| bigpemu | 167 | 3 | 2 | 136 | 136 | 172 |
| armsx2 | 53 | 52 | 0 | 88 | 88 | 105 |
| flycast | 59 | 9 | 5 | 60 | 60 | 73 |
| rmg | 48 | 16 | 0 | 52 | 52 | 64 |
| mame | 37 | 2 | 9 | 39 | 39 | 48 |
| eden | 22 | 3 | 0 | 12 | 12 | 25 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
