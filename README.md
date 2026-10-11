# Estadísticas de EmuDeck

Actualizado: 2026-10-11 20:15 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 225 |
| linux-arm | 9 | 29 | 29 | 35 |
| windows | 12 | 34 | 34 | 50 |

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
| Instalaciones early | 152 | 152 | 217 |
| Con CloudSync | 231 | 231 | 339 |
| % con CloudSync | | | 156% |

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
| pcsx2 | 532 | 12 | 67 | 441 | 441 | 611 |
| azahar | 473 | 44 | 67 | 422 | 422 | 584 |
| duckstation | 516 | 42 | 23 | 416 | 416 | 581 |
| esde | 438 | 39 | 103 | 415 | 415 | 580 |
| ryujinx | 450 | 45 | 65 | 412 | 412 | 560 |
| rpcs3 | 472 | 41 | 22 | 385 | 385 | 535 |
| cemu | 468 | 43 | 16 | 386 | 386 | 527 |
| xenia | 420 | 37 | 47 | 362 | 362 | 504 |
| srm | 416 | 31 | 43 | 365 | 365 | 490 |
| shadps4 | 405 | 42 | 34 | 341 | 341 | 481 |
| vita3k | 420 | 37 | 11 | 332 | 332 | 468 |
| cloudsync | 247 | 13 | 97 | 244 | 244 | 357 |
| ppsspp | 199 | 30 | 47 | 187 | 187 | 276 |
| ra | 222 | 33 | 20 | 196 | 196 | 275 |
| dolphin | 215 | 32 | 24 | 189 | 189 | 271 |
| xemu | 181 | 23 | 20 | 153 | 153 | 224 |
| melonds | 183 | 22 | 17 | 150 | 150 | 222 |
| mgba | 178 | 17 | 16 | 164 | 164 | 211 |
| primehack | 161 | 24 | 21 | 150 | 150 | 206 |
| scummvm | 154 | 23 | 12 | 129 | 129 | 189 |
| model2 | 155 | 30 | 2 | 133 | 133 | 187 |
| supermodel | 151 | 30 | 5 | 130 | 130 | 186 |
| bigpemu | 127 | 3 | 2 | 101 | 101 | 132 |
| armsx2 | 39 | 45 | 0 | 65 | 65 | 84 |
| flycast | 43 | 5 | 5 | 42 | 42 | 53 |
| rmg | 37 | 10 | 0 | 41 | 41 | 47 |
| mame | 31 | 1 | 8 | 32 | 32 | 40 |
| eden | 12 | 3 | 0 | 4 | 4 | 15 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| yuzu | 3 | 0 | 0 | 2 | 2 | 3 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
