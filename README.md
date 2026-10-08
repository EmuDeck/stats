# Estadísticas de EmuDeck

Actualizado: 2026-10-08 16:18 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 83 |
| linux-arm | 1 | 1 | 1 | 8 |
| windows | 5 | 5 | 5 | 20 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 81 |
| Con CloudSync | 58 | 58 | 167 |
| % con CloudSync | | | 206% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 217 | 7 | 31 | 95 | 95 | 255 |
| duckstation | 210 | 16 | 12 | 87 | 87 | 238 |
| esde | 186 | 10 | 42 | 84 | 84 | 238 |
| azahar | 195 | 15 | 25 | 88 | 88 | 235 |
| ryujinx | 173 | 17 | 22 | 84 | 84 | 212 |
| rpcs3 | 183 | 14 | 12 | 78 | 78 | 209 |
| cemu | 185 | 14 | 8 | 80 | 80 | 207 |
| xenia | 165 | 15 | 19 | 79 | 79 | 199 |
| shadps4 | 167 | 15 | 15 | 81 | 81 | 197 |
| vita3k | 169 | 14 | 5 | 68 | 68 | 188 |
| srm | 164 | 9 | 14 | 76 | 76 | 187 |
| cloudsync | 109 | 4 | 60 | 60 | 60 | 173 |
| dolphin | 79 | 9 | 13 | 34 | 34 | 101 |
| ra | 81 | 7 | 11 | 35 | 35 | 99 |
| ppsspp | 71 | 8 | 19 | 31 | 31 | 98 |
| melonds | 66 | 8 | 10 | 31 | 31 | 84 |
| mgba | 69 | 8 | 5 | 35 | 35 | 82 |
| xemu | 60 | 7 | 12 | 26 | 26 | 79 |
| primehack | 62 | 6 | 9 | 23 | 23 | 77 |
| scummvm | 55 | 5 | 6 | 22 | 22 | 66 |
| model2 | 56 | 7 | 2 | 22 | 22 | 65 |
| supermodel | 55 | 7 | 1 | 21 | 21 | 63 |
| bigpemu | 46 | 3 | 1 | 18 | 18 | 50 |
| armsx2 | 15 | 16 | 0 | 13 | 13 | 31 |
| flycast | 19 | 1 | 2 | 9 | 9 | 22 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
