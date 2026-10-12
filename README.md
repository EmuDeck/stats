# Estadísticas de EmuDeck

Actualizado: 2026-10-12 19:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 16125 | 80866 |
| Linux ARM | 195 | 1166 |
| Windows | 4407 | 21819 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1216**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 61 | 216 | 216 | 258 |
| linux-arm | 3 | 32 | 32 | 39 |
| windows | 10 | 44 | 44 | 56 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 216 | 32 | 44 | 292 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 206 | 206 | 254 |
| Con CloudSync | 295 | 295 | 377 |
| % con CloudSync | | | 148% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54]
    line [58, 69, 55, 49, 64]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 611 | 12 | 77 | 561 | 561 | 700 |
| azahar | 546 | 49 | 73 | 531 | 531 | 668 |
| duckstation | 595 | 47 | 24 | 530 | 530 | 666 |
| esde | 505 | 44 | 115 | 505 | 505 | 664 |
| ryujinx | 514 | 50 | 76 | 518 | 518 | 640 |
| rpcs3 | 544 | 46 | 23 | 487 | 487 | 613 |
| cemu | 547 | 48 | 17 | 487 | 487 | 612 |
| xenia | 494 | 42 | 52 | 466 | 466 | 588 |
| srm | 474 | 33 | 46 | 460 | 460 | 553 |
| shadps4 | 460 | 47 | 42 | 439 | 439 | 549 |
| vita3k | 489 | 42 | 11 | 425 | 425 | 542 |
| cloudsync | 272 | 13 | 110 | 311 | 311 | 395 |
| ppsspp | 227 | 34 | 54 | 258 | 258 | 315 |
| ra | 254 | 37 | 22 | 259 | 259 | 313 |
| dolphin | 247 | 36 | 25 | 254 | 254 | 308 |
| xemu | 209 | 27 | 22 | 210 | 210 | 258 |
| melonds | 209 | 26 | 18 | 204 | 204 | 253 |
| mgba | 205 | 21 | 18 | 197 | 197 | 244 |
| primehack | 185 | 28 | 21 | 190 | 190 | 234 |
| model2 | 175 | 34 | 2 | 176 | 176 | 211 |
| scummvm | 173 | 26 | 12 | 174 | 174 | 211 |
| supermodel | 172 | 34 | 5 | 176 | 176 | 211 |
| bigpemu | 146 | 3 | 2 | 121 | 121 | 151 |
| armsx2 | 45 | 50 | 0 | 76 | 76 | 95 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 40 | 14 | 0 | 45 | 45 | 54 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 16 | 3 | 0 | 8 | 8 | 19 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 2 | 2 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
