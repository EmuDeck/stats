# Estadísticas de EmuDeck

Actualizado: 2026-10-14 18:18 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13168 | 96146 |
| Linux ARM | 126 | 1213 |
| Windows | 3456 | 25673 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1566**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125, 13994, 13168]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195, 143, 126]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407, 3719, 3456]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 27 | 279 | 279 | 327 |
| linux-arm | 7 | 43 | 43 | 47 |
| windows | 9 | 59 | 59 | 68 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61, 36, 27]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3, 4, 7]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10, 6, 9]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323, 369, 412]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 279 | 43 | 59 | 381 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 280 | 280 | 320 |
| Con CloudSync | 385 | 385 | 499 |
| % con CloudSync | | | 156% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11", "10-12", "10-13"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54, 39, 35]
    line [58, 69, 55, 49, 64, 41, 49]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 807 | 15 | 97 | 753 | 753 | 919 |
| azahar | 723 | 62 | 88 | 717 | 717 | 873 |
| duckstation | 784 | 60 | 29 | 715 | 715 | 873 |
| esde | 666 | 55 | 137 | 686 | 686 | 858 |
| ryujinx | 675 | 64 | 89 | 685 | 685 | 828 |
| rpcs3 | 722 | 61 | 32 | 660 | 660 | 815 |
| cemu | 724 | 62 | 20 | 666 | 666 | 806 |
| xenia | 658 | 54 | 67 | 645 | 645 | 779 |
| srm | 625 | 47 | 60 | 622 | 622 | 732 |
| shadps4 | 613 | 54 | 53 | 579 | 579 | 720 |
| vita3k | 647 | 54 | 14 | 579 | 579 | 715 |
| cloudsync | 364 | 15 | 140 | 403 | 403 | 519 |
| dolphin | 321 | 44 | 37 | 336 | 336 | 402 |
| ppsspp | 292 | 41 | 68 | 340 | 340 | 401 |
| ra | 322 | 44 | 29 | 336 | 336 | 395 |
| melonds | 275 | 33 | 22 | 274 | 274 | 330 |
| mgba | 286 | 23 | 20 | 278 | 278 | 329 |
| xemu | 271 | 34 | 24 | 275 | 275 | 329 |
| primehack | 238 | 35 | 24 | 246 | 246 | 297 |
| model2 | 234 | 44 | 4 | 234 | 234 | 282 |
| supermodel | 232 | 41 | 7 | 232 | 232 | 280 |
| scummvm | 231 | 31 | 12 | 225 | 225 | 274 |
| bigpemu | 203 | 3 | 3 | 166 | 166 | 209 |
| armsx2 | 67 | 63 | 0 | 107 | 107 | 130 |
| flycast | 66 | 10 | 5 | 73 | 73 | 81 |
| rmg | 56 | 17 | 0 | 65 | 65 | 73 |
| mame | 42 | 2 | 9 | 48 | 48 | 53 |
| eden | 31 | 6 | 0 | 21 | 21 | 37 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
