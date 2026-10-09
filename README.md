# Estadísticas de EmuDeck

Actualizado: 2026-10-09 22:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 12567 | 36400 |
| Linux ARM | 190 | 572 |
| Windows | 3258 | 9706 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **455**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07", "10-08"]
    y-axis "Arranques"
    line [11882, 11951, 12567]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07", "10-08"]
    y-axis "Arranques"
    line [222, 160, 190]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07", "10-08"]
    y-axis "Arranques"
    line [3321, 3127, 3258]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 42 | 76 | 76 | 139 |
| linux-arm | 11 | 12 | 12 | 23 |
| windows | 11 | 16 | 16 | 28 |

```mermaid
xychart-beta
    title "Instalaciones - linux"
    x-axis ["10-07", "10-08"]
    y-axis "Instalaciones"
    line [34, 42]
```

```mermaid
xychart-beta
    title "Instalaciones - linux-arm"
    x-axis ["10-07", "10-08"]
    y-axis "Instalaciones"
    line [1, 11]
```

```mermaid
xychart-beta
    title "Instalaciones - windows"
    x-axis ["10-07", "10-08"]
    y-axis "Instalaciones"
    line [5, 11]
```

```mermaid
xychart-beta
    title "Instalaciones acumuladas (todos los sistemas)"
    x-axis ["10-06", "10-07", "10-08"]
    y-axis "Total"
    line [31, 71, 135]
```

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 76 | 12 | 16 | 104 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 68 | 68 | 129 |
| Con CloudSync | 127 | 127 | 245 |
| % con CloudSync | | | 190% |

Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.

```mermaid
xychart-beta
    title "Canal early: instalaciones y CloudSync"
    x-axis ["10-07", "10-08"]
    y-axis "Instalaciones"
    line [29, 39]
    line [58, 69]
```

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 331 | 11 | 42 | 219 | 219 | 384 |
| esde | 288 | 23 | 65 | 189 | 189 | 376 |
| azahar | 294 | 34 | 41 | 199 | 199 | 369 |
| duckstation | 315 | 30 | 16 | 197 | 197 | 361 |
| ryujinx | 282 | 33 | 44 | 193 | 193 | 359 |
| cemu | 291 | 30 | 13 | 176 | 176 | 334 |
| rpcs3 | 284 | 29 | 17 | 177 | 177 | 330 |
| xenia | 258 | 26 | 27 | 170 | 170 | 311 |
| srm | 259 | 23 | 22 | 178 | 178 | 304 |
| shadps4 | 250 | 28 | 22 | 163 | 163 | 300 |
| vita3k | 259 | 25 | 8 | 152 | 152 | 292 |
| cloudsync | 168 | 10 | 79 | 131 | 131 | 257 |
| ra | 134 | 24 | 15 | 95 | 95 | 173 |
| dolphin | 126 | 23 | 19 | 90 | 90 | 168 |
| ppsspp | 119 | 20 | 26 | 84 | 84 | 165 |
| melonds | 108 | 16 | 14 | 73 | 73 | 138 |
| primehack | 104 | 18 | 12 | 67 | 67 | 134 |
| xemu | 101 | 16 | 15 | 69 | 69 | 132 |
| mgba | 105 | 13 | 10 | 78 | 78 | 128 |
| model2 | 97 | 18 | 2 | 60 | 60 | 117 |
| scummvm | 93 | 14 | 9 | 54 | 54 | 116 |
| supermodel | 93 | 18 | 4 | 57 | 57 | 115 |
| bigpemu | 71 | 3 | 1 | 38 | 38 | 75 |
| armsx2 | 23 | 32 | 0 | 29 | 29 | 55 |
| rmg | 28 | 8 | 0 | 22 | 22 | 36 |
| flycast | 28 | 2 | 3 | 22 | 22 | 33 |
| mame | 22 | 1 | 5 | 17 | 17 | 28 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 4 | 0 | 1 | 1 | 1 | 5 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
