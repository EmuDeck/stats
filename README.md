# Estadísticas de EmuDeck

Actualizado: 2026-10-09 20:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 136 |
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
| Instalaciones early | 68 | 68 | 127 |
| Con CloudSync | 127 | 127 | 238 |
| % con CloudSync | | | 187% |

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
| pcsx2 | 326 | 11 | 42 | 219 | 219 | 379 |
| azahar | 289 | 34 | 40 | 199 | 199 | 363 |
| esde | 280 | 22 | 61 | 189 | 189 | 363 |
| duckstation | 309 | 29 | 16 | 197 | 197 | 354 |
| ryujinx | 277 | 32 | 43 | 193 | 193 | 352 |
| cemu | 286 | 29 | 13 | 176 | 176 | 328 |
| rpcs3 | 280 | 28 | 17 | 177 | 177 | 325 |
| xenia | 253 | 25 | 27 | 170 | 170 | 305 |
| srm | 254 | 23 | 22 | 178 | 178 | 299 |
| shadps4 | 246 | 27 | 21 | 163 | 163 | 294 |
| vita3k | 256 | 24 | 8 | 152 | 152 | 288 |
| cloudsync | 166 | 9 | 75 | 131 | 131 | 250 |
| ra | 131 | 23 | 15 | 95 | 95 | 169 |
| dolphin | 125 | 22 | 18 | 90 | 90 | 165 |
| ppsspp | 117 | 19 | 26 | 84 | 84 | 162 |
| melonds | 107 | 16 | 14 | 73 | 73 | 137 |
| primehack | 103 | 18 | 12 | 67 | 67 | 133 |
| xemu | 100 | 16 | 15 | 69 | 69 | 131 |
| mgba | 103 | 12 | 8 | 78 | 78 | 123 |
| model2 | 96 | 17 | 2 | 60 | 60 | 115 |
| scummvm | 92 | 13 | 9 | 54 | 54 | 114 |
| supermodel | 92 | 17 | 4 | 57 | 57 | 113 |
| bigpemu | 70 | 3 | 1 | 38 | 38 | 74 |
| armsx2 | 22 | 31 | 0 | 29 | 29 | 53 |
| rmg | 25 | 8 | 0 | 22 | 22 | 33 |
| flycast | 27 | 1 | 3 | 22 | 22 | 31 |
| mame | 21 | 1 | 5 | 17 | 17 | 27 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
