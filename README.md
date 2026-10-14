# Estadísticas de EmuDeck

Actualizado: 2026-10-14 23:35 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 337 |
| linux-arm | 7 | 43 | 43 | 48 |
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
| Instalaciones early | 280 | 280 | 327 |
| Con CloudSync | 385 | 385 | 516 |
| % con CloudSync | | | 158% |

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
| pcsx2 | 834 | 15 | 97 | 753 | 753 | 946 |
| azahar | 746 | 64 | 91 | 717 | 717 | 901 |
| duckstation | 805 | 62 | 30 | 715 | 715 | 897 |
| esde | 688 | 57 | 139 | 686 | 686 | 884 |
| ryujinx | 700 | 64 | 90 | 685 | 685 | 854 |
| rpcs3 | 748 | 62 | 32 | 660 | 660 | 842 |
| cemu | 753 | 62 | 22 | 666 | 666 | 837 |
| xenia | 683 | 54 | 68 | 645 | 645 | 805 |
| srm | 644 | 47 | 60 | 622 | 622 | 751 |
| shadps4 | 637 | 56 | 54 | 579 | 579 | 747 |
| vita3k | 676 | 54 | 14 | 579 | 579 | 744 |
| cloudsync | 379 | 16 | 141 | 403 | 403 | 536 |
| dolphin | 330 | 45 | 38 | 336 | 336 | 413 |
| ppsspp | 300 | 42 | 68 | 340 | 340 | 410 |
| ra | 333 | 45 | 31 | 336 | 336 | 409 |
| melonds | 286 | 34 | 24 | 274 | 274 | 344 |
| xemu | 280 | 35 | 24 | 275 | 275 | 339 |
| mgba | 290 | 23 | 21 | 278 | 278 | 334 |
| primehack | 247 | 36 | 24 | 246 | 246 | 307 |
| supermodel | 248 | 42 | 7 | 232 | 232 | 297 |
| model2 | 244 | 45 | 4 | 234 | 234 | 293 |
| scummvm | 240 | 31 | 12 | 225 | 225 | 283 |
| bigpemu | 207 | 3 | 5 | 166 | 166 | 215 |
| armsx2 | 69 | 65 | 0 | 107 | 107 | 134 |
| flycast | 68 | 10 | 5 | 73 | 73 | 83 |
| rmg | 58 | 17 | 0 | 65 | 65 | 75 |
| mame | 42 | 2 | 9 | 48 | 48 | 53 |
| eden | 31 | 6 | 0 | 21 | 21 | 37 |
| pegasus | 6 | 0 | 4 | 6 | 6 | 10 |
| yuzu | 6 | 0 | 0 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| citron | 2 | 0 | 0 | 1 | 1 | 2 |
