# Estadísticas de EmuDeck

Actualizado: 2026-10-10 18:17 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 13083 | 49483 |
| Linux ARM | 177 | 749 |
| Windows | 3508 | 13214 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **739**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09"]
    y-axis "Arranques"
    line [222, 160, 190, 177]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 44 | 120 | 120 | 162 |
| linux-arm | 8 | 20 | 20 | 31 |
| windows | 6 | 22 | 22 | 40 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09"]
    y-axis "Instalaciones"
    line [34, 42, 44]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09"]
    y-axis "Instalaciones"
    line [1, 11, 8]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09"]
    y-axis "Instalaciones"
    line [5, 11, 6]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09"]
    y-axis "Total"
    line [31, 71, 135, 193]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 120 | 20 | 22 | 162 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 107 | 107 | 161 |
| Con CloudSync | 182 | 182 | 284 |
| % con CloudSync | | | 176% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09"]
    y-axis "Instalaciones"
    line [29, 39, 39]
    line [58, 69, 55]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 400 | 11 | 56 | 316 | 316 | 467 |
| esde | 343 | 36 | 84 | 288 | 288 | 463 |
| azahar | 355 | 41 | 56 | 301 | 301 | 452 |
| duckstation | 385 | 39 | 19 | 294 | 294 | 443 |
| ryujinx | 346 | 42 | 54 | 299 | 299 | 442 |
| cemu | 355 | 40 | 14 | 276 | 276 | 409 |
| rpcs3 | 347 | 38 | 20 | 269 | 269 | 405 |
| xenia | 311 | 34 | 37 | 259 | 259 | 382 |
| srm | 319 | 27 | 28 | 262 | 262 | 374 |
| shadps4 | 300 | 37 | 29 | 240 | 240 | 366 |
| vita3k | 314 | 34 | 10 | 233 | 233 | 358 |
| cloudsync | 199 | 13 | 85 | 192 | 192 | 297 |
| ra | 156 | 31 | 20 | 147 | 147 | 207 |
| dolphin | 150 | 30 | 21 | 141 | 141 | 201 |
| ppsspp | 136 | 28 | 37 | 135 | 135 | 201 |
| mgba | 138 | 17 | 12 | 109 | 109 | 167 |
| melonds | 126 | 20 | 16 | 113 | 113 | 162 |
| primehack | 120 | 22 | 19 | 113 | 113 | 161 |
| xemu | 118 | 21 | 17 | 109 | 109 | 156 |
| model2 | 113 | 26 | 2 | 99 | 99 | 141 |
| scummvm | 108 | 21 | 12 | 95 | 95 | 141 |
| supermodel | 109 | 26 | 5 | 97 | 97 | 140 |
| bigpemu | 95 | 3 | 2 | 59 | 59 | 100 |
| armsx2 | 29 | 42 | 0 | 48 | 48 | 71 |
| flycast | 35 | 5 | 4 | 28 | 28 | 44 |
| rmg | 32 | 10 | 0 | 32 | 32 | 42 |
| mame | 26 | 1 | 6 | 24 | 24 | 33 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
