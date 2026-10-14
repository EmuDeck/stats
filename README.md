# Estadísticas de EmuDeck

Actualizado: 2026-10-14 13:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 318 |
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
| Instalaciones early | 280 | 280 | 313 |
| Con CloudSync | 385 | 385 | 491 |
| % con CloudSync | | | 157% |

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
| pcsx2 | 783 | 15 | 96 | 753 | 753 | 894 |
| azahar | 702 | 60 | 88 | 717 | 717 | 850 |
| duckstation | 763 | 58 | 28 | 715 | 715 | 849 |
| esde | 648 | 53 | 137 | 686 | 686 | 838 |
| ryujinx | 658 | 61 | 89 | 685 | 685 | 808 |
| rpcs3 | 699 | 59 | 30 | 660 | 660 | 788 |
| cemu | 704 | 60 | 20 | 666 | 666 | 784 |
| xenia | 639 | 52 | 66 | 645 | 645 | 757 |
| srm | 606 | 46 | 60 | 622 | 622 | 712 |
| shadps4 | 593 | 53 | 51 | 579 | 579 | 697 |
| vita3k | 629 | 52 | 13 | 579 | 579 | 694 |
| cloudsync | 360 | 14 | 137 | 403 | 403 | 511 |
| dolphin | 313 | 43 | 37 | 336 | 336 | 393 |
| ppsspp | 284 | 40 | 68 | 340 | 340 | 392 |
| ra | 313 | 43 | 28 | 336 | 336 | 384 |
| mgba | 281 | 23 | 20 | 278 | 278 | 324 |
| melonds | 267 | 32 | 22 | 274 | 274 | 321 |
| xemu | 263 | 33 | 23 | 275 | 275 | 319 |
| primehack | 230 | 34 | 24 | 246 | 246 | 288 |
| model2 | 225 | 43 | 4 | 234 | 234 | 272 |
| supermodel | 224 | 40 | 6 | 232 | 232 | 270 |
| scummvm | 223 | 30 | 12 | 225 | 225 | 265 |
| bigpemu | 198 | 3 | 3 | 166 | 166 | 204 |
| armsx2 | 66 | 61 | 0 | 107 | 107 | 127 |
| flycast | 65 | 10 | 5 | 73 | 73 | 80 |
| rmg | 55 | 17 | 0 | 65 | 65 | 72 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 26 | 6 | 0 | 21 | 21 | 32 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
