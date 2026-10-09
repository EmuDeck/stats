# Estadísticas de EmuDeck

Actualizado: 2026-10-09 02:56 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 102 |
| linux-arm | 11 | 12 | 12 | 16 |
| windows | 11 | 16 | 16 | 23 |

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
| Instalaciones early | 68 | 68 | 97 |
| Con CloudSync | 127 | 127 | 200 |
| % con CloudSync | | | 206% |

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
| pcsx2 | 256 | 11 | 36 | 219 | 219 | 303 |
| esde | 226 | 14 | 49 | 189 | 189 | 289 |
| azahar | 226 | 25 | 32 | 199 | 199 | 283 |
| duckstation | 244 | 21 | 15 | 197 | 197 | 280 |
| ryujinx | 217 | 23 | 36 | 193 | 193 | 276 |
| rpcs3 | 220 | 20 | 15 | 177 | 177 | 255 |
| cemu | 220 | 21 | 10 | 176 | 176 | 251 |
| shadps4 | 198 | 21 | 20 | 163 | 163 | 239 |
| xenia | 196 | 19 | 24 | 170 | 170 | 239 |
| srm | 198 | 18 | 17 | 178 | 178 | 233 |
| vita3k | 198 | 18 | 7 | 152 | 152 | 223 |
| cloudsync | 136 | 5 | 65 | 131 | 131 | 206 |
| ra | 100 | 17 | 13 | 95 | 95 | 130 |
| dolphin | 94 | 16 | 16 | 90 | 90 | 126 |
| ppsspp | 87 | 13 | 22 | 84 | 84 | 122 |
| melonds | 80 | 12 | 12 | 73 | 73 | 104 |
| mgba | 84 | 11 | 6 | 78 | 78 | 101 |
| xemu | 74 | 12 | 14 | 69 | 69 | 100 |
| primehack | 75 | 12 | 11 | 67 | 67 | 98 |
| model2 | 70 | 13 | 2 | 60 | 60 | 85 |
| scummvm | 66 | 9 | 8 | 54 | 54 | 83 |
| supermodel | 67 | 13 | 2 | 57 | 57 | 82 |
| bigpemu | 56 | 3 | 1 | 38 | 38 | 60 |
| armsx2 | 17 | 22 | 0 | 29 | 29 | 39 |
| flycast | 24 | 1 | 2 | 22 | 22 | 27 |
| rmg | 20 | 7 | 0 | 22 | 22 | 27 |
| mame | 17 | 0 | 5 | 17 | 17 | 22 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
