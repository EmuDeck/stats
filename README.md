# Estadísticas de EmuDeck

Actualizado: 2026-10-09 18:45 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 129 |
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
| Instalaciones early | 68 | 68 | 122 |
| Con CloudSync | 127 | 127 | 232 |
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
| pcsx2 | 307 | 11 | 41 | 219 | 219 | 359 |
| esde | 263 | 21 | 61 | 189 | 189 | 345 |
| azahar | 270 | 34 | 39 | 199 | 199 | 343 |
| ryujinx | 261 | 32 | 43 | 193 | 193 | 336 |
| duckstation | 290 | 29 | 16 | 197 | 197 | 335 |
| rpcs3 | 264 | 28 | 17 | 177 | 177 | 309 |
| cemu | 267 | 29 | 12 | 176 | 176 | 308 |
| xenia | 237 | 25 | 27 | 170 | 170 | 289 |
| srm | 237 | 23 | 21 | 178 | 178 | 281 |
| shadps4 | 230 | 27 | 21 | 163 | 163 | 278 |
| vita3k | 240 | 24 | 8 | 152 | 152 | 272 |
| cloudsync | 162 | 9 | 73 | 131 | 131 | 244 |
| ra | 122 | 23 | 15 | 95 | 95 | 160 |
| dolphin | 118 | 22 | 17 | 90 | 90 | 157 |
| ppsspp | 110 | 19 | 26 | 84 | 84 | 155 |
| melonds | 102 | 16 | 13 | 73 | 73 | 131 |
| primehack | 97 | 18 | 12 | 67 | 67 | 127 |
| xemu | 94 | 16 | 15 | 69 | 69 | 125 |
| mgba | 98 | 12 | 8 | 78 | 78 | 118 |
| model2 | 91 | 17 | 2 | 60 | 60 | 110 |
| scummvm | 87 | 13 | 9 | 54 | 54 | 109 |
| supermodel | 87 | 17 | 4 | 57 | 57 | 108 |
| bigpemu | 65 | 3 | 1 | 38 | 38 | 69 |
| armsx2 | 18 | 31 | 0 | 29 | 29 | 49 |
| rmg | 23 | 8 | 0 | 22 | 22 | 31 |
| flycast | 26 | 1 | 3 | 22 | 22 | 30 |
| mame | 19 | 1 | 5 | 17 | 17 | 25 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
