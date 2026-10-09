# Estadísticas de EmuDeck

Actualizado: 2026-10-09 19:39 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| pcsx2 | 314 | 11 | 42 | 219 | 219 | 367 |
| esde | 270 | 22 | 61 | 189 | 189 | 353 |
| azahar | 277 | 34 | 40 | 199 | 199 | 351 |
| duckstation | 297 | 29 | 16 | 197 | 197 | 342 |
| ryujinx | 267 | 32 | 43 | 193 | 193 | 342 |
| cemu | 275 | 29 | 13 | 176 | 176 | 317 |
| rpcs3 | 270 | 28 | 17 | 177 | 177 | 315 |
| xenia | 243 | 25 | 27 | 170 | 170 | 295 |
| srm | 244 | 23 | 22 | 178 | 178 | 289 |
| shadps4 | 235 | 27 | 21 | 163 | 163 | 283 |
| vita3k | 246 | 24 | 8 | 152 | 152 | 278 |
| cloudsync | 163 | 9 | 73 | 131 | 131 | 245 |
| ra | 124 | 23 | 15 | 95 | 95 | 162 |
| dolphin | 120 | 22 | 18 | 90 | 90 | 160 |
| ppsspp | 112 | 19 | 26 | 84 | 84 | 157 |
| melonds | 104 | 16 | 14 | 73 | 73 | 134 |
| primehack | 99 | 18 | 12 | 67 | 67 | 129 |
| xemu | 96 | 16 | 15 | 69 | 69 | 127 |
| mgba | 101 | 12 | 8 | 78 | 78 | 121 |
| model2 | 93 | 17 | 2 | 60 | 60 | 112 |
| scummvm | 89 | 13 | 9 | 54 | 54 | 111 |
| supermodel | 89 | 17 | 4 | 57 | 57 | 110 |
| bigpemu | 68 | 3 | 1 | 38 | 38 | 72 |
| armsx2 | 20 | 31 | 0 | 29 | 29 | 51 |
| rmg | 24 | 8 | 0 | 22 | 22 | 32 |
| flycast | 27 | 1 | 3 | 22 | 22 | 31 |
| mame | 20 | 1 | 5 | 17 | 17 | 26 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
