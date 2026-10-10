# Estadísticas de EmuDeck

Actualizado: 2026-10-10 05:41 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 149 |
| linux-arm | 8 | 20 | 20 | 25 |
| windows | 6 | 22 | 22 | 32 |

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
| Instalaciones early | 107 | 107 | 141 |
| Con CloudSync | 182 | 182 | 265 |
| % con CloudSync | | | 188% |

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
| pcsx2 | 358 | 11 | 47 | 316 | 316 | 416 |
| esde | 307 | 27 | 70 | 288 | 288 | 404 |
| azahar | 318 | 38 | 46 | 301 | 301 | 402 |
| duckstation | 344 | 34 | 18 | 294 | 294 | 396 |
| ryujinx | 307 | 35 | 46 | 299 | 299 | 388 |
| cemu | 316 | 34 | 14 | 276 | 276 | 364 |
| rpcs3 | 306 | 32 | 18 | 269 | 269 | 356 |
| xenia | 280 | 28 | 31 | 259 | 259 | 339 |
| srm | 284 | 26 | 22 | 262 | 262 | 332 |
| shadps4 | 268 | 31 | 24 | 240 | 240 | 323 |
| vita3k | 282 | 28 | 9 | 233 | 233 | 319 |
| cloudsync | 186 | 10 | 81 | 192 | 192 | 277 |
| ra | 147 | 26 | 18 | 147 | 147 | 191 |
| dolphin | 138 | 25 | 20 | 141 | 141 | 183 |
| ppsspp | 126 | 22 | 29 | 135 | 135 | 177 |
| melonds | 117 | 18 | 15 | 113 | 113 | 150 |
| primehack | 111 | 20 | 15 | 113 | 113 | 146 |
| xemu | 109 | 18 | 16 | 109 | 109 | 143 |
| mgba | 117 | 13 | 10 | 109 | 109 | 140 |
| model2 | 106 | 20 | 2 | 99 | 99 | 128 |
| scummvm | 101 | 16 | 10 | 95 | 95 | 127 |
| supermodel | 102 | 20 | 4 | 97 | 97 | 126 |
| bigpemu | 78 | 3 | 1 | 59 | 59 | 82 |
| armsx2 | 25 | 36 | 0 | 48 | 48 | 61 |
| rmg | 30 | 10 | 0 | 32 | 32 | 40 |
| flycast | 32 | 2 | 3 | 28 | 28 | 37 |
| mame | 24 | 1 | 5 | 24 | 24 | 30 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
