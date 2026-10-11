# Estadísticas de EmuDeck

Actualizado: 2026-10-11 06:55 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 197 |
| linux-arm | 9 | 29 | 29 | 32 |
| windows | 12 | 34 | 34 | 46 |

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
| Instalaciones early | 152 | 152 | 192 |
| Con CloudSync | 231 | 231 | 307 |
| % con CloudSync | | | 160% |

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
| pcsx2 | 484 | 12 | 63 | 441 | 441 | 559 |
| azahar | 431 | 43 | 63 | 422 | 422 | 537 |
| esde | 399 | 38 | 94 | 415 | 415 | 531 |
| duckstation | 465 | 41 | 19 | 416 | 416 | 525 |
| ryujinx | 413 | 44 | 60 | 412 | 412 | 517 |
| rpcs3 | 426 | 40 | 21 | 385 | 385 | 487 |
| cemu | 425 | 42 | 15 | 386 | 386 | 482 |
| xenia | 379 | 36 | 44 | 362 | 362 | 459 |
| srm | 383 | 28 | 34 | 365 | 365 | 445 |
| shadps4 | 370 | 39 | 33 | 341 | 341 | 442 |
| vita3k | 378 | 36 | 11 | 332 | 332 | 425 |
| cloudsync | 220 | 13 | 89 | 244 | 244 | 322 |
| ra | 192 | 32 | 20 | 196 | 196 | 244 |
| ppsspp | 171 | 29 | 43 | 187 | 187 | 243 |
| dolphin | 186 | 31 | 22 | 189 | 189 | 239 |
| melonds | 160 | 21 | 17 | 150 | 150 | 198 |
| xemu | 155 | 22 | 20 | 153 | 153 | 197 |
| mgba | 165 | 17 | 13 | 164 | 164 | 195 |
| primehack | 143 | 23 | 21 | 150 | 150 | 187 |
| model2 | 139 | 27 | 2 | 133 | 133 | 168 |
| scummvm | 133 | 22 | 12 | 129 | 129 | 167 |
| supermodel | 134 | 27 | 5 | 130 | 130 | 166 |
| bigpemu | 121 | 3 | 2 | 101 | 101 | 126 |
| armsx2 | 34 | 44 | 0 | 65 | 65 | 78 |
| flycast | 39 | 5 | 4 | 42 | 42 | 48 |
| rmg | 35 | 10 | 0 | 41 | 41 | 45 |
| mame | 30 | 1 | 6 | 32 | 32 | 37 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
