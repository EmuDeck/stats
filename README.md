# Estadísticas de EmuDeck

Actualizado: 2026-10-10 12:20 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 153 |
| linux-arm | 8 | 20 | 20 | 31 |
| windows | 6 | 22 | 22 | 34 |

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
| Instalaciones early | 107 | 107 | 152 |
| Con CloudSync | 182 | 182 | 274 |
| % con CloudSync | | | 180% |

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
| pcsx2 | 369 | 11 | 49 | 316 | 316 | 429 |
| esde | 313 | 36 | 75 | 288 | 288 | 424 |
| azahar | 327 | 41 | 48 | 301 | 301 | 416 |
| duckstation | 354 | 39 | 18 | 294 | 294 | 411 |
| ryujinx | 318 | 42 | 48 | 299 | 299 | 408 |
| cemu | 325 | 40 | 14 | 276 | 276 | 379 |
| rpcs3 | 316 | 38 | 18 | 269 | 269 | 372 |
| xenia | 289 | 34 | 32 | 259 | 259 | 355 |
| srm | 292 | 27 | 25 | 262 | 262 | 344 |
| shadps4 | 276 | 37 | 25 | 240 | 240 | 338 |
| vita3k | 290 | 34 | 9 | 233 | 233 | 333 |
| cloudsync | 191 | 13 | 83 | 192 | 192 | 287 |
| ra | 151 | 31 | 19 | 147 | 147 | 201 |
| dolphin | 142 | 30 | 21 | 141 | 141 | 193 |
| ppsspp | 129 | 28 | 31 | 135 | 135 | 188 |
| melonds | 122 | 20 | 16 | 113 | 113 | 158 |
| primehack | 114 | 22 | 16 | 113 | 113 | 152 |
| mgba | 120 | 17 | 12 | 109 | 109 | 149 |
| xemu | 112 | 21 | 16 | 109 | 109 | 149 |
| model2 | 109 | 26 | 2 | 99 | 99 | 137 |
| scummvm | 104 | 21 | 11 | 95 | 95 | 136 |
| supermodel | 105 | 26 | 4 | 97 | 97 | 135 |
| bigpemu | 81 | 3 | 1 | 59 | 59 | 85 |
| armsx2 | 25 | 42 | 0 | 48 | 48 | 67 |
| flycast | 33 | 5 | 4 | 28 | 28 | 42 |
| rmg | 30 | 10 | 0 | 32 | 32 | 40 |
| mame | 24 | 1 | 6 | 24 | 24 | 31 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
