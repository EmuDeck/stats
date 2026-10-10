# Estadísticas de EmuDeck

Actualizado: 2026-10-10 16:41 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| windows | 6 | 22 | 22 | 38 |

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
| Instalaciones early | 107 | 107 | 158 |
| Con CloudSync | 182 | 182 | 280 |
| % con CloudSync | | | 177% |

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
| pcsx2 | 391 | 11 | 53 | 316 | 316 | 455 |
| esde | 335 | 36 | 80 | 288 | 288 | 451 |
| azahar | 347 | 41 | 52 | 301 | 301 | 440 |
| ryujinx | 340 | 42 | 53 | 299 | 299 | 435 |
| duckstation | 376 | 39 | 19 | 294 | 294 | 434 |
| cemu | 347 | 40 | 14 | 276 | 276 | 401 |
| rpcs3 | 338 | 38 | 19 | 269 | 269 | 395 |
| xenia | 304 | 34 | 34 | 259 | 259 | 372 |
| srm | 311 | 27 | 27 | 262 | 262 | 365 |
| shadps4 | 292 | 37 | 26 | 240 | 240 | 355 |
| vita3k | 306 | 34 | 9 | 233 | 233 | 349 |
| cloudsync | 196 | 13 | 84 | 192 | 192 | 293 |
| ra | 155 | 31 | 20 | 147 | 147 | 206 |
| dolphin | 148 | 30 | 21 | 141 | 141 | 199 |
| ppsspp | 135 | 28 | 34 | 135 | 135 | 197 |
| mgba | 133 | 17 | 12 | 109 | 109 | 162 |
| melonds | 125 | 20 | 16 | 113 | 113 | 161 |
| primehack | 118 | 22 | 18 | 113 | 113 | 158 |
| xemu | 117 | 21 | 16 | 109 | 109 | 154 |
| model2 | 112 | 26 | 2 | 99 | 99 | 140 |
| scummvm | 107 | 21 | 11 | 95 | 95 | 139 |
| supermodel | 108 | 26 | 5 | 97 | 97 | 139 |
| bigpemu | 92 | 3 | 2 | 59 | 59 | 97 |
| armsx2 | 28 | 42 | 0 | 48 | 48 | 70 |
| flycast | 35 | 5 | 4 | 28 | 28 | 44 |
| rmg | 32 | 10 | 0 | 32 | 32 | 42 |
| mame | 26 | 1 | 6 | 24 | 24 | 33 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
