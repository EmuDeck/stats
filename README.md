# Estadísticas de EmuDeck

Actualizado: 2026-10-10 23:13 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 174 |
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
| Instalaciones early | 107 | 107 | 173 |
| Con CloudSync | 182 | 182 | 294 |
| % con CloudSync | | | 170% |

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
| pcsx2 | 442 | 11 | 57 | 316 | 316 | 510 |
| esde | 374 | 37 | 90 | 288 | 288 | 501 |
| azahar | 392 | 42 | 58 | 301 | 301 | 492 |
| duckstation | 425 | 40 | 19 | 294 | 294 | 484 |
| ryujinx | 378 | 43 | 56 | 299 | 299 | 477 |
| rpcs3 | 390 | 39 | 20 | 269 | 269 | 449 |
| cemu | 389 | 41 | 15 | 276 | 276 | 445 |
| xenia | 346 | 35 | 39 | 259 | 259 | 420 |
| srm | 353 | 27 | 30 | 262 | 262 | 410 |
| shadps4 | 336 | 38 | 29 | 240 | 240 | 403 |
| vita3k | 346 | 35 | 11 | 233 | 233 | 392 |
| cloudsync | 210 | 13 | 86 | 192 | 192 | 309 |
| ra | 170 | 32 | 20 | 147 | 147 | 222 |
| dolphin | 164 | 31 | 21 | 141 | 141 | 216 |
| ppsspp | 149 | 29 | 38 | 135 | 135 | 216 |
| mgba | 155 | 17 | 12 | 109 | 109 | 184 |
| xemu | 136 | 22 | 19 | 109 | 109 | 177 |
| melonds | 138 | 21 | 16 | 113 | 113 | 175 |
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
