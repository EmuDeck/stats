# Estadísticas de EmuDeck

Actualizado: 2026-10-12 06:38 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 244 |
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
| Instalaciones early | 206 | 206 | 241 |
| Con CloudSync | 295 | 295 | 365 |
| % con CloudSync | | | 151% |

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
| pcsx2 | 575 | 12 | 75 | 561 | 561 | 662 |
| azahar | 513 | 49 | 72 | 531 | 531 | 634 |
| duckstation | 560 | 47 | 23 | 530 | 530 | 630 |
| esde | 468 | 44 | 110 | 505 | 505 | 622 |
| ryujinx | 488 | 50 | 74 | 518 | 518 | 612 |
| rpcs3 | 512 | 46 | 23 | 487 | 487 | 581 |
| cemu | 512 | 48 | 16 | 487 | 487 | 576 |
| xenia | 461 | 42 | 52 | 466 | 466 | 555 |
| srm | 452 | 33 | 46 | 460 | 460 | 531 |
| shadps4 | 439 | 47 | 41 | 439 | 439 | 527 |
| vita3k | 457 | 42 | 11 | 425 | 425 | 510 |
| cloudsync | 263 | 13 | 107 | 311 | 311 | 383 |
| ppsspp | 217 | 34 | 53 | 258 | 258 | 304 |
| ra | 240 | 37 | 20 | 259 | 259 | 297 |
| dolphin | 233 | 36 | 24 | 254 | 254 | 293 |
| xemu | 197 | 27 | 21 | 210 | 210 | 245 |
| melonds | 197 | 26 | 17 | 204 | 204 | 240 |
| mgba | 190 | 21 | 17 | 197 | 197 | 228 |
| primehack | 174 | 28 | 21 | 190 | 190 | 223 |
| model2 | 169 | 34 | 2 | 176 | 176 | 205 |
| scummvm | 167 | 26 | 12 | 174 | 174 | 205 |
| supermodel | 166 | 34 | 5 | 176 | 176 | 205 |
| bigpemu | 139 | 3 | 2 | 121 | 121 | 144 |
| armsx2 | 42 | 50 | 0 | 76 | 76 | 92 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 39 | 14 | 0 | 45 | 45 | 53 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
