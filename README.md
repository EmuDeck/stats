# Estadísticas de EmuDeck

Actualizado: 2026-10-11 21:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 230 |
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
| Instalaciones early | 152 | 152 | 222 |
| Con CloudSync | 231 | 231 | 351 |
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
| pcsx2 | 540 | 12 | 68 | 441 | 441 | 620 |
| azahar | 479 | 44 | 67 | 422 | 422 | 590 |
| duckstation | 524 | 42 | 23 | 416 | 416 | 589 |
| esde | 444 | 39 | 105 | 415 | 415 | 588 |
| ryujinx | 457 | 45 | 67 | 412 | 412 | 569 |
| rpcs3 | 479 | 41 | 22 | 385 | 385 | 542 |
| cemu | 475 | 43 | 16 | 386 | 386 | 534 |
| xenia | 427 | 37 | 47 | 362 | 362 | 511 |
| srm | 424 | 31 | 43 | 365 | 365 | 498 |
| shadps4 | 414 | 42 | 36 | 341 | 341 | 492 |
| vita3k | 429 | 37 | 11 | 332 | 332 | 477 |
| cloudsync | 256 | 13 | 100 | 244 | 244 | 369 |
| ppsspp | 204 | 30 | 47 | 187 | 187 | 281 |
| ra | 227 | 33 | 20 | 196 | 196 | 280 |
| dolphin | 220 | 32 | 24 | 189 | 189 | 276 |
| xemu | 185 | 23 | 20 | 153 | 153 | 228 |
| melonds | 187 | 22 | 17 | 150 | 150 | 226 |
| mgba | 180 | 17 | 17 | 164 | 164 | 214 |
| primehack | 165 | 24 | 21 | 150 | 150 | 210 |
| scummvm | 158 | 23 | 12 | 129 | 129 | 193 |
| model2 | 160 | 30 | 2 | 133 | 133 | 192 |
| supermodel | 156 | 30 | 5 | 130 | 130 | 191 |
| bigpemu | 130 | 3 | 2 | 101 | 101 | 135 |
| armsx2 | 40 | 45 | 0 | 65 | 65 | 85 |
| flycast | 44 | 5 | 5 | 42 | 42 | 54 |
| rmg | 38 | 10 | 0 | 41 | 41 | 48 |
| mame | 32 | 1 | 8 | 32 | 32 | 41 |
| eden | 13 | 3 | 0 | 4 | 4 | 16 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| yuzu | 3 | 0 | 0 | 2 | 2 | 3 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
