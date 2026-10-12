# Estadísticas de EmuDeck

Actualizado: 2026-10-12 22:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 269 |
| linux-arm | 3 | 32 | 32 | 39 |
| windows | 10 | 44 | 44 | 57 |

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
| Instalaciones early | 206 | 206 | 265 |
| Con CloudSync | 295 | 295 | 394 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 632 | 12 | 79 | 561 | 561 | 723 |
| azahar | 566 | 49 | 75 | 531 | 531 | 690 |
| duckstation | 616 | 47 | 24 | 530 | 530 | 687 |
| esde | 517 | 44 | 117 | 505 | 505 | 678 |
| ryujinx | 533 | 50 | 77 | 518 | 518 | 660 |
| cemu | 572 | 48 | 17 | 487 | 487 | 637 |
| rpcs3 | 563 | 46 | 23 | 487 | 487 | 632 |
| xenia | 515 | 42 | 53 | 466 | 466 | 610 |
| srm | 496 | 33 | 46 | 460 | 460 | 575 |
| shadps4 | 477 | 47 | 44 | 439 | 439 | 568 |
| vita3k | 509 | 42 | 11 | 425 | 425 | 562 |
| cloudsync | 289 | 13 | 112 | 311 | 311 | 414 |
| ppsspp | 238 | 34 | 55 | 258 | 258 | 327 |
| ra | 265 | 37 | 23 | 259 | 259 | 325 |
| dolphin | 258 | 36 | 25 | 254 | 254 | 319 |
| xemu | 220 | 27 | 22 | 210 | 210 | 269 |
| melonds | 219 | 26 | 18 | 204 | 204 | 263 |
| mgba | 214 | 21 | 18 | 197 | 197 | 253 |
| primehack | 193 | 28 | 21 | 190 | 190 | 242 |
| supermodel | 184 | 34 | 5 | 176 | 176 | 223 |
| model2 | 185 | 34 | 2 | 176 | 176 | 221 |
| scummvm | 183 | 26 | 12 | 174 | 174 | 221 |
| bigpemu | 147 | 3 | 2 | 121 | 121 | 152 |
| armsx2 | 46 | 50 | 0 | 76 | 76 | 96 |
| flycast | 52 | 8 | 5 | 53 | 53 | 65 |
| rmg | 42 | 14 | 0 | 45 | 45 | 56 |
| mame | 33 | 1 | 9 | 38 | 38 | 43 |
| eden | 17 | 3 | 0 | 8 | 8 | 20 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 2 | 2 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
