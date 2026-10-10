# Estadísticas de EmuDeck

Actualizado: 2026-10-10 05:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| windows | 6 | 22 | 22 | 31 |

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
| pcsx2 | 357 | 11 | 46 | 316 | 316 | 414 |
| esde | 306 | 27 | 69 | 288 | 288 | 402 |
| azahar | 317 | 38 | 45 | 301 | 301 | 400 |
| duckstation | 343 | 33 | 18 | 294 | 294 | 394 |
| ryujinx | 306 | 34 | 46 | 299 | 299 | 386 |
| cemu | 316 | 33 | 14 | 276 | 276 | 363 |
| rpcs3 | 305 | 32 | 18 | 269 | 269 | 355 |
| xenia | 279 | 27 | 30 | 259 | 259 | 336 |
| srm | 283 | 26 | 22 | 262 | 262 | 331 |
| shadps4 | 267 | 30 | 24 | 240 | 240 | 321 |
| vita3k | 281 | 27 | 9 | 233 | 233 | 317 |
| cloudsync | 186 | 10 | 81 | 192 | 192 | 277 |
| ra | 147 | 25 | 18 | 147 | 147 | 190 |
| dolphin | 138 | 24 | 20 | 141 | 141 | 182 |
| ppsspp | 126 | 21 | 28 | 135 | 135 | 175 |
| melonds | 117 | 17 | 15 | 113 | 113 | 149 |
| primehack | 111 | 20 | 14 | 113 | 113 | 145 |
| xemu | 109 | 17 | 16 | 109 | 109 | 142 |
| mgba | 116 | 13 | 10 | 109 | 109 | 139 |
| model2 | 106 | 19 | 2 | 99 | 99 | 127 |
| scummvm | 101 | 15 | 10 | 95 | 95 | 126 |
| supermodel | 102 | 19 | 4 | 97 | 97 | 125 |
| bigpemu | 77 | 3 | 1 | 59 | 59 | 81 |
| armsx2 | 25 | 36 | 0 | 48 | 48 | 61 |
| rmg | 30 | 10 | 0 | 32 | 32 | 40 |
| flycast | 32 | 2 | 3 | 28 | 28 | 37 |
| mame | 24 | 1 | 5 | 24 | 24 | 30 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
