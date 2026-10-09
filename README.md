# Estadísticas de EmuDeck

Actualizado: 2026-10-09 04:19 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| Instalaciones early | 68 | 68 | 101 |
| Con CloudSync | 127 | 127 | 203 |
| % con CloudSync | | | 201% |

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
| pcsx2 | 258 | 11 | 39 | 219 | 219 | 308 |
| esde | 227 | 18 | 53 | 189 | 189 | 298 |
| azahar | 228 | 26 | 35 | 199 | 199 | 289 |
| duckstation | 246 | 22 | 15 | 197 | 197 | 283 |
| ryujinx | 219 | 25 | 38 | 193 | 193 | 282 |
| rpcs3 | 222 | 21 | 15 | 177 | 177 | 258 |
| cemu | 222 | 23 | 10 | 176 | 176 | 255 |
| xenia | 198 | 20 | 26 | 170 | 170 | 244 |
| shadps4 | 200 | 22 | 20 | 163 | 163 | 242 |
| srm | 199 | 18 | 17 | 178 | 178 | 234 |
| vita3k | 200 | 19 | 7 | 152 | 152 | 226 |
| cloudsync | 138 | 6 | 65 | 131 | 131 | 209 |
| ra | 100 | 18 | 13 | 95 | 95 | 131 |
| dolphin | 94 | 17 | 16 | 90 | 90 | 127 |
| ppsspp | 87 | 14 | 24 | 84 | 84 | 125 |
| melonds | 80 | 13 | 12 | 73 | 73 | 105 |
| mgba | 86 | 11 | 7 | 78 | 78 | 104 |
| xemu | 74 | 13 | 14 | 69 | 69 | 101 |
| primehack | 75 | 13 | 11 | 67 | 67 | 99 |
| model2 | 70 | 14 | 2 | 60 | 60 | 86 |
| scummvm | 66 | 10 | 8 | 54 | 54 | 84 |
| supermodel | 67 | 14 | 3 | 57 | 57 | 84 |
| bigpemu | 56 | 3 | 1 | 38 | 38 | 60 |
| armsx2 | 17 | 24 | 0 | 29 | 29 | 41 |
| flycast | 24 | 1 | 2 | 22 | 22 | 27 |
| rmg | 20 | 7 | 0 | 22 | 22 | 27 |
| mame | 17 | 0 | 5 | 17 | 17 | 22 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
