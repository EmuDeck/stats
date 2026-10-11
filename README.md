# Estadísticas de EmuDeck

Actualizado: 2026-10-11 15:13 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 35 | 155 | 155 | 208 |
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
| Instalaciones early | 152 | 152 | 203 |
| Con CloudSync | 231 | 231 | 320 |
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
| pcsx2 | 509 | 12 | 65 | 441 | 441 | 586 |
| azahar | 451 | 43 | 65 | 422 | 422 | 559 |
| esde | 421 | 38 | 97 | 415 | 415 | 556 |
| duckstation | 492 | 41 | 22 | 416 | 416 | 555 |
| ryujinx | 433 | 44 | 63 | 412 | 412 | 540 |
| rpcs3 | 451 | 40 | 21 | 385 | 385 | 512 |
| cemu | 443 | 42 | 15 | 386 | 386 | 500 |
| xenia | 398 | 36 | 46 | 362 | 362 | 480 |
| srm | 403 | 30 | 35 | 365 | 365 | 468 |
| shadps4 | 385 | 41 | 33 | 341 | 341 | 459 |
| vita3k | 398 | 36 | 11 | 332 | 332 | 445 |
| cloudsync | 232 | 13 | 90 | 244 | 244 | 335 |
| ppsspp | 182 | 29 | 45 | 187 | 187 | 256 |
| ra | 204 | 32 | 20 | 196 | 196 | 256 |
| dolphin | 197 | 31 | 23 | 189 | 189 | 251 |
| melonds | 168 | 21 | 17 | 150 | 150 | 206 |
| xemu | 163 | 22 | 20 | 153 | 153 | 205 |
| mgba | 173 | 17 | 13 | 164 | 164 | 203 |
| primehack | 148 | 23 | 21 | 150 | 150 | 192 |
| model2 | 143 | 29 | 2 | 133 | 133 | 174 |
| supermodel | 139 | 29 | 5 | 130 | 130 | 173 |
| scummvm | 138 | 22 | 12 | 129 | 129 | 172 |
| bigpemu | 124 | 3 | 2 | 101 | 101 | 129 |
| armsx2 | 38 | 44 | 0 | 65 | 65 | 82 |
| flycast | 40 | 5 | 5 | 42 | 42 | 50 |
| rmg | 36 | 10 | 0 | 41 | 41 | 46 |
| mame | 30 | 1 | 7 | 32 | 32 | 38 |
| eden | 10 | 2 | 0 | 4 | 4 | 12 |
| pegasus | 5 | 0 | 1 | 3 | 3 | 6 |
| ares | 1 | 1 | 0 | 2 | 2 | 2 |
| yuzu | 2 | 0 | 0 | 2 | 2 | 2 |
| citron | 1 | 0 | 0 | 0 | 0 | 1 |
