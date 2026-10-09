# Estadísticas de EmuDeck

Actualizado: 2026-10-09 06:26 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 107 |
| linux-arm | 11 | 12 | 12 | 17 |
| windows | 11 | 16 | 16 | 27 |

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
| Instalaciones early | 68 | 68 | 104 |
| Con CloudSync | 127 | 127 | 206 |
| % con CloudSync | | | 198% |

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
| pcsx2 | 266 | 11 | 40 | 219 | 219 | 317 |
| esde | 233 | 18 | 55 | 189 | 189 | 306 |
| azahar | 235 | 26 | 37 | 199 | 199 | 298 |
| duckstation | 251 | 22 | 16 | 197 | 197 | 289 |
| ryujinx | 225 | 25 | 39 | 193 | 193 | 289 |
| rpcs3 | 231 | 21 | 16 | 177 | 177 | 268 |
| cemu | 232 | 23 | 12 | 176 | 176 | 267 |
| xenia | 205 | 20 | 27 | 170 | 170 | 252 |
| shadps4 | 204 | 22 | 21 | 163 | 163 | 247 |
| srm | 207 | 18 | 17 | 178 | 178 | 242 |
| vita3k | 207 | 19 | 8 | 152 | 152 | 234 |
| cloudsync | 141 | 7 | 66 | 131 | 131 | 214 |
| ra | 103 | 18 | 15 | 95 | 95 | 136 |
| dolphin | 98 | 17 | 17 | 90 | 90 | 132 |
| ppsspp | 90 | 14 | 25 | 84 | 84 | 129 |
| melonds | 83 | 13 | 13 | 73 | 73 | 109 |
| mgba | 90 | 11 | 7 | 78 | 78 | 108 |
| primehack | 79 | 13 | 12 | 67 | 67 | 104 |
| xemu | 76 | 13 | 15 | 69 | 69 | 104 |
| model2 | 72 | 14 | 2 | 60 | 60 | 88 |
| scummvm | 69 | 10 | 9 | 54 | 54 | 88 |
| supermodel | 69 | 14 | 3 | 57 | 57 | 86 |
| bigpemu | 57 | 3 | 1 | 38 | 38 | 61 |
| armsx2 | 17 | 24 | 0 | 29 | 29 | 41 |
| flycast | 25 | 1 | 3 | 22 | 22 | 29 |
| rmg | 22 | 7 | 0 | 22 | 22 | 29 |
| mame | 18 | 0 | 5 | 17 | 17 | 23 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
