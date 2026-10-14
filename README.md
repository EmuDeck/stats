# Estadísticas de EmuDeck

Actualizado: 2026-10-14 00:35 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 27 | 279 | 279 | 301 |
| linux-arm | 7 | 43 | 43 | 46 |
| windows | 9 | 59 | 59 | 66 |

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
| Instalaciones early | 280 | 280 | 304 |
| Con CloudSync | 385 | 385 | 453 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 726 | 14 | 91 | 753 | 753 | 831 |
| azahar | 651 | 58 | 85 | 717 | 717 | 794 |
| duckstation | 707 | 56 | 27 | 715 | 715 | 790 |
| esde | 605 | 50 | 129 | 686 | 686 | 784 |
| ryujinx | 609 | 59 | 87 | 685 | 685 | 755 |
| cemu | 654 | 58 | 19 | 666 | 666 | 731 |
| rpcs3 | 646 | 56 | 29 | 660 | 660 | 731 |
| xenia | 594 | 50 | 62 | 645 | 645 | 706 |
| srm | 568 | 45 | 59 | 622 | 622 | 672 |
| shadps4 | 546 | 52 | 49 | 579 | 579 | 647 |
| vita3k | 582 | 50 | 13 | 579 | 579 | 645 |
| cloudsync | 335 | 13 | 125 | 403 | 403 | 473 |
| ppsspp | 266 | 40 | 65 | 340 | 340 | 371 |
| dolphin | 291 | 43 | 31 | 336 | 336 | 365 |
| ra | 295 | 43 | 27 | 336 | 336 | 365 |
| mgba | 260 | 22 | 20 | 278 | 278 | 302 |
| melonds | 247 | 32 | 22 | 274 | 274 | 301 |
| xemu | 245 | 33 | 22 | 275 | 275 | 300 |
| primehack | 212 | 34 | 24 | 246 | 246 | 270 |
| model2 | 207 | 43 | 4 | 234 | 234 | 254 |
| supermodel | 206 | 40 | 6 | 232 | 232 | 252 |
| scummvm | 206 | 30 | 12 | 225 | 225 | 248 |
| bigpemu | 181 | 3 | 2 | 166 | 166 | 186 |
| armsx2 | 59 | 59 | 0 | 107 | 107 | 118 |
| flycast | 63 | 10 | 5 | 73 | 73 | 78 |
| rmg | 52 | 17 | 0 | 65 | 65 | 69 |
| mame | 41 | 2 | 9 | 48 | 48 | 52 |
| eden | 26 | 3 | 0 | 21 | 21 | 29 |
| pegasus | 5 | 0 | 3 | 6 | 6 | 8 |
| ares | 3 | 1 | 0 | 4 | 4 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
