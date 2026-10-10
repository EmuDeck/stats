# Estadísticas de EmuDeck

Actualizado: 2026-10-10 02:54 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 44 | 120 | 120 | 143 |
| linux-arm | 8 | 20 | 20 | 24 |
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
| Instalaciones early | 107 | 107 | 134 |
| Con CloudSync | 182 | 182 | 251 |
| % con CloudSync | | | 187% |

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
| pcsx2 | 343 | 11 | 45 | 316 | 316 | 399 |
| esde | 294 | 26 | 68 | 288 | 288 | 388 |
| azahar | 304 | 37 | 45 | 301 | 301 | 386 |
| duckstation | 327 | 33 | 18 | 294 | 294 | 378 |
| ryujinx | 295 | 34 | 46 | 299 | 299 | 375 |
| cemu | 304 | 33 | 14 | 276 | 276 | 351 |
| rpcs3 | 294 | 31 | 18 | 269 | 269 | 343 |
| xenia | 269 | 27 | 30 | 259 | 259 | 326 |
| srm | 269 | 26 | 22 | 262 | 262 | 317 |
| shadps4 | 258 | 30 | 24 | 240 | 240 | 312 |
| vita3k | 269 | 27 | 9 | 233 | 233 | 305 |
| cloudsync | 172 | 10 | 81 | 192 | 192 | 263 |
| ra | 142 | 25 | 16 | 147 | 147 | 183 |
| dolphin | 132 | 24 | 20 | 141 | 141 | 176 |
| ppsspp | 122 | 21 | 28 | 135 | 135 | 171 |
| melonds | 113 | 17 | 15 | 113 | 113 | 145 |
| primehack | 108 | 19 | 14 | 113 | 113 | 141 |
| xemu | 106 | 17 | 16 | 109 | 109 | 139 |
| mgba | 111 | 13 | 10 | 109 | 109 | 134 |
| model2 | 102 | 19 | 2 | 99 | 99 | 123 |
| scummvm | 98 | 15 | 10 | 95 | 95 | 123 |
| supermodel | 98 | 19 | 4 | 97 | 97 | 121 |
| bigpemu | 73 | 3 | 1 | 59 | 59 | 77 |
| armsx2 | 25 | 35 | 0 | 48 | 48 | 60 |
| rmg | 29 | 10 | 0 | 32 | 32 | 39 |
| flycast | 30 | 2 | 3 | 28 | 28 | 35 |
| mame | 22 | 1 | 5 | 24 | 24 | 28 |
| eden | 10 | 0 | 0 | 2 | 2 | 10 |
| pegasus | 4 | 0 | 1 | 3 | 3 | 5 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 1 | 0 | 0 | 1 | 1 | 1 |
