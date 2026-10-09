# Estadísticas de EmuDeck

Actualizado: 2026-10-09 16:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 121 |
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
| Instalaciones early | 68 | 68 | 112 |
| Con CloudSync | 127 | 127 | 222 |
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
| pcsx2 | 292 | 11 | 41 | 219 | 219 | 344 |
| esde | 252 | 21 | 56 | 189 | 189 | 329 |
| azahar | 257 | 30 | 39 | 199 | 199 | 326 |
| ryujinx | 248 | 29 | 42 | 193 | 193 | 319 |
| duckstation | 276 | 25 | 16 | 197 | 197 | 317 |
| rpcs3 | 254 | 24 | 17 | 177 | 177 | 295 |
| cemu | 254 | 26 | 12 | 176 | 176 | 292 |
| xenia | 228 | 22 | 27 | 170 | 170 | 277 |
| shadps4 | 224 | 24 | 21 | 163 | 163 | 269 |
| srm | 222 | 19 | 20 | 178 | 178 | 261 |
| vita3k | 228 | 21 | 8 | 152 | 152 | 257 |
| cloudsync | 151 | 8 | 72 | 131 | 131 | 231 |
| ra | 116 | 19 | 15 | 95 | 95 | 150 |
| dolphin | 111 | 18 | 17 | 90 | 90 | 146 |
| ppsspp | 102 | 15 | 26 | 84 | 84 | 143 |
| melonds | 96 | 13 | 13 | 73 | 73 | 122 |
| primehack | 91 | 14 | 12 | 67 | 67 | 117 |
| mgba | 96 | 12 | 8 | 78 | 78 | 116 |
| xemu | 88 | 13 | 15 | 69 | 69 | 116 |
| model2 | 84 | 14 | 2 | 60 | 60 | 100 |
| scummvm | 81 | 10 | 9 | 54 | 54 | 100 |
| supermodel | 82 | 14 | 4 | 57 | 57 | 100 |
| bigpemu | 61 | 3 | 1 | 38 | 38 | 65 |
| armsx2 | 18 | 27 | 0 | 29 | 29 | 45 |
| rmg | 22 | 8 | 0 | 22 | 22 | 30 |
| flycast | 25 | 1 | 3 | 22 | 22 | 29 |
| mame | 18 | 0 | 5 | 17 | 17 | 23 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
