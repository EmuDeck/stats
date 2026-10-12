# Estadísticas de EmuDeck

Actualizado: 2026-10-12 02:36 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 16125 | 80866 |
| Linux ARM | 195 | 1166 |
| Windows | 4407 | 21819 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **1216**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [11882, 11951, 12567, 13083, 15258, 16125]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [222, 160, 190, 177, 222, 195]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Arranques"
    line [3321, 3127, 3258, 3508, 4198, 4407]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 61 | 216 | 216 | 240 |
| linux-arm | 3 | 32 | 32 | 37 |
| windows | 10 | 44 | 44 | 52 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [34, 42, 44, 35, 61]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [1, 11, 8, 9, 3]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [5, 11, 6, 12, 10]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Total"
    line [31, 71, 135, 193, 249, 323]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 216 | 32 | 44 | 292 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 206 | 206 | 235 |
| Con CloudSync | 295 | 295 | 361 |
| % con CloudSync | | | 154% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08", "10-09", "10-10", "10-11"]
    y-axis "Instalaciones"
    line [29, 39, 39, 45, 54]
    line [58, 69, 55, 49, 64]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 565 | 12 | 71 | 561 | 561 | 648 |
| azahar | 504 | 47 | 69 | 531 | 531 | 620 |
| duckstation | 550 | 45 | 23 | 530 | 530 | 618 |
| esde | 459 | 42 | 110 | 505 | 505 | 611 |
| ryujinx | 479 | 48 | 72 | 518 | 518 | 599 |
| rpcs3 | 503 | 44 | 22 | 487 | 487 | 569 |
| cemu | 503 | 46 | 16 | 487 | 487 | 565 |
| xenia | 450 | 40 | 49 | 466 | 466 | 539 |
| srm | 444 | 33 | 43 | 460 | 460 | 520 |
| shadps4 | 431 | 45 | 37 | 439 | 439 | 513 |
| vita3k | 449 | 40 | 11 | 425 | 425 | 500 |
| cloudsync | 263 | 13 | 103 | 311 | 311 | 379 |
| ppsspp | 214 | 32 | 49 | 258 | 258 | 295 |
| ra | 237 | 35 | 20 | 259 | 259 | 292 |
| dolphin | 230 | 34 | 24 | 254 | 254 | 288 |
| xemu | 195 | 25 | 20 | 210 | 210 | 240 |
| melonds | 195 | 24 | 17 | 204 | 204 | 236 |
| mgba | 188 | 19 | 17 | 197 | 197 | 224 |
| primehack | 172 | 26 | 21 | 190 | 190 | 219 |
| model2 | 167 | 32 | 2 | 176 | 176 | 201 |
| scummvm | 165 | 24 | 12 | 174 | 174 | 201 |
| supermodel | 164 | 32 | 5 | 176 | 176 | 201 |
| bigpemu | 136 | 3 | 2 | 121 | 121 | 141 |
| armsx2 | 42 | 48 | 0 | 76 | 76 | 90 |
| flycast | 48 | 6 | 5 | 53 | 53 | 59 |
| rmg | 39 | 12 | 0 | 45 | 45 | 51 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
