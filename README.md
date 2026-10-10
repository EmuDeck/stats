# Estadísticas de EmuDeck

Actualizado: 2026-10-10 19:11 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 163 |
| linux-arm | 8 | 20 | 20 | 31 |
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
| Instalaciones early | 107 | 107 | 162 |
| Con CloudSync | 182 | 182 | 284 |
| % con CloudSync | | | 175% |

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
| pcsx2 | 410 | 11 | 56 | 316 | 316 | 477 |
| esde | 353 | 36 | 84 | 288 | 288 | 473 |
| azahar | 365 | 41 | 56 | 301 | 301 | 462 |
| duckstation | 395 | 39 | 19 | 294 | 294 | 453 |
| ryujinx | 355 | 42 | 54 | 299 | 299 | 451 |
| cemu | 364 | 40 | 14 | 276 | 276 | 418 |
| rpcs3 | 359 | 38 | 20 | 269 | 269 | 417 |
| xenia | 320 | 34 | 37 | 259 | 259 | 391 |
| srm | 328 | 27 | 29 | 262 | 262 | 384 |
| shadps4 | 308 | 37 | 29 | 240 | 240 | 374 |
| vita3k | 324 | 34 | 10 | 233 | 233 | 368 |
| cloudsync | 199 | 13 | 85 | 192 | 192 | 297 |
| ra | 158 | 31 | 20 | 147 | 147 | 209 |
| dolphin | 152 | 30 | 21 | 141 | 141 | 203 |
| ppsspp | 138 | 28 | 37 | 135 | 135 | 203 |
| mgba | 142 | 17 | 12 | 109 | 109 | 171 |
| melonds | 128 | 20 | 16 | 113 | 113 | 164 |
| primehack | 121 | 22 | 19 | 113 | 113 | 162 |
| xemu | 120 | 21 | 17 | 109 | 109 | 158 |
| model2 | 115 | 26 | 2 | 99 | 99 | 143 |
| scummvm | 110 | 21 | 12 | 95 | 95 | 143 |
| supermodel | 110 | 26 | 5 | 97 | 97 | 141 |
| bigpemu | 101 | 3 | 2 | 59 | 59 | 106 |
| armsx2 | 30 | 42 | 0 | 48 | 48 | 72 |
| flycast | 35 | 5 | 4 | 28 | 28 | 44 |
| rmg | 32 | 10 | 0 | 32 | 32 | 42 |
| mame | 26 | 1 | 6 | 24 | 24 | 33 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
