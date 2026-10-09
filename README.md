# Estadísticas de EmuDeck

Actualizado: 2026-10-09 13:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 116 |
| linux-arm | 11 | 12 | 12 | 18 |
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
| Instalaciones early | 68 | 68 | 111 |
| Con CloudSync | 127 | 127 | 219 |
| % con CloudSync | | | 197% |

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
| pcsx2 | 282 | 11 | 41 | 219 | 219 | 334 |
| esde | 246 | 19 | 56 | 189 | 189 | 321 |
| azahar | 249 | 28 | 38 | 199 | 199 | 315 |
| ryujinx | 240 | 26 | 40 | 193 | 193 | 306 |
| duckstation | 266 | 23 | 16 | 197 | 197 | 305 |
| rpcs3 | 246 | 22 | 16 | 177 | 177 | 284 |
| cemu | 246 | 24 | 12 | 176 | 176 | 282 |
| xenia | 220 | 20 | 27 | 170 | 170 | 267 |
| shadps4 | 216 | 22 | 21 | 163 | 163 | 259 |
| srm | 218 | 19 | 20 | 178 | 178 | 257 |
| vita3k | 220 | 19 | 8 | 152 | 152 | 247 |
| cloudsync | 148 | 8 | 72 | 131 | 131 | 228 |
| ra | 111 | 19 | 15 | 95 | 95 | 145 |
| dolphin | 106 | 18 | 17 | 90 | 90 | 141 |
| ppsspp | 98 | 15 | 26 | 84 | 84 | 139 |
| melonds | 92 | 13 | 13 | 73 | 73 | 118 |
| mgba | 93 | 12 | 8 | 78 | 78 | 113 |
| primehack | 87 | 14 | 12 | 67 | 67 | 113 |
| xemu | 84 | 13 | 15 | 69 | 69 | 112 |
| model2 | 80 | 14 | 2 | 60 | 60 | 96 |
| scummvm | 77 | 10 | 9 | 54 | 54 | 96 |
| supermodel | 78 | 14 | 4 | 57 | 57 | 96 |
| bigpemu | 60 | 3 | 1 | 38 | 38 | 64 |
| armsx2 | 18 | 25 | 0 | 29 | 29 | 43 |
| flycast | 25 | 1 | 3 | 22 | 22 | 29 |
| rmg | 22 | 7 | 0 | 22 | 22 | 29 |
| mame | 18 | 0 | 5 | 17 | 17 | 23 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
