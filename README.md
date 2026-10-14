# Estadísticas de EmuDeck

Actualizado: 2026-10-14 07:19 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 313 |
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
| Instalaciones early | 280 | 280 | 312 |
| Con CloudSync | 385 | 385 | 474 |
| % con CloudSync | | | 152% |

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
| pcsx2 | 767 | 15 | 95 | 753 | 753 | 877 |
| azahar | 688 | 60 | 88 | 717 | 717 | 836 |
| duckstation | 749 | 58 | 27 | 715 | 715 | 834 |
| esde | 638 | 53 | 134 | 686 | 686 | 825 |
| ryujinx | 648 | 61 | 88 | 685 | 685 | 797 |
| rpcs3 | 686 | 59 | 29 | 660 | 660 | 774 |
| cemu | 690 | 60 | 19 | 666 | 666 | 769 |
| xenia | 625 | 52 | 66 | 645 | 645 | 743 |
| srm | 597 | 46 | 60 | 622 | 622 | 703 |
| shadps4 | 579 | 53 | 51 | 579 | 579 | 683 |
| vita3k | 618 | 52 | 13 | 579 | 579 | 683 |
| cloudsync | 348 | 14 | 132 | 403 | 403 | 494 |
| ppsspp | 278 | 40 | 68 | 340 | 340 | 386 |
| dolphin | 307 | 43 | 35 | 336 | 336 | 385 |
| ra | 307 | 43 | 27 | 336 | 336 | 377 |
| mgba | 279 | 23 | 20 | 278 | 278 | 322 |
| melonds | 259 | 32 | 22 | 274 | 274 | 313 |
| xemu | 257 | 33 | 23 | 275 | 275 | 313 |
| primehack | 224 | 34 | 24 | 246 | 246 | 282 |
| model2 | 218 | 43 | 4 | 234 | 234 | 265 |
| supermodel | 217 | 40 | 6 | 232 | 232 | 263 |
| scummvm | 217 | 30 | 12 | 225 | 225 | 259 |
| bigpemu | 195 | 3 | 3 | 166 | 166 | 201 |
| armsx2 | 66 | 61 | 0 | 107 | 107 | 127 |
| flycast | 64 | 10 | 5 | 73 | 73 | 79 |
| rmg | 54 | 17 | 0 | 65 | 65 | 71 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 26 | 6 | 0 | 21 | 21 | 32 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
