# Estadísticas de EmuDeck

Actualizado: 2026-10-11 11:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 15258 | 64741 |
| Linux ARM | 222 | 971 |
| Windows | 4198 | 17412 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **968**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 35 | 155 | 155 | 200 |
| linux-arm | 9 | 29 | 29 | 32 |
| windows | 12 | 34 | 34 | 47 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10"]
    y-axis "Total"
    line [31, 71, 135, 193, 249]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 155 | 29 | 34 | 218 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 152 | 152 | 193 |
| Con CloudSync | 231 | 231 | 312 |
| % con CloudSync | | | 162% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45]
    line [58, 69, 55, 49]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 495 | 12 | 64 | 441 | 441 | 571 |
| azahar | 441 | 43 | 64 | 422 | 422 | 548 |
| esde | 409 | 38 | 96 | 415 | 415 | 543 |
| duckstation | 476 | 41 | 22 | 416 | 416 | 539 |
| ryujinx | 422 | 44 | 60 | 412 | 412 | 526 |
| rpcs3 | 437 | 40 | 21 | 385 | 385 | 498 |
| cemu | 435 | 42 | 15 | 386 | 386 | 492 |
| xenia | 387 | 36 | 45 | 362 | 362 | 468 |
| srm | 393 | 28 | 34 | 365 | 365 | 455 |
| shadps4 | 378 | 39 | 33 | 341 | 341 | 450 |
| vita3k | 387 | 36 | 11 | 332 | 332 | 434 |
| cloudsync | 225 | 13 | 89 | 244 | 244 | 327 |
| ppsspp | 174 | 29 | 44 | 187 | 187 | 247 |
| ra | 195 | 32 | 20 | 196 | 196 | 247 |
| dolphin | 189 | 31 | 23 | 189 | 189 | 243 |
| melonds | 162 | 21 | 17 | 150 | 150 | 200 |
| mgba | 169 | 17 | 13 | 164 | 164 | 199 |
| xemu | 157 | 22 | 20 | 153 | 153 | 199 |
| primehack | 145 | 23 | 21 | 150 | 150 | 189 |
| model2 | 140 | 27 | 2 | 133 | 133 | 169 |
| scummvm | 134 | 22 | 12 | 129 | 129 | 168 |
| supermodel | 135 | 27 | 5 | 130 | 130 | 167 |
| bigpemu | 122 | 3 | 2 | 101 | 101 | 127 |
| armsx2 | 35 | 44 | 0 | 65 | 65 | 79 |
| flycast | 39 | 5 | 4 | 42 | 42 | 48 |
| rmg | 35 | 10 | 0 | 41 | 41 | 45 |
| mame | 30 | 1 | 7 | 32 | 32 | 38 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
