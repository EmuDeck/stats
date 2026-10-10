# Estadísticas de EmuDeck

Actualizado: 2026-10-10 09:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux-arm | 8 | 20 | 20 | 27 |
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
| Instalaciones early | 107 | 107 | 148 |
| Con CloudSync | 182 | 182 | 271 |
| % con CloudSync | | | 183% |

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
| pcsx2 | 367 | 11 | 48 | 316 | 316 | 426 |
| esde | 312 | 31 | 75 | 288 | 288 | 418 |
| azahar | 326 | 40 | 48 | 301 | 301 | 414 |
| duckstation | 353 | 35 | 18 | 294 | 294 | 406 |
| ryujinx | 315 | 38 | 47 | 299 | 299 | 400 |
| cemu | 324 | 36 | 14 | 276 | 276 | 374 |
| rpcs3 | 314 | 34 | 18 | 269 | 269 | 366 |
| xenia | 288 | 30 | 32 | 259 | 259 | 350 |
| srm | 291 | 26 | 25 | 262 | 262 | 342 |
| shadps4 | 275 | 33 | 25 | 240 | 240 | 333 |
| vita3k | 290 | 30 | 9 | 233 | 233 | 329 |
| cloudsync | 191 | 10 | 83 | 192 | 192 | 284 |
| ra | 151 | 27 | 19 | 147 | 147 | 197 |
| dolphin | 142 | 26 | 21 | 141 | 141 | 189 |
| ppsspp | 129 | 24 | 31 | 135 | 135 | 184 |
| melonds | 122 | 19 | 16 | 113 | 113 | 157 |
| primehack | 114 | 21 | 16 | 113 | 113 | 151 |
| xemu | 112 | 20 | 16 | 109 | 109 | 148 |
| mgba | 120 | 14 | 12 | 109 | 109 | 146 |
| model2 | 109 | 22 | 2 | 99 | 99 | 133 |
| scummvm | 104 | 17 | 11 | 95 | 95 | 132 |
| supermodel | 105 | 22 | 4 | 97 | 97 | 131 |
| bigpemu | 80 | 3 | 1 | 59 | 59 | 84 |
| armsx2 | 25 | 38 | 0 | 48 | 48 | 63 |
| rmg | 30 | 10 | 0 | 32 | 32 | 40 |
| flycast | 33 | 2 | 4 | 28 | 28 | 39 |
| mame | 24 | 1 | 6 | 24 | 24 | 31 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
