# Estadísticas de EmuDeck

Actualizado: 2026-10-10 17:11 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 160 |
| linux-arm | 8 | 20 | 20 | 31 |
| windows | 6 | 22 | 22 | 39 |

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
| Instalaciones early | 107 | 107 | 159 |
| Con CloudSync | 182 | 182 | 283 |
| % con CloudSync | | | 178% |

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
| pcsx2 | 393 | 11 | 54 | 316 | 316 | 458 |
| esde | 336 | 36 | 81 | 288 | 288 | 453 |
| azahar | 349 | 41 | 54 | 301 | 301 | 444 |
| ryujinx | 342 | 42 | 54 | 299 | 299 | 438 |
| duckstation | 378 | 39 | 19 | 294 | 294 | 436 |
| cemu | 349 | 40 | 14 | 276 | 276 | 403 |
| rpcs3 | 341 | 38 | 20 | 269 | 269 | 399 |
| xenia | 306 | 34 | 36 | 259 | 259 | 376 |
| srm | 313 | 27 | 27 | 262 | 262 | 367 |
| shadps4 | 294 | 37 | 28 | 240 | 240 | 359 |
| vita3k | 308 | 34 | 10 | 233 | 233 | 352 |
| cloudsync | 198 | 13 | 85 | 192 | 192 | 296 |
| ra | 155 | 31 | 20 | 147 | 147 | 206 |
| dolphin | 148 | 30 | 21 | 141 | 141 | 199 |
| ppsspp | 135 | 28 | 36 | 135 | 135 | 199 |
| mgba | 135 | 17 | 12 | 109 | 109 | 164 |
| melonds | 125 | 20 | 16 | 113 | 113 | 161 |
| primehack | 118 | 22 | 19 | 113 | 113 | 159 |
| xemu | 117 | 21 | 17 | 109 | 109 | 155 |
| model2 | 112 | 26 | 2 | 99 | 99 | 140 |
| scummvm | 107 | 21 | 12 | 95 | 95 | 140 |
| supermodel | 108 | 26 | 5 | 97 | 97 | 139 |
| bigpemu | 94 | 3 | 2 | 59 | 59 | 99 |
| armsx2 | 29 | 42 | 0 | 48 | 48 | 71 |
| flycast | 35 | 5 | 4 | 28 | 28 | 44 |
| rmg | 32 | 10 | 0 | 32 | 32 | 42 |
| mame | 26 | 1 | 6 | 24 | 24 | 33 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
