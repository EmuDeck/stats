# Estadísticas de EmuDeck

Actualizado: 2026-10-09 11:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 113 |
| linux-arm | 11 | 12 | 12 | 18 |
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
| Instalaciones early | 68 | 68 | 108 |
| Con CloudSync | 127 | 127 | 207 |
| % con CloudSync | | | 192% |

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
| pcsx2 | 275 | 11 | 40 | 219 | 219 | 326 |
| esde | 240 | 19 | 55 | 189 | 189 | 314 |
| azahar | 244 | 28 | 37 | 199 | 199 | 309 |
| duckstation | 260 | 23 | 16 | 197 | 197 | 299 |
| ryujinx | 234 | 26 | 39 | 193 | 193 | 299 |
| rpcs3 | 241 | 22 | 16 | 177 | 177 | 279 |
| cemu | 240 | 24 | 12 | 176 | 176 | 276 |
| xenia | 214 | 20 | 27 | 170 | 170 | 261 |
| shadps4 | 213 | 22 | 21 | 163 | 163 | 256 |
| srm | 213 | 19 | 17 | 178 | 178 | 249 |
| vita3k | 215 | 19 | 8 | 152 | 152 | 242 |
| cloudsync | 142 | 7 | 67 | 131 | 131 | 216 |
| ra | 109 | 19 | 15 | 95 | 95 | 143 |
| dolphin | 104 | 18 | 17 | 90 | 90 | 139 |
| ppsspp | 96 | 15 | 25 | 84 | 84 | 136 |
| melonds | 89 | 13 | 13 | 73 | 73 | 115 |
| mgba | 92 | 12 | 8 | 78 | 78 | 112 |
| primehack | 85 | 14 | 12 | 67 | 67 | 111 |
| xemu | 82 | 13 | 15 | 69 | 69 | 110 |
| model2 | 78 | 14 | 2 | 60 | 60 | 94 |
| scummvm | 75 | 10 | 9 | 54 | 54 | 94 |
| supermodel | 76 | 14 | 4 | 57 | 57 | 94 |
| bigpemu | 60 | 3 | 1 | 38 | 38 | 64 |
| armsx2 | 18 | 25 | 0 | 29 | 29 | 43 |
| flycast | 25 | 1 | 3 | 22 | 22 | 29 |
| rmg | 22 | 7 | 0 | 22 | 22 | 29 |
| mame | 18 | 0 | 5 | 17 | 17 | 23 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
