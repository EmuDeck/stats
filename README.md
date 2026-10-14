# Estadísticas de EmuDeck

Actualizado: 2026-10-14 05:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 312 |
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
| Instalaciones early | 280 | 280 | 311 |
| Con CloudSync | 385 | 385 | 466 |
| % con CloudSync | | | 150% |

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
| pcsx2 | 760 | 15 | 94 | 753 | 753 | 869 |
| azahar | 682 | 60 | 88 | 717 | 717 | 830 |
| duckstation | 741 | 58 | 27 | 715 | 715 | 826 |
| esde | 629 | 53 | 133 | 686 | 686 | 815 |
| ryujinx | 639 | 61 | 88 | 685 | 685 | 788 |
| rpcs3 | 679 | 58 | 29 | 660 | 660 | 766 |
| cemu | 683 | 60 | 19 | 666 | 666 | 762 |
| xenia | 619 | 52 | 65 | 645 | 645 | 736 |
| srm | 592 | 46 | 60 | 622 | 622 | 698 |
| shadps4 | 573 | 53 | 51 | 579 | 579 | 677 |
| vita3k | 611 | 52 | 13 | 579 | 579 | 676 |
| cloudsync | 343 | 14 | 129 | 403 | 403 | 486 |
| ppsspp | 276 | 40 | 67 | 340 | 340 | 383 |
| dolphin | 303 | 43 | 31 | 336 | 336 | 377 |
| ra | 305 | 43 | 27 | 336 | 336 | 375 |
| mgba | 273 | 23 | 20 | 278 | 278 | 316 |
| melonds | 257 | 32 | 22 | 274 | 274 | 311 |
| xemu | 255 | 33 | 23 | 275 | 275 | 311 |
| primehack | 223 | 34 | 24 | 246 | 246 | 281 |
| model2 | 217 | 43 | 4 | 234 | 234 | 264 |
| supermodel | 216 | 40 | 6 | 232 | 232 | 262 |
| scummvm | 215 | 30 | 12 | 225 | 225 | 257 |
| bigpemu | 192 | 3 | 2 | 166 | 166 | 197 |
| armsx2 | 64 | 61 | 0 | 107 | 107 | 125 |
| flycast | 64 | 10 | 5 | 73 | 73 | 79 |
| rmg | 53 | 17 | 0 | 65 | 65 | 70 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 26 | 6 | 0 | 21 | 21 | 32 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
