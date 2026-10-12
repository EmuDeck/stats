# Estadísticas de EmuDeck

Actualizado: 2026-10-12 20:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 262 |
| linux-arm | 3 | 32 | 32 | 39 |
| windows | 10 | 44 | 44 | 57 |

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
| Instalaciones early | 206 | 206 | 259 |
| Con CloudSync | 295 | 295 | 389 |
| % con CloudSync | | | 150% |

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
| pcsx2 | 619 | 12 | 78 | 561 | 561 | 709 |
| azahar | 553 | 49 | 74 | 531 | 531 | 676 |
| duckstation | 602 | 47 | 24 | 530 | 530 | 673 |
| esde | 509 | 44 | 117 | 505 | 505 | 670 |
| ryujinx | 521 | 50 | 76 | 518 | 518 | 647 |
| cemu | 558 | 48 | 17 | 487 | 487 | 623 |
| rpcs3 | 551 | 46 | 23 | 487 | 487 | 620 |
| xenia | 502 | 42 | 53 | 466 | 466 | 597 |
| srm | 484 | 33 | 46 | 460 | 460 | 563 |
| shadps4 | 467 | 47 | 43 | 439 | 439 | 557 |
| vita3k | 497 | 42 | 11 | 425 | 425 | 550 |
| cloudsync | 284 | 13 | 112 | 311 | 311 | 409 |
| ppsspp | 231 | 34 | 55 | 258 | 258 | 320 |
| ra | 258 | 37 | 22 | 259 | 259 | 317 |
| dolphin | 251 | 36 | 25 | 254 | 254 | 312 |
| xemu | 213 | 27 | 22 | 210 | 210 | 262 |
| melonds | 213 | 26 | 18 | 204 | 204 | 257 |
| mgba | 207 | 21 | 18 | 197 | 197 | 246 |
| primehack | 189 | 28 | 21 | 190 | 190 | 238 |
| supermodel | 178 | 34 | 5 | 176 | 176 | 217 |
| model2 | 179 | 34 | 2 | 176 | 176 | 215 |
| scummvm | 177 | 26 | 12 | 174 | 174 | 215 |
| bigpemu | 146 | 3 | 2 | 121 | 121 | 151 |
| armsx2 | 46 | 50 | 0 | 76 | 76 | 96 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 40 | 14 | 0 | 45 | 45 | 54 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 17 | 3 | 0 | 8 | 8 | 20 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 2 | 2 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
