# Estadísticas de EmuDeck

Actualizado: 2026-10-11 23:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 237 |
| linux-arm | 9 | 29 | 29 | 35 |
| windows | 12 | 34 | 34 | 51 |

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
| Instalaciones early | 152 | 152 | 229 |
| Con CloudSync | 231 | 231 | 359 |
| % con CloudSync | | | 157% |

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
| pcsx2 | 552 | 12 | 70 | 441 | 441 | 634 |
| azahar | 492 | 44 | 69 | 422 | 422 | 605 |
| duckstation | 537 | 42 | 23 | 416 | 416 | 602 |
| esde | 450 | 39 | 107 | 415 | 415 | 596 |
| ryujinx | 468 | 45 | 71 | 412 | 412 | 584 |
| rpcs3 | 490 | 41 | 22 | 385 | 385 | 553 |
| cemu | 490 | 43 | 16 | 386 | 386 | 549 |
| xenia | 439 | 37 | 48 | 362 | 362 | 524 |
| srm | 433 | 31 | 43 | 365 | 365 | 507 |
| shadps4 | 423 | 42 | 37 | 341 | 341 | 502 |
| vita3k | 439 | 37 | 11 | 332 | 332 | 487 |
| cloudsync | 261 | 13 | 103 | 244 | 244 | 377 |
| ppsspp | 211 | 30 | 48 | 187 | 187 | 289 |
| ra | 234 | 33 | 20 | 196 | 196 | 287 |
| dolphin | 227 | 32 | 24 | 189 | 189 | 283 |
| xemu | 192 | 23 | 20 | 153 | 153 | 235 |
| melonds | 192 | 22 | 17 | 150 | 150 | 231 |
| mgba | 184 | 17 | 17 | 164 | 164 | 218 |
| primehack | 169 | 24 | 21 | 150 | 150 | 214 |
| scummvm | 162 | 23 | 12 | 129 | 129 | 197 |
| model2 | 164 | 30 | 2 | 133 | 133 | 196 |
| supermodel | 161 | 30 | 5 | 130 | 130 | 196 |
| bigpemu | 134 | 3 | 2 | 101 | 101 | 139 |
| armsx2 | 40 | 45 | 0 | 65 | 65 | 85 |
| flycast | 48 | 5 | 5 | 42 | 42 | 58 |
| rmg | 39 | 10 | 0 | 41 | 41 | 49 |
| mame | 33 | 1 | 8 | 32 | 32 | 42 |
| eden | 13 | 3 | 0 | 4 | 4 | 16 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| yuzu | 4 | 0 | 0 | 2 | 2 | 4 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
