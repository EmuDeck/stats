# Estadísticas de EmuDeck

Actualizado: 2026-10-14 14:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 319 |
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
| Instalaciones early | 280 | 280 | 315 |
| Con CloudSync | 385 | 385 | 492 |
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
| pcsx2 | 789 | 15 | 96 | 753 | 753 | 900 |
| azahar | 705 | 62 | 88 | 717 | 717 | 855 |
| duckstation | 766 | 60 | 28 | 715 | 715 | 854 |
| esde | 649 | 55 | 137 | 686 | 686 | 841 |
| ryujinx | 663 | 63 | 89 | 685 | 685 | 815 |
| rpcs3 | 703 | 61 | 30 | 660 | 660 | 794 |
| cemu | 706 | 62 | 20 | 666 | 666 | 788 |
| xenia | 641 | 54 | 66 | 645 | 645 | 761 |
| srm | 609 | 47 | 60 | 622 | 622 | 716 |
| shadps4 | 600 | 54 | 51 | 579 | 579 | 705 |
| vita3k | 630 | 54 | 13 | 579 | 579 | 697 |
| cloudsync | 360 | 15 | 137 | 403 | 403 | 512 |
| dolphin | 314 | 44 | 37 | 336 | 336 | 395 |
| ppsspp | 285 | 41 | 68 | 340 | 340 | 394 |
| ra | 315 | 44 | 28 | 336 | 336 | 387 |
| mgba | 282 | 23 | 20 | 278 | 278 | 325 |
| melonds | 268 | 33 | 22 | 274 | 274 | 323 |
| xemu | 264 | 34 | 23 | 275 | 275 | 321 |
| primehack | 231 | 35 | 24 | 246 | 246 | 290 |
| model2 | 226 | 44 | 4 | 234 | 234 | 274 |
| supermodel | 225 | 41 | 6 | 232 | 232 | 272 |
| scummvm | 224 | 31 | 12 | 225 | 225 | 267 |
| bigpemu | 199 | 3 | 3 | 166 | 166 | 205 |
| armsx2 | 66 | 63 | 0 | 107 | 107 | 129 |
| flycast | 65 | 10 | 5 | 73 | 73 | 80 |
| rmg | 55 | 17 | 0 | 65 | 65 | 72 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 29 | 6 | 0 | 21 | 21 | 35 |
| pegasus | 5 | 0 | 4 | 6 | 6 | 9 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
