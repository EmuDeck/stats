# Estadísticas de EmuDeck

Actualizado: 2026-10-10 14:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 157 |
| linux-arm | 8 | 20 | 20 | 31 |
| windows | 6 | 22 | 22 | 35 |

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
| Instalaciones early | 107 | 107 | 154 |
| Con CloudSync | 182 | 182 | 276 |
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
| pcsx2 | 381 | 11 | 49 | 316 | 316 | 441 |
| esde | 325 | 36 | 77 | 288 | 288 | 438 |
| azahar | 337 | 41 | 49 | 301 | 301 | 427 |
| duckstation | 366 | 39 | 18 | 294 | 294 | 423 |
| ryujinx | 328 | 42 | 51 | 299 | 299 | 421 |
| cemu | 335 | 40 | 14 | 276 | 276 | 389 |
| rpcs3 | 328 | 38 | 18 | 269 | 269 | 384 |
| xenia | 295 | 34 | 32 | 259 | 259 | 361 |
| srm | 300 | 27 | 26 | 262 | 262 | 353 |
| shadps4 | 284 | 37 | 25 | 240 | 240 | 346 |
| vita3k | 298 | 34 | 9 | 233 | 233 | 341 |
| cloudsync | 193 | 13 | 83 | 192 | 192 | 289 |
| ra | 153 | 31 | 20 | 147 | 147 | 204 |
| dolphin | 146 | 30 | 21 | 141 | 141 | 197 |
| ppsspp | 133 | 28 | 31 | 135 | 135 | 192 |
| melonds | 123 | 20 | 16 | 113 | 113 | 159 |
| mgba | 126 | 17 | 12 | 109 | 109 | 155 |
| primehack | 116 | 22 | 16 | 113 | 113 | 154 |
| xemu | 115 | 21 | 16 | 109 | 109 | 152 |
| model2 | 110 | 26 | 2 | 99 | 99 | 138 |
| scummvm | 105 | 21 | 11 | 95 | 95 | 137 |
| supermodel | 106 | 26 | 4 | 97 | 97 | 136 |
| bigpemu | 87 | 3 | 1 | 59 | 59 | 91 |
| armsx2 | 26 | 42 | 0 | 48 | 48 | 68 |
| flycast | 34 | 5 | 4 | 28 | 28 | 43 |
| rmg | 31 | 10 | 0 | 32 | 32 | 41 |
| mame | 25 | 1 | 6 | 24 | 24 | 32 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
