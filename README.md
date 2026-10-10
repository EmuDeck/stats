# Estadísticas de EmuDeck

Actualizado: 2026-10-10 11:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux-arm | 8 | 20 | 20 | 29 |
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
| Instalaciones early | 107 | 107 | 150 |
| Con CloudSync | 182 | 182 | 273 |
| % con CloudSync | | | 182% |

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
| esde | 313 | 33 | 75 | 288 | 288 | 421 |
| azahar | 327 | 40 | 48 | 301 | 301 | 415 |
| duckstation | 354 | 37 | 18 | 294 | 294 | 409 |
| ryujinx | 318 | 40 | 48 | 299 | 299 | 406 |
| cemu | 325 | 38 | 14 | 276 | 276 | 377 |
| rpcs3 | 316 | 36 | 18 | 269 | 269 | 370 |
| xenia | 289 | 32 | 32 | 259 | 259 | 353 |
| srm | 292 | 26 | 25 | 262 | 262 | 343 |
| shadps4 | 276 | 35 | 25 | 240 | 240 | 336 |
| vita3k | 290 | 32 | 9 | 233 | 233 | 331 |
| cloudsync | 191 | 12 | 83 | 192 | 192 | 286 |
| ra | 151 | 29 | 19 | 147 | 147 | 199 |
| dolphin | 142 | 28 | 21 | 141 | 141 | 191 |
| ppsspp | 129 | 26 | 31 | 135 | 135 | 186 |
| melonds | 122 | 19 | 16 | 113 | 113 | 157 |
| primehack | 114 | 21 | 16 | 113 | 113 | 151 |
| mgba | 120 | 16 | 12 | 109 | 109 | 148 |
| xemu | 112 | 20 | 16 | 109 | 109 | 148 |
| model2 | 109 | 24 | 2 | 99 | 99 | 135 |
| scummvm | 104 | 19 | 11 | 95 | 95 | 134 |
| supermodel | 105 | 24 | 4 | 97 | 97 | 133 |
| bigpemu | 81 | 3 | 1 | 59 | 59 | 85 |
| armsx2 | 25 | 40 | 0 | 48 | 48 | 65 |
| flycast | 33 | 4 | 4 | 28 | 28 | 41 |
| rmg | 30 | 10 | 0 | 32 | 32 | 40 |
| mame | 24 | 1 | 6 | 24 | 24 | 31 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
