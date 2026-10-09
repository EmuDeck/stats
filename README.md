# Estadísticas de EmuDeck

Actualizado: 2026-10-09 17:12 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 123 |
| linux-arm | 11 | 12 | 12 | 19 |
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
| Instalaciones early | 68 | 68 | 114 |
| Con CloudSync | 127 | 127 | 225 |
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
| pcsx2 | 294 | 11 | 41 | 219 | 219 | 346 |
| esde | 254 | 21 | 57 | 189 | 189 | 332 |
| azahar | 259 | 31 | 39 | 199 | 199 | 329 |
| ryujinx | 252 | 30 | 43 | 193 | 193 | 325 |
| duckstation | 278 | 26 | 16 | 197 | 197 | 320 |
| rpcs3 | 256 | 25 | 17 | 177 | 177 | 298 |
| cemu | 256 | 27 | 12 | 176 | 176 | 295 |
| xenia | 229 | 23 | 27 | 170 | 170 | 279 |
| shadps4 | 224 | 25 | 21 | 163 | 163 | 270 |
| srm | 226 | 20 | 21 | 178 | 178 | 267 |
| vita3k | 231 | 22 | 8 | 152 | 152 | 261 |
| cloudsync | 154 | 8 | 72 | 131 | 131 | 234 |
| ra | 117 | 20 | 15 | 95 | 95 | 152 |
| dolphin | 112 | 19 | 17 | 90 | 90 | 148 |
| ppsspp | 104 | 16 | 26 | 84 | 84 | 146 |
| melonds | 97 | 14 | 13 | 73 | 73 | 124 |
| primehack | 92 | 15 | 12 | 67 | 67 | 119 |
| xemu | 89 | 14 | 15 | 69 | 69 | 118 |
| mgba | 96 | 12 | 8 | 78 | 78 | 116 |
| model2 | 86 | 15 | 2 | 60 | 60 | 103 |
| scummvm | 82 | 11 | 9 | 54 | 54 | 102 |
| supermodel | 83 | 15 | 4 | 57 | 57 | 102 |
| bigpemu | 62 | 3 | 1 | 38 | 38 | 66 |
| armsx2 | 18 | 28 | 0 | 29 | 29 | 46 |
| rmg | 23 | 8 | 0 | 22 | 22 | 31 |
| flycast | 26 | 1 | 3 | 22 | 22 | 30 |
| mame | 19 | 0 | 5 | 17 | 17 | 24 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
