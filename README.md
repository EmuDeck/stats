# Estadísticas de EmuDeck

Actualizado: 2026-10-10 21:13 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 170 |
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
| Con CloudSync | 182 | 182 | 292 |
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
| pcsx2 | 430 | 11 | 56 | 316 | 316 | 497 |
| esde | 365 | 37 | 86 | 288 | 288 | 488 |
| azahar | 381 | 42 | 57 | 301 | 301 | 480 |
| duckstation | 414 | 40 | 19 | 294 | 294 | 473 |
| ryujinx | 369 | 43 | 54 | 299 | 299 | 466 |
| rpcs3 | 378 | 39 | 20 | 269 | 269 | 437 |
| cemu | 379 | 41 | 15 | 276 | 276 | 435 |
| xenia | 338 | 35 | 37 | 259 | 259 | 410 |
| srm | 342 | 27 | 30 | 262 | 262 | 399 |
| shadps4 | 326 | 38 | 29 | 240 | 240 | 393 |
| vita3k | 338 | 35 | 11 | 233 | 233 | 384 |
| cloudsync | 206 | 13 | 86 | 192 | 192 | 305 |
| ra | 165 | 32 | 20 | 147 | 147 | 217 |
| dolphin | 160 | 31 | 21 | 141 | 141 | 212 |
| ppsspp | 145 | 29 | 37 | 135 | 135 | 211 |
| mgba | 152 | 17 | 12 | 109 | 109 | 181 |
| melonds | 134 | 21 | 16 | 113 | 113 | 171 |
| xemu | 132 | 22 | 17 | 109 | 109 | 171 |
| primehack | 127 | 23 | 19 | 113 | 113 | 169 |
| model2 | 120 | 27 | 2 | 99 | 99 | 149 |
| scummvm | 114 | 22 | 12 | 95 | 95 | 148 |
| supermodel | 114 | 27 | 5 | 97 | 97 | 146 |
| bigpemu | 110 | 3 | 2 | 59 | 59 | 115 |
| armsx2 | 31 | 43 | 0 | 48 | 48 | 74 |
| flycast | 38 | 5 | 4 | 28 | 28 | 47 |
| rmg | 35 | 10 | 0 | 32 | 32 | 45 |
| mame | 29 | 1 | 6 | 24 | 24 | 36 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
