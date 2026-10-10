# Estadísticas de EmuDeck

Actualizado: 2026-10-10 16:15 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 159 |
| linux-arm | 8 | 20 | 20 | 31 |
| windows | 6 | 22 | 22 | 37 |

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
| Instalaciones early | 107 | 107 | 156 |
| Con CloudSync | 182 | 182 | 279 |
| % con CloudSync | | | 179% |

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
| pcsx2 | 387 | 11 | 52 | 316 | 316 | 450 |
| esde | 332 | 36 | 79 | 288 | 288 | 447 |
| azahar | 343 | 41 | 52 | 301 | 301 | 436 |
| duckstation | 372 | 39 | 19 | 294 | 294 | 430 |
| ryujinx | 336 | 42 | 51 | 299 | 299 | 429 |
| cemu | 343 | 40 | 14 | 276 | 276 | 397 |
| rpcs3 | 334 | 38 | 19 | 269 | 269 | 391 |
| xenia | 300 | 34 | 34 | 259 | 259 | 368 |
| srm | 307 | 27 | 27 | 262 | 262 | 361 |
| shadps4 | 289 | 37 | 26 | 240 | 240 | 352 |
| vita3k | 303 | 34 | 9 | 233 | 233 | 346 |
| cloudsync | 196 | 13 | 83 | 192 | 192 | 292 |
| ra | 154 | 31 | 20 | 147 | 147 | 205 |
| dolphin | 147 | 30 | 21 | 141 | 141 | 198 |
| ppsspp | 134 | 28 | 34 | 135 | 135 | 196 |
| melonds | 124 | 20 | 16 | 113 | 113 | 160 |
| mgba | 131 | 17 | 12 | 109 | 109 | 160 |
| primehack | 117 | 22 | 18 | 113 | 113 | 157 |
| xemu | 116 | 21 | 16 | 109 | 109 | 153 |
| model2 | 111 | 26 | 2 | 99 | 99 | 139 |
| scummvm | 106 | 21 | 11 | 95 | 95 | 138 |
| supermodel | 107 | 26 | 5 | 97 | 97 | 138 |
| bigpemu | 90 | 3 | 2 | 59 | 59 | 95 |
| armsx2 | 26 | 42 | 0 | 48 | 48 | 68 |
| flycast | 35 | 5 | 4 | 28 | 28 | 44 |
| rmg | 32 | 10 | 0 | 32 | 32 | 42 |
| mame | 26 | 1 | 6 | 24 | 24 | 33 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
