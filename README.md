# Estadísticas de EmuDeck

Actualizado: 2026-10-09 17:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 42 | 76 | 76 | 126 |
| linux-arm | 11 | 12 | 12 | 20 |
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
| Instalaciones early | 68 | 68 | 117 |
| Con CloudSync | 127 | 127 | 225 |
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
| pcsx2 | 300 | 11 | 41 | 219 | 219 | 352 |
| esde | 258 | 21 | 61 | 189 | 189 | 340 |
| azahar | 263 | 32 | 39 | 199 | 199 | 334 |
| ryujinx | 257 | 31 | 43 | 193 | 193 | 331 |
| duckstation | 283 | 27 | 16 | 197 | 197 | 326 |
| rpcs3 | 260 | 26 | 17 | 177 | 177 | 303 |
| cemu | 260 | 28 | 12 | 176 | 176 | 300 |
| xenia | 230 | 24 | 27 | 170 | 170 | 281 |
| srm | 231 | 21 | 21 | 178 | 178 | 273 |
| shadps4 | 225 | 26 | 21 | 163 | 163 | 272 |
| vita3k | 234 | 23 | 8 | 152 | 152 | 265 |
| cloudsync | 154 | 8 | 72 | 131 | 131 | 234 |
| ra | 119 | 21 | 15 | 95 | 95 | 155 |
| dolphin | 115 | 20 | 17 | 90 | 90 | 152 |
| ppsspp | 107 | 17 | 26 | 84 | 84 | 150 |
| melonds | 98 | 15 | 13 | 73 | 73 | 126 |
| primehack | 94 | 16 | 12 | 67 | 67 | 122 |
| xemu | 90 | 15 | 15 | 69 | 69 | 120 |
| mgba | 97 | 12 | 8 | 78 | 78 | 117 |
| model2 | 87 | 16 | 2 | 60 | 60 | 105 |
| scummvm | 83 | 12 | 9 | 54 | 54 | 104 |
| supermodel | 83 | 16 | 4 | 57 | 57 | 103 |
| bigpemu | 64 | 3 | 1 | 38 | 38 | 68 |
| armsx2 | 18 | 29 | 0 | 29 | 29 | 47 |
| rmg | 23 | 8 | 0 | 22 | 22 | 31 |
| flycast | 26 | 1 | 3 | 22 | 22 | 30 |
| mame | 19 | 0 | 5 | 17 | 17 | 24 |
| eden | 10 | 0 | 0 | 0 | 0 | 10 |
| pegasus | 3 | 0 | 1 | 1 | 1 | 4 |
| ares | 1 | 1 | 0 | 1 | 1 | 2 |
| yuzu | 1 | 0 | 0 | 0 | 0 | 1 |
