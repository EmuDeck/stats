# Estadísticas de EmuDeck

Actualizado: 2026-10-11 17:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 212 |
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
| Instalaciones early | 152 | 152 | 205 |
| Con CloudSync | 231 | 231 | 325 |
| % con CloudSync | | | 159% |

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
| pcsx2 | 516 | 12 | 65 | 441 | 441 | 593 |
| azahar | 458 | 43 | 66 | 422 | 422 | 567 |
| duckstation | 500 | 41 | 22 | 416 | 416 | 563 |
| esde | 426 | 38 | 97 | 415 | 415 | 561 |
| ryujinx | 438 | 44 | 64 | 412 | 412 | 546 |
| rpcs3 | 457 | 40 | 21 | 385 | 385 | 518 |
| cemu | 451 | 42 | 15 | 386 | 386 | 508 |
| xenia | 405 | 36 | 46 | 362 | 362 | 487 |
| srm | 408 | 30 | 35 | 365 | 365 | 473 |
| shadps4 | 391 | 41 | 33 | 341 | 341 | 465 |
| vita3k | 404 | 36 | 11 | 332 | 332 | 451 |
| cloudsync | 237 | 13 | 92 | 244 | 244 | 342 |
| ppsspp | 186 | 29 | 46 | 187 | 187 | 261 |
| ra | 208 | 32 | 20 | 196 | 196 | 260 |
| dolphin | 201 | 31 | 23 | 189 | 189 | 255 |
| melonds | 172 | 21 | 17 | 150 | 150 | 210 |
| xemu | 168 | 22 | 20 | 153 | 153 | 210 |
| mgba | 175 | 17 | 13 | 164 | 164 | 205 |
| primehack | 151 | 23 | 21 | 150 | 150 | 195 |
| model2 | 146 | 29 | 2 | 133 | 133 | 177 |
| scummvm | 142 | 22 | 12 | 129 | 129 | 176 |
| supermodel | 142 | 29 | 5 | 130 | 130 | 176 |
| bigpemu | 125 | 3 | 2 | 101 | 101 | 130 |
| armsx2 | 38 | 44 | 0 | 65 | 65 | 82 |
| flycast | 40 | 5 | 5 | 42 | 42 | 50 |
| rmg | 36 | 10 | 0 | 41 | 41 | 46 |
| mame | 30 | 1 | 8 | 32 | 32 | 39 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
