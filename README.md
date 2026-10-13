# Estadísticas de EmuDeck

Actualizado: 2026-10-13 13:50 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 285 |
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
| Instalaciones early | 245 | 245 | 279 |
| Con CloudSync | 336 | 336 | 414 |
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
| pcsx2 | 682 | 12 | 82 | 657 | 657 | 776 |
| duckstation | 665 | 49 | 26 | 622 | 622 | 740 |
| azahar | 612 | 51 | 75 | 623 | 623 | 738 |
| esde | 562 | 46 | 123 | 592 | 592 | 731 |
| ryujinx | 576 | 52 | 78 | 600 | 600 | 706 |
| cemu | 620 | 50 | 18 | 582 | 582 | 688 |
| rpcs3 | 606 | 49 | 28 | 572 | 572 | 683 |
| xenia | 557 | 44 | 54 | 557 | 557 | 655 |
| srm | 537 | 39 | 48 | 534 | 534 | 624 |
| shadps4 | 514 | 49 | 44 | 511 | 511 | 607 |
| vita3k | 549 | 44 | 13 | 506 | 506 | 606 |
| cloudsync | 304 | 13 | 117 | 354 | 354 | 434 |
| dolphin | 277 | 39 | 29 | 294 | 294 | 345 |
| ppsspp | 252 | 36 | 56 | 300 | 300 | 344 |
| ra | 279 | 39 | 26 | 302 | 302 | 344 |
| xemu | 233 | 29 | 22 | 248 | 248 | 284 |
| mgba | 241 | 22 | 20 | 233 | 233 | 283 |
| melonds | 233 | 28 | 18 | 240 | 240 | 279 |
| primehack | 203 | 30 | 21 | 222 | 222 | 254 |
| supermodel | 195 | 36 | 5 | 207 | 207 | 236 |
| model2 | 196 | 36 | 3 | 205 | 205 | 235 |
| scummvm | 195 | 26 | 12 | 202 | 202 | 233 |
| bigpemu | 168 | 3 | 2 | 136 | 136 | 173 |
| armsx2 | 54 | 52 | 0 | 88 | 88 | 106 |
| flycast | 60 | 9 | 5 | 60 | 60 | 74 |
| rmg | 49 | 16 | 0 | 52 | 52 | 65 |
| mame | 38 | 2 | 9 | 39 | 39 | 49 |
| eden | 23 | 3 | 0 | 12 | 12 | 26 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
