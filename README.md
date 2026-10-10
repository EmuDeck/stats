# Estadísticas de EmuDeck

Actualizado: 2026-10-10 21:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 171 |
| linux-arm | 8 | 20 | 20 | 32 |
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
| Instalaciones early | 107 | 107 | 169 |
| Con CloudSync | 182 | 182 | 293 |
| % con CloudSync | | | 173% |

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
| pcsx2 | 433 | 11 | 56 | 316 | 316 | 500 |
| esde | 367 | 37 | 86 | 288 | 288 | 490 |
| azahar | 383 | 42 | 57 | 301 | 301 | 482 |
| duckstation | 417 | 40 | 19 | 294 | 294 | 476 |
| ryujinx | 371 | 43 | 54 | 299 | 299 | 468 |
| rpcs3 | 381 | 39 | 20 | 269 | 269 | 440 |
| cemu | 381 | 41 | 15 | 276 | 276 | 437 |
| xenia | 339 | 35 | 37 | 259 | 259 | 411 |
| srm | 345 | 27 | 30 | 262 | 262 | 402 |
| shadps4 | 329 | 38 | 29 | 240 | 240 | 396 |
| vita3k | 339 | 35 | 11 | 233 | 233 | 385 |
| cloudsync | 207 | 13 | 86 | 192 | 192 | 306 |
| ra | 166 | 32 | 20 | 147 | 147 | 218 |
| dolphin | 161 | 31 | 21 | 141 | 141 | 213 |
| ppsspp | 146 | 29 | 37 | 135 | 135 | 212 |
| mgba | 152 | 17 | 12 | 109 | 109 | 181 |
| melonds | 135 | 21 | 16 | 113 | 113 | 172 |
| xemu | 133 | 22 | 17 | 109 | 109 | 172 |
| primehack | 128 | 23 | 19 | 113 | 113 | 170 |
| model2 | 121 | 27 | 2 | 99 | 99 | 150 |
| scummvm | 115 | 22 | 12 | 95 | 95 | 149 |
| supermodel | 115 | 27 | 5 | 97 | 97 | 147 |
| bigpemu | 110 | 3 | 2 | 59 | 59 | 115 |
| armsx2 | 31 | 43 | 0 | 48 | 48 | 74 |
| flycast | 38 | 5 | 4 | 28 | 28 | 47 |
| rmg | 35 | 10 | 0 | 32 | 32 | 45 |
| mame | 29 | 1 | 6 | 24 | 24 | 36 |
| eden | 10 | 1 | 0 | 2 | 2 | 11 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
