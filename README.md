# Estadísticas de EmuDeck

Actualizado: 2026-10-11 14:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 204 |
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
| Instalaciones early | 152 | 152 | 199 |
| Con CloudSync | 231 | 231 | 316 |
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
| pcsx2 | 504 | 12 | 65 | 441 | 441 | 581 |
| azahar | 447 | 43 | 65 | 422 | 422 | 555 |
| esde | 418 | 38 | 97 | 415 | 415 | 553 |
| duckstation | 487 | 41 | 22 | 416 | 416 | 550 |
| ryujinx | 429 | 44 | 61 | 412 | 412 | 534 |
| rpcs3 | 448 | 40 | 21 | 385 | 385 | 509 |
| cemu | 440 | 42 | 15 | 386 | 386 | 497 |
| xenia | 394 | 36 | 46 | 362 | 362 | 476 |
| srm | 399 | 30 | 34 | 365 | 365 | 463 |
| shadps4 | 383 | 41 | 33 | 341 | 341 | 457 |
| vita3k | 396 | 36 | 11 | 332 | 332 | 443 |
| cloudsync | 229 | 13 | 89 | 244 | 244 | 331 |
| ppsspp | 178 | 29 | 45 | 187 | 187 | 252 |
| ra | 200 | 32 | 20 | 196 | 196 | 252 |
| dolphin | 193 | 31 | 23 | 189 | 189 | 247 |
| melonds | 165 | 21 | 17 | 150 | 150 | 203 |
| xemu | 161 | 22 | 20 | 153 | 153 | 203 |
| mgba | 172 | 17 | 13 | 164 | 164 | 202 |
| primehack | 146 | 23 | 21 | 150 | 150 | 190 |
| model2 | 142 | 29 | 2 | 133 | 133 | 173 |
| supermodel | 138 | 29 | 5 | 130 | 130 | 172 |
| scummvm | 137 | 22 | 12 | 129 | 129 | 171 |
| bigpemu | 124 | 3 | 2 | 101 | 101 | 129 |
| armsx2 | 38 | 44 | 0 | 65 | 65 | 82 |
| flycast | 40 | 5 | 4 | 42 | 42 | 49 |
| rmg | 36 | 10 | 0 | 41 | 41 | 46 |
| mame | 30 | 1 | 7 | 32 | 32 | 38 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
