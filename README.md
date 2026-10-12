# Estadísticas de EmuDeck

Actualizado: 2026-10-12 00:47 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 237 |
| linux-arm | 3 | 32 | 32 | 35 |
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
| Instalaciones early | 206 | 206 | 230 |
| Con CloudSync | 295 | 295 | 359 |
| % con CloudSync | | | 156% |

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
| pcsx2 | 557 | 12 | 71 | 561 | 561 | 640 |
| azahar | 496 | 44 | 69 | 531 | 531 | 609 |
| duckstation | 542 | 42 | 23 | 530 | 530 | 607 |
| esde | 454 | 39 | 110 | 505 | 505 | 603 |
| ryujinx | 470 | 45 | 72 | 518 | 518 | 587 |
| rpcs3 | 495 | 41 | 22 | 487 | 487 | 558 |
| cemu | 494 | 43 | 16 | 487 | 487 | 553 |
| xenia | 443 | 37 | 49 | 466 | 466 | 529 |
| srm | 436 | 31 | 43 | 460 | 460 | 510 |
| shadps4 | 424 | 42 | 37 | 439 | 439 | 503 |
| vita3k | 441 | 37 | 11 | 425 | 425 | 489 |
| cloudsync | 261 | 13 | 103 | 311 | 311 | 377 |
| ppsspp | 211 | 30 | 49 | 258 | 258 | 290 |
| ra | 234 | 33 | 20 | 259 | 259 | 287 |
| dolphin | 227 | 32 | 24 | 254 | 254 | 283 |
| xemu | 192 | 23 | 20 | 210 | 210 | 235 |
| melonds | 192 | 22 | 17 | 204 | 204 | 231 |
| mgba | 185 | 17 | 17 | 197 | 197 | 219 |
| primehack | 169 | 24 | 21 | 190 | 190 | 214 |
| scummvm | 162 | 23 | 12 | 174 | 174 | 197 |
| model2 | 164 | 30 | 2 | 176 | 176 | 196 |
| supermodel | 161 | 30 | 5 | 176 | 176 | 196 |
| bigpemu | 134 | 3 | 2 | 121 | 121 | 139 |
| armsx2 | 40 | 45 | 0 | 76 | 76 | 85 |
| flycast | 48 | 5 | 5 | 53 | 53 | 58 |
| rmg | 39 | 10 | 0 | 45 | 45 | 49 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
