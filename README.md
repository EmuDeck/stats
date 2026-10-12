# Estadísticas de EmuDeck

Actualizado: 2026-10-12 17:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 256 |
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
| Instalaciones early | 206 | 206 | 251 |
| Con CloudSync | 295 | 295 | 377 |
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
| pcsx2 | 605 | 12 | 76 | 561 | 561 | 693 |
| azahar | 538 | 49 | 72 | 531 | 531 | 659 |
| duckstation | 589 | 47 | 23 | 530 | 530 | 659 |
| esde | 498 | 44 | 114 | 505 | 505 | 656 |
| ryujinx | 508 | 50 | 75 | 518 | 518 | 633 |
| rpcs3 | 538 | 46 | 23 | 487 | 487 | 607 |
| cemu | 540 | 48 | 17 | 487 | 487 | 605 |
| xenia | 487 | 42 | 52 | 466 | 466 | 581 |
| srm | 470 | 33 | 46 | 460 | 460 | 549 |
| shadps4 | 456 | 47 | 42 | 439 | 439 | 545 |
| vita3k | 483 | 42 | 11 | 425 | 425 | 536 |
| cloudsync | 272 | 13 | 110 | 311 | 311 | 395 |
| ppsspp | 226 | 34 | 53 | 258 | 258 | 313 |
| ra | 252 | 37 | 21 | 259 | 259 | 310 |
| dolphin | 245 | 36 | 24 | 254 | 254 | 305 |
| xemu | 207 | 27 | 21 | 210 | 210 | 255 |
| melonds | 207 | 26 | 17 | 204 | 204 | 250 |
| mgba | 200 | 21 | 18 | 197 | 197 | 239 |
| primehack | 184 | 28 | 21 | 190 | 190 | 233 |
| model2 | 175 | 34 | 2 | 176 | 176 | 211 |
| scummvm | 173 | 26 | 12 | 174 | 174 | 211 |
| supermodel | 172 | 34 | 5 | 176 | 176 | 211 |
| bigpemu | 144 | 3 | 2 | 121 | 121 | 149 |
| armsx2 | 44 | 50 | 0 | 76 | 76 | 94 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 40 | 14 | 0 | 45 | 45 | 54 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 13 | 3 | 0 | 8 | 8 | 16 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| ares | 2 | 1 | 0 | 2 | 2 | 3 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
