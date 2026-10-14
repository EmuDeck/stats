# Estadísticas de EmuDeck

Actualizado: 2026-10-14 03:17 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 306 |
| linux-arm | 7 | 43 | 43 | 46 |
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
| Instalaciones early | 280 | 280 | 307 |
| Con CloudSync | 385 | 385 | 463 |
| % con CloudSync | | | 151% |

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
| pcsx2 | 747 | 15 | 94 | 753 | 753 | 856 |
| azahar | 669 | 59 | 87 | 717 | 717 | 815 |
| duckstation | 729 | 57 | 27 | 715 | 715 | 813 |
| esde | 618 | 51 | 133 | 686 | 686 | 802 |
| ryujinx | 623 | 60 | 88 | 685 | 685 | 771 |
| rpcs3 | 665 | 57 | 29 | 660 | 660 | 751 |
| cemu | 670 | 59 | 19 | 666 | 666 | 748 |
| xenia | 609 | 51 | 65 | 645 | 645 | 725 |
| srm | 585 | 46 | 59 | 622 | 622 | 690 |
| shadps4 | 562 | 52 | 51 | 579 | 579 | 665 |
| vita3k | 600 | 51 | 13 | 579 | 579 | 664 |
| cloudsync | 341 | 13 | 129 | 403 | 403 | 483 |
| ppsspp | 271 | 40 | 67 | 340 | 340 | 378 |
| dolphin | 297 | 43 | 31 | 336 | 336 | 371 |
| ra | 300 | 43 | 27 | 336 | 336 | 370 |
| mgba | 268 | 23 | 20 | 278 | 278 | 311 |
| melonds | 252 | 32 | 22 | 274 | 274 | 306 |
| xemu | 250 | 33 | 23 | 275 | 275 | 306 |
| primehack | 216 | 34 | 24 | 246 | 246 | 274 |
| model2 | 212 | 43 | 4 | 234 | 234 | 259 |
| supermodel | 211 | 40 | 6 | 232 | 232 | 257 |
| scummvm | 210 | 30 | 12 | 225 | 225 | 252 |
| bigpemu | 189 | 3 | 2 | 166 | 166 | 194 |
| armsx2 | 63 | 60 | 0 | 107 | 107 | 123 |
| flycast | 63 | 10 | 5 | 73 | 73 | 78 |
| rmg | 52 | 17 | 0 | 65 | 65 | 69 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 26 | 5 | 0 | 21 | 21 | 31 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 5 | 0 | 0 | 4 | 4 | 5 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
