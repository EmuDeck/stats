# Estadísticas de EmuDeck

Actualizado: 2026-10-10 23:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 176 |
| linux-arm | 8 | 20 | 20 | 32 |
| windows | 6 | 22 | 22 | 41 |

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
| Instalaciones early | 107 | 107 | 175 |
| Con CloudSync | 182 | 182 | 295 |
| % con CloudSync | | | 169% |

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
| pcsx2 | 446 | 11 | 57 | 316 | 316 | 514 |
| esde | 378 | 37 | 91 | 288 | 288 | 506 |
| azahar | 396 | 42 | 58 | 301 | 301 | 496 |
| duckstation | 429 | 40 | 19 | 294 | 294 | 488 |
| ryujinx | 379 | 43 | 56 | 299 | 299 | 478 |
| rpcs3 | 392 | 39 | 20 | 269 | 269 | 451 |
| cemu | 392 | 41 | 15 | 276 | 276 | 448 |
| xenia | 346 | 35 | 39 | 259 | 259 | 420 |
| srm | 355 | 27 | 30 | 262 | 262 | 412 |
| shadps4 | 337 | 38 | 29 | 240 | 240 | 404 |
| vita3k | 348 | 35 | 11 | 233 | 233 | 394 |
| cloudsync | 211 | 13 | 86 | 192 | 192 | 310 |
| ra | 172 | 32 | 20 | 147 | 147 | 224 |
| dolphin | 166 | 31 | 21 | 141 | 141 | 218 |
| ppsspp | 151 | 29 | 38 | 135 | 135 | 218 |
| mgba | 156 | 17 | 12 | 109 | 109 | 185 |
| xemu | 137 | 22 | 19 | 109 | 109 | 178 |
| melonds | 140 | 21 | 16 | 113 | 113 | 177 |
| primehack | 131 | 23 | 20 | 113 | 113 | 174 |
| model2 | 124 | 27 | 2 | 99 | 99 | 153 |
| scummvm | 118 | 22 | 12 | 95 | 95 | 152 |
| supermodel | 118 | 27 | 5 | 97 | 97 | 150 |
| bigpemu | 114 | 3 | 2 | 59 | 59 | 119 |
| armsx2 | 31 | 43 | 0 | 48 | 48 | 74 |
| flycast | 38 | 5 | 4 | 28 | 28 | 47 |
| rmg | 35 | 10 | 0 | 32 | 32 | 45 |
| mame | 29 | 1 | 6 | 24 | 24 | 36 |
| eden | 10 | 2 | 0 | 2 | 2 | 12 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 1 | 1 | 2 |
