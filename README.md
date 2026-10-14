# Estadísticas de EmuDeck

Actualizado: 2026-10-14 16:15 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 323 |
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
| Instalaciones early | 280 | 280 | 316 |
| Con CloudSync | 385 | 385 | 494 |
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
| pcsx2 | 796 | 15 | 96 | 753 | 753 | 907 |
| azahar | 712 | 62 | 88 | 717 | 717 | 862 |
| duckstation | 773 | 60 | 28 | 715 | 715 | 861 |
| esde | 655 | 55 | 137 | 686 | 686 | 847 |
| ryujinx | 666 | 63 | 89 | 685 | 685 | 818 |
| rpcs3 | 711 | 61 | 30 | 660 | 660 | 802 |
| cemu | 712 | 62 | 20 | 666 | 666 | 794 |
| xenia | 647 | 54 | 66 | 645 | 645 | 767 |
| srm | 618 | 47 | 60 | 622 | 622 | 725 |
| shadps4 | 605 | 54 | 51 | 579 | 579 | 710 |
| vita3k | 637 | 54 | 13 | 579 | 579 | 704 |
| cloudsync | 361 | 15 | 138 | 403 | 403 | 514 |
| dolphin | 317 | 44 | 37 | 336 | 336 | 398 |
| ppsspp | 288 | 41 | 68 | 340 | 340 | 397 |
| ra | 318 | 44 | 28 | 336 | 336 | 390 |
| mgba | 285 | 23 | 20 | 278 | 278 | 328 |
| melonds | 270 | 33 | 22 | 274 | 274 | 325 |
| xemu | 266 | 34 | 23 | 275 | 275 | 323 |
| primehack | 234 | 35 | 24 | 246 | 246 | 293 |
| model2 | 229 | 44 | 4 | 234 | 234 | 277 |
| supermodel | 227 | 41 | 6 | 232 | 232 | 274 |
| scummvm | 226 | 31 | 12 | 225 | 225 | 269 |
| bigpemu | 201 | 3 | 3 | 166 | 166 | 207 |
| armsx2 | 67 | 63 | 0 | 107 | 107 | 130 |
| flycast | 66 | 10 | 5 | 73 | 73 | 81 |
| rmg | 56 | 17 | 0 | 65 | 65 | 73 |
| mame | 42 | 2 | 9 | 48 | 48 | 53 |
| eden | 31 | 6 | 0 | 21 | 21 | 37 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
