# Estadísticas de EmuDeck

Actualizado: 2026-10-09 04:46 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 104 |
| linux-arm | 11 | 12 | 12 | 17 |
| windows | 11 | 16 | 16 | 26 |

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
| Instalaciones early | 68 | 68 | 103 |
| Con CloudSync | 127 | 127 | 204 |
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
| pcsx2 | 260 | 11 | 39 | 219 | 219 | 310 |
| esde | 227 | 18 | 54 | 189 | 189 | 299 |
| azahar | 230 | 26 | 36 | 199 | 199 | 292 |
| duckstation | 248 | 22 | 15 | 197 | 197 | 285 |
| ryujinx | 221 | 25 | 38 | 193 | 193 | 284 |
| rpcs3 | 225 | 21 | 15 | 177 | 177 | 261 |
| cemu | 224 | 23 | 11 | 176 | 176 | 258 |
| xenia | 200 | 20 | 26 | 170 | 170 | 246 |
| shadps4 | 201 | 22 | 20 | 163 | 163 | 243 |
| srm | 201 | 18 | 17 | 178 | 178 | 236 |
| vita3k | 202 | 19 | 7 | 152 | 152 | 228 |
| cloudsync | 138 | 7 | 65 | 131 | 131 | 210 |
| ra | 102 | 18 | 14 | 95 | 95 | 134 |
| dolphin | 96 | 17 | 16 | 90 | 90 | 129 |
| ppsspp | 89 | 14 | 24 | 84 | 84 | 127 |
| melonds | 82 | 13 | 12 | 73 | 73 | 107 |
| mgba | 87 | 11 | 7 | 78 | 78 | 105 |
| xemu | 75 | 13 | 14 | 69 | 69 | 102 |
| primehack | 77 | 13 | 11 | 67 | 67 | 101 |
| model2 | 71 | 14 | 2 | 60 | 60 | 87 |
| scummvm | 68 | 10 | 8 | 54 | 54 | 86 |
| supermodel | 68 | 14 | 3 | 57 | 57 | 85 |
| bigpemu | 56 | 3 | 1 | 38 | 38 | 60 |
| armsx2 | 17 | 24 | 0 | 29 | 29 | 41 |
| flycast | 24 | 1 | 3 | 22 | 22 | 28 |
| rmg | 21 | 7 | 0 | 22 | 22 | 28 |
| mame | 17 | 0 | 5 | 17 | 17 | 22 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
