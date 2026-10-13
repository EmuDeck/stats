# Estadísticas de EmuDeck

Actualizado: 2026-10-13 23:36 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 36 | 252 | 252 | 300 |
| linux-arm | 4 | 36 | 36 | 46 |
| windows | 6 | 50 | 50 | 66 |

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
| Instalaciones early | 245 | 245 | 303 |
| Con CloudSync | 336 | 336 | 449 |
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
| pcsx2 | 721 | 14 | 91 | 657 | 657 | 826 |
| azahar | 648 | 58 | 85 | 623 | 623 | 791 |
| duckstation | 704 | 56 | 27 | 622 | 622 | 787 |
| esde | 599 | 50 | 128 | 592 | 592 | 777 |
| ryujinx | 605 | 59 | 87 | 600 | 600 | 751 |
| cemu | 651 | 58 | 19 | 582 | 582 | 728 |
| rpcs3 | 641 | 56 | 29 | 572 | 572 | 726 |
| xenia | 591 | 50 | 62 | 557 | 557 | 703 |
| srm | 565 | 45 | 59 | 534 | 534 | 669 |
| shadps4 | 541 | 52 | 49 | 511 | 511 | 642 |
| vita3k | 578 | 50 | 13 | 506 | 506 | 641 |
| cloudsync | 331 | 13 | 125 | 354 | 354 | 469 |
| ppsspp | 266 | 40 | 65 | 300 | 300 | 371 |
| dolphin | 291 | 43 | 31 | 294 | 294 | 365 |
| ra | 294 | 43 | 27 | 302 | 302 | 364 |
| melonds | 247 | 32 | 22 | 240 | 240 | 301 |
| xemu | 245 | 33 | 22 | 248 | 248 | 300 |
| mgba | 257 | 22 | 20 | 233 | 233 | 299 |
| primehack | 212 | 34 | 24 | 222 | 222 | 270 |
| model2 | 207 | 43 | 4 | 205 | 205 | 254 |
| supermodel | 206 | 40 | 6 | 207 | 207 | 252 |
| scummvm | 206 | 30 | 12 | 202 | 202 | 248 |
| bigpemu | 179 | 3 | 2 | 136 | 136 | 184 |
| armsx2 | 57 | 59 | 0 | 88 | 88 | 116 |
| flycast | 63 | 10 | 5 | 60 | 60 | 78 |
| rmg | 52 | 17 | 0 | 52 | 52 | 69 |
| mame | 41 | 2 | 9 | 39 | 39 | 52 |
| eden | 26 | 3 | 0 | 12 | 12 | 29 |
| pegasus | 5 | 0 | 3 | 4 | 4 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
