# Estadísticas de EmuDeck

Actualizado: 2026-10-11 04:45 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 15258 | 64741 |
| Linux ARM | 222 | 971 |
| Windows | 4198 | 17412 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **968**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 35 | 155 | 155 | 194 |
| linux-arm | 9 | 29 | 29 | 32 |
| windows | 12 | 34 | 34 | 46 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Total"
    line [31, 71, 135, 193, 249]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 155 | 29 | 34 | 218 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 152 | 152 | 190 |
| Con CloudSync | 231 | 231 | 304 |
| % con CloudSync | | | 160% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45]
    line [58, 69, 55, 49]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 479 | 11 | 63 | 441 | 441 | 553 |
| azahar | 426 | 42 | 63 | 422 | 422 | 531 |
| esde | 395 | 37 | 94 | 415 | 415 | 526 |
| duckstation | 459 | 40 | 19 | 416 | 416 | 518 |
| ryujinx | 408 | 43 | 58 | 412 | 412 | 509 |
| rpcs3 | 421 | 39 | 21 | 385 | 385 | 481 |
| cemu | 419 | 41 | 15 | 386 | 386 | 475 |
| xenia | 374 | 35 | 44 | 362 | 362 | 453 |
| srm | 378 | 27 | 34 | 365 | 365 | 439 |
| shadps4 | 365 | 38 | 33 | 341 | 341 | 436 |
| vita3k | 373 | 35 | 11 | 332 | 332 | 419 |
| cloudsync | 217 | 13 | 89 | 244 | 244 | 319 |
| ra | 190 | 32 | 20 | 196 | 196 | 242 |
| ppsspp | 169 | 29 | 43 | 187 | 187 | 241 |
| dolphin | 184 | 31 | 22 | 189 | 189 | 237 |
| melonds | 158 | 21 | 17 | 150 | 150 | 196 |
| mgba | 165 | 17 | 13 | 164 | 164 | 195 |
| xemu | 153 | 22 | 20 | 153 | 153 | 195 |
| primehack | 141 | 23 | 20 | 150 | 150 | 184 |
| model2 | 137 | 27 | 2 | 133 | 133 | 166 |
| scummvm | 131 | 22 | 12 | 129 | 129 | 165 |
| supermodel | 132 | 27 | 5 | 130 | 130 | 164 |
| bigpemu | 121 | 3 | 2 | 101 | 101 | 126 |
| armsx2 | 34 | 43 | 0 | 65 | 65 | 77 |
| flycast | 39 | 5 | 4 | 42 | 42 | 48 |
| rmg | 35 | 10 | 0 | 41 | 41 | 45 |
| mame | 29 | 1 | 6 | 32 | 32 | 36 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
