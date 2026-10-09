# Estadísticas de EmuDeck

Actualizado: 2026-10-09 19:11 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 131 |
| linux-arm | 11 | 12 | 12 | 22 |
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
| Instalaciones early | 68 | 68 | 123 |
| Con CloudSync | 127 | 127 | 233 |
| % con CloudSync | | | 189% |

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
| pcsx2 | 313 | 11 | 41 | 219 | 219 | 365 |
| esde | 268 | 22 | 61 | 189 | 189 | 351 |
| azahar | 276 | 34 | 39 | 199 | 199 | 349 |
| duckstation | 296 | 29 | 16 | 197 | 197 | 341 |
| ryujinx | 266 | 32 | 43 | 193 | 193 | 341 |
| cemu | 274 | 29 | 12 | 176 | 176 | 315 |
| rpcs3 | 269 | 28 | 17 | 177 | 177 | 314 |
| xenia | 241 | 25 | 27 | 170 | 170 | 293 |
| srm | 244 | 23 | 21 | 178 | 178 | 288 |
| shadps4 | 233 | 27 | 21 | 163 | 163 | 281 |
| vita3k | 244 | 24 | 8 | 152 | 152 | 276 |
| cloudsync | 163 | 9 | 73 | 131 | 131 | 245 |
| ra | 124 | 23 | 15 | 95 | 95 | 162 |
| dolphin | 120 | 22 | 17 | 90 | 90 | 159 |
| ppsspp | 112 | 19 | 26 | 84 | 84 | 157 |
| melonds | 103 | 16 | 13 | 73 | 73 | 132 |
| primehack | 99 | 18 | 12 | 67 | 67 | 129 |
| xemu | 96 | 16 | 15 | 69 | 69 | 127 |
| mgba | 100 | 12 | 8 | 78 | 78 | 120 |
| model2 | 92 | 17 | 2 | 60 | 60 | 111 |
| scummvm | 89 | 13 | 9 | 54 | 54 | 111 |
| supermodel | 88 | 17 | 4 | 57 | 57 | 109 |
| bigpemu | 67 | 3 | 1 | 38 | 38 | 71 |
| armsx2 | 20 | 31 | 0 | 29 | 29 | 51 |
| rmg | 24 | 8 | 0 | 22 | 22 | 32 |
| flycast | 26 | 1 | 3 | 22 | 22 | 30 |
| mame | 20 | 1 | 5 | 17 | 17 | 26 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
