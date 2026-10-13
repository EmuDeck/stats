# Estadísticas de EmuDeck

Actualizado: 2026-10-13 15:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 291 |
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
| Instalaciones early | 245 | 245 | 285 |
| Con CloudSync | 336 | 336 | 425 |
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
| pcsx2 | 693 | 12 | 82 | 657 | 657 | 787 |
| duckstation | 676 | 49 | 26 | 622 | 622 | 751 |
| azahar | 622 | 51 | 75 | 623 | 623 | 748 |
| esde | 569 | 46 | 123 | 592 | 592 | 738 |
| ryujinx | 582 | 53 | 79 | 600 | 600 | 714 |
| cemu | 628 | 51 | 18 | 582 | 582 | 697 |
| rpcs3 | 616 | 49 | 28 | 572 | 572 | 693 |
| xenia | 563 | 44 | 54 | 557 | 557 | 661 |
| srm | 543 | 39 | 48 | 534 | 534 | 630 |
| shadps4 | 522 | 49 | 44 | 511 | 511 | 615 |
| vita3k | 555 | 44 | 13 | 506 | 506 | 612 |
| cloudsync | 311 | 13 | 121 | 354 | 354 | 445 |
| dolphin | 282 | 39 | 29 | 294 | 294 | 350 |
| ppsspp | 258 | 36 | 56 | 300 | 300 | 350 |
| ra | 285 | 39 | 26 | 302 | 302 | 350 |
| mgba | 247 | 22 | 20 | 233 | 233 | 289 |
| xemu | 238 | 29 | 22 | 248 | 248 | 289 |
| melonds | 239 | 28 | 18 | 240 | 240 | 285 |
| primehack | 205 | 30 | 21 | 222 | 222 | 256 |
| model2 | 201 | 39 | 3 | 205 | 205 | 243 |
| supermodel | 200 | 36 | 5 | 207 | 207 | 241 |
| scummvm | 200 | 26 | 12 | 202 | 202 | 238 |
| bigpemu | 170 | 3 | 2 | 136 | 136 | 175 |
| armsx2 | 54 | 52 | 0 | 88 | 88 | 106 |
| flycast | 63 | 9 | 5 | 60 | 60 | 77 |
| rmg | 52 | 16 | 0 | 52 | 52 | 68 |
| mame | 41 | 2 | 9 | 39 | 39 | 52 |
| eden | 25 | 3 | 0 | 12 | 12 | 28 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
