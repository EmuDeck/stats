# Estadísticas de EmuDeck

Actualizado: 2026-10-08 21:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

## Arranques de la app (comprobaciones de actualización)

Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.

| Sistema | Ayer | Últimos 7 días |
|---|---|---|
| Linux x86 | 11951 | 23833 |
| Linux ARM | 160 | 382 |
| Windows | 3127 | 6448 |
| Mac | 0 | 0 |

Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **239**

```mermaid
xychart-beta
    title "Arranques Linux x86"
    x-axis ["10-06", "10-07"]
    y-axis "Arranques"
    line [11882, 11951]
```

```mermaid
xychart-beta
    title "Arranques Linux ARM"
    x-axis ["10-06", "10-07"]
    y-axis "Arranques"
    line [222, 160]
```

```mermaid
xychart-beta
    title "Arranques Windows"
    x-axis ["10-06", "10-07"]
    y-axis "Arranques"
    line [3321, 3127]
```

## Instalaciones de EmuDeck (beacons)

Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.

| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|
| linux | 34 | 34 | 34 | 95 |
| linux-arm | 1 | 1 | 1 | 15 |
| windows | 5 | 5 | 5 | 22 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 89 |
| Con CloudSync | 58 | 58 | 179 |
| % con CloudSync | | | 201% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 234 | 11 | 33 | 95 | 95 | 278 |
| esde | 210 | 12 | 47 | 84 | 84 | 269 |
| azahar | 210 | 21 | 28 | 88 | 88 | 259 |
| duckstation | 226 | 20 | 13 | 87 | 87 | 259 |
| ryujinx | 198 | 21 | 26 | 84 | 84 | 245 |
| rpcs3 | 199 | 19 | 14 | 78 | 78 | 232 |
| cemu | 201 | 18 | 9 | 80 | 80 | 228 |
| xenia | 180 | 18 | 23 | 79 | 79 | 221 |
| shadps4 | 179 | 20 | 17 | 81 | 81 | 216 |
| srm | 185 | 15 | 16 | 76 | 76 | 216 |
| vita3k | 182 | 17 | 6 | 68 | 68 | 205 |
| cloudsync | 117 | 4 | 64 | 60 | 60 | 185 |
| ra | 92 | 14 | 12 | 35 | 35 | 118 |
| dolphin | 87 | 14 | 14 | 34 | 34 | 115 |
| ppsspp | 79 | 12 | 21 | 31 | 31 | 112 |
| melonds | 76 | 11 | 11 | 31 | 31 | 98 |
| xemu | 68 | 11 | 13 | 26 | 26 | 92 |
| mgba | 75 | 9 | 6 | 35 | 35 | 90 |
| primehack | 69 | 11 | 10 | 23 | 23 | 90 |
| model2 | 64 | 12 | 2 | 22 | 22 | 78 |
| scummvm | 61 | 8 | 7 | 22 | 22 | 76 |
| supermodel | 61 | 12 | 2 | 21 | 21 | 75 |
| bigpemu | 49 | 3 | 1 | 18 | 18 | 53 |
| armsx2 | 16 | 21 | 0 | 13 | 13 | 37 |
| flycast | 22 | 1 | 2 | 9 | 9 | 25 |
| rmg | 18 | 5 | 0 | 6 | 6 | 23 |
| mame | 15 | 0 | 4 | 2 | 2 | 19 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
