# Estadísticas de EmuDeck

Actualizado: 2026-10-10 20:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 169 |
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
| Instalaciones early | 107 | 107 | 167 |
| Con CloudSync | 182 | 182 | 291 |
| % con CloudSync | | | 174% |

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
| pcsx2 | 424 | 11 | 56 | 316 | 316 | 491 |
| esde | 364 | 36 | 86 | 288 | 288 | 486 |
| azahar | 378 | 41 | 57 | 301 | 301 | 476 |
| duckstation | 408 | 39 | 19 | 294 | 294 | 466 |
| ryujinx | 364 | 42 | 54 | 299 | 299 | 460 |
| cemu | 377 | 40 | 15 | 276 | 276 | 432 |
| rpcs3 | 372 | 38 | 20 | 269 | 269 | 430 |
| xenia | 332 | 34 | 37 | 259 | 259 | 403 |
| srm | 336 | 27 | 30 | 262 | 262 | 393 |
| shadps4 | 321 | 37 | 29 | 240 | 240 | 387 |
| vita3k | 335 | 34 | 11 | 233 | 233 | 380 |
| cloudsync | 205 | 13 | 86 | 192 | 192 | 304 |
| ra | 164 | 31 | 20 | 147 | 147 | 215 |
| dolphin | 159 | 30 | 21 | 141 | 141 | 210 |
| ppsspp | 144 | 28 | 37 | 135 | 135 | 209 |
| mgba | 152 | 17 | 12 | 109 | 109 | 181 |
| melonds | 134 | 20 | 16 | 113 | 113 | 170 |
| primehack | 126 | 22 | 19 | 113 | 113 | 167 |
| xemu | 128 | 21 | 17 | 109 | 109 | 166 |
| model2 | 120 | 26 | 2 | 99 | 99 | 148 |
| scummvm | 114 | 21 | 12 | 95 | 95 | 147 |
| supermodel | 114 | 26 | 5 | 97 | 97 | 145 |
| bigpemu | 108 | 3 | 2 | 59 | 59 | 113 |
| armsx2 | 31 | 42 | 0 | 48 | 48 | 73 |
| flycast | 38 | 5 | 4 | 28 | 28 | 47 |
| rmg | 35 | 10 | 0 | 32 | 32 | 45 |
| mame | 29 | 1 | 6 | 24 | 24 | 36 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
