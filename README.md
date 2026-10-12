# Estadísticas de EmuDeck

Actualizado: 2026-10-12 08:34 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 248 |
| linux-arm | 3 | 32 | 32 | 39 |
| windows | 10 | 44 | 44 | 55 |

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
| Instalaciones early | 206 | 206 | 245 |
| Con CloudSync | 295 | 295 | 368 |
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
| pcsx2 | 582 | 12 | 75 | 561 | 561 | 669 |
| azahar | 518 | 49 | 72 | 531 | 531 | 639 |
| duckstation | 565 | 47 | 23 | 530 | 530 | 635 |
| esde | 474 | 44 | 110 | 505 | 505 | 628 |
| ryujinx | 491 | 50 | 74 | 518 | 518 | 615 |
| rpcs3 | 519 | 46 | 23 | 487 | 487 | 588 |
| cemu | 517 | 48 | 16 | 487 | 487 | 581 |
| xenia | 467 | 42 | 52 | 466 | 466 | 561 |
| srm | 455 | 33 | 46 | 460 | 460 | 534 |
| shadps4 | 442 | 47 | 41 | 439 | 439 | 530 |
| vita3k | 463 | 42 | 11 | 425 | 425 | 516 |
| cloudsync | 266 | 13 | 107 | 311 | 311 | 386 |
| ppsspp | 220 | 34 | 53 | 258 | 258 | 307 |
| ra | 243 | 37 | 20 | 259 | 259 | 300 |
| dolphin | 237 | 36 | 24 | 254 | 254 | 297 |
| xemu | 200 | 27 | 21 | 210 | 210 | 248 |
| melonds | 200 | 26 | 17 | 204 | 204 | 243 |
| mgba | 192 | 21 | 17 | 197 | 197 | 230 |
| primehack | 177 | 28 | 21 | 190 | 190 | 226 |
| model2 | 170 | 34 | 2 | 176 | 176 | 206 |
| scummvm | 168 | 26 | 12 | 174 | 174 | 206 |
| supermodel | 167 | 34 | 5 | 176 | 176 | 206 |
| bigpemu | 140 | 3 | 2 | 121 | 121 | 145 |
| armsx2 | 42 | 50 | 0 | 76 | 76 | 92 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 39 | 14 | 0 | 45 | 45 | 53 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
