# Estadísticas de EmuDeck

Actualizado: 2026-10-11 17:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 217 |
| linux-arm | 9 | 29 | 29 | 34 |
| windows | 12 | 34 | 34 | 48 |

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
| Instalaciones early | 152 | 152 | 207 |
| Con CloudSync | 231 | 231 | 328 |
| % con CloudSync | | | 158% |

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
| pcsx2 | 523 | 12 | 65 | 441 | 441 | 600 |
| azahar | 464 | 43 | 66 | 422 | 422 | 573 |
| duckstation | 507 | 41 | 22 | 416 | 416 | 570 |
| esde | 431 | 38 | 97 | 415 | 415 | 566 |
| ryujinx | 442 | 44 | 64 | 412 | 412 | 550 |
| rpcs3 | 463 | 40 | 21 | 385 | 385 | 524 |
| cemu | 458 | 42 | 15 | 386 | 386 | 515 |
| xenia | 411 | 36 | 46 | 362 | 362 | 493 |
| srm | 412 | 30 | 35 | 365 | 365 | 477 |
| shadps4 | 396 | 41 | 33 | 341 | 341 | 470 |
| vita3k | 410 | 36 | 11 | 332 | 332 | 457 |
| cloudsync | 240 | 13 | 92 | 244 | 244 | 345 |
| ppsspp | 191 | 29 | 46 | 187 | 187 | 266 |
| ra | 213 | 32 | 20 | 196 | 196 | 265 |
| dolphin | 207 | 31 | 23 | 189 | 189 | 261 |
| xemu | 173 | 22 | 20 | 153 | 153 | 215 |
| melonds | 176 | 21 | 17 | 150 | 150 | 214 |
| mgba | 177 | 17 | 13 | 164 | 164 | 207 |
| primehack | 153 | 23 | 21 | 150 | 150 | 197 |
| scummvm | 146 | 22 | 12 | 129 | 129 | 180 |
| model2 | 148 | 29 | 2 | 133 | 133 | 179 |
| supermodel | 144 | 29 | 5 | 130 | 130 | 178 |
| bigpemu | 126 | 3 | 2 | 101 | 101 | 131 |
| armsx2 | 39 | 44 | 0 | 65 | 65 | 83 |
| flycast | 41 | 5 | 5 | 42 | 42 | 51 |
| rmg | 37 | 10 | 0 | 41 | 41 | 47 |
| mame | 31 | 1 | 8 | 32 | 32 | 40 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| yuzu | 3 | 0 | 0 | 2 | 2 | 3 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
