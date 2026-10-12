# Estadísticas de EmuDeck

Actualizado: 2026-10-12 05:48 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 242 |
| linux-arm | 3 | 32 | 32 | 38 |
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
| Instalaciones early | 206 | 206 | 236 |
| Con CloudSync | 295 | 295 | 361 |
| % con CloudSync | | | 153% |

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
| pcsx2 | 573 | 12 | 72 | 561 | 561 | 657 |
| azahar | 511 | 48 | 69 | 531 | 531 | 628 |
| duckstation | 558 | 46 | 23 | 530 | 530 | 627 |
| esde | 466 | 43 | 110 | 505 | 505 | 619 |
| ryujinx | 486 | 49 | 74 | 518 | 518 | 609 |
| rpcs3 | 510 | 45 | 23 | 487 | 487 | 578 |
| cemu | 509 | 47 | 16 | 487 | 487 | 572 |
| xenia | 457 | 41 | 49 | 466 | 466 | 547 |
| srm | 451 | 33 | 43 | 460 | 460 | 527 |
| shadps4 | 437 | 46 | 37 | 439 | 439 | 520 |
| vita3k | 456 | 41 | 11 | 425 | 425 | 508 |
| cloudsync | 263 | 13 | 103 | 311 | 311 | 379 |
| ppsspp | 215 | 33 | 50 | 258 | 258 | 298 |
| ra | 239 | 36 | 20 | 259 | 259 | 295 |
| dolphin | 231 | 35 | 24 | 254 | 254 | 290 |
| xemu | 196 | 26 | 21 | 210 | 210 | 243 |
| melonds | 196 | 25 | 17 | 204 | 204 | 238 |
| mgba | 190 | 20 | 17 | 197 | 197 | 227 |
| primehack | 173 | 27 | 21 | 190 | 190 | 221 |
| model2 | 168 | 33 | 2 | 176 | 176 | 203 |
| scummvm | 166 | 25 | 12 | 174 | 174 | 203 |
| supermodel | 165 | 33 | 5 | 176 | 176 | 203 |
| bigpemu | 138 | 3 | 2 | 121 | 121 | 143 |
| armsx2 | 42 | 49 | 0 | 76 | 76 | 91 |
| flycast | 48 | 7 | 5 | 53 | 53 | 60 |
| rmg | 39 | 13 | 0 | 45 | 45 | 52 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
