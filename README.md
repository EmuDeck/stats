# Estadísticas de EmuDeck

Actualizado: 2026-10-12 18:47 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 61 | 216 | 216 | 257 |
| linux-arm | 3 | 32 | 32 | 39 |
| windows | 10 | 44 | 44 | 56 |

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
| Instalaciones early | 206 | 206 | 253 |
| Con CloudSync | 295 | 295 | 377 |
| % con CloudSync | | | 149% |

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
| pcsx2 | 608 | 12 | 77 | 561 | 561 | 697 |
| azahar | 543 | 49 | 73 | 531 | 531 | 665 |
| duckstation | 592 | 47 | 24 | 530 | 530 | 663 |
| esde | 502 | 44 | 115 | 505 | 505 | 661 |
| ryujinx | 513 | 50 | 76 | 518 | 518 | 639 |
| rpcs3 | 541 | 46 | 23 | 487 | 487 | 610 |
| cemu | 544 | 48 | 17 | 487 | 487 | 609 |
| xenia | 491 | 42 | 52 | 466 | 466 | 585 |
| srm | 473 | 33 | 46 | 460 | 460 | 552 |
| shadps4 | 459 | 47 | 42 | 439 | 439 | 548 |
| vita3k | 486 | 42 | 11 | 425 | 425 | 539 |
| cloudsync | 272 | 13 | 110 | 311 | 311 | 395 |
| ppsspp | 226 | 34 | 54 | 258 | 258 | 314 |
| ra | 253 | 37 | 22 | 259 | 259 | 312 |
| dolphin | 246 | 36 | 25 | 254 | 254 | 307 |
| xemu | 208 | 27 | 22 | 210 | 210 | 257 |
| melonds | 208 | 26 | 18 | 204 | 204 | 252 |
| mgba | 203 | 21 | 18 | 197 | 197 | 242 |
| primehack | 184 | 28 | 21 | 190 | 190 | 233 |
| model2 | 175 | 34 | 2 | 176 | 176 | 211 |
| scummvm | 173 | 26 | 12 | 174 | 174 | 211 |
| supermodel | 172 | 34 | 5 | 176 | 176 | 211 |
| bigpemu | 145 | 3 | 2 | 121 | 121 | 150 |
| armsx2 | 44 | 50 | 0 | 76 | 76 | 94 |
| flycast | 48 | 8 | 5 | 53 | 53 | 61 |
| rmg | 40 | 14 | 0 | 45 | 45 | 54 |
| mame | 33 | 1 | 8 | 38 | 38 | 42 |
| eden | 16 | 3 | 0 | 8 | 8 | 19 |
| pegasus | 5 | 0 | 1 | 4 | 4 | 6 |
| ares | 3 | 1 | 0 | 2 | 2 | 4 |
| yuzu | 4 | 0 | 0 | 4 | 4 | 4 |
| citron | 1 | 0 | 0 | 1 | 1 | 1 |
