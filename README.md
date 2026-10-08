# Estadísticas de EmuDeck

Actualizado: 2026-10-08 18:18 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 89 |
| linux-arm | 1 | 1 | 1 | 10 |
| windows | 5 | 5 | 5 | 21 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 84 |
| Con CloudSync | 58 | 58 | 173 |
| % con CloudSync | | | 206% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 223 | 8 | 32 | 95 | 95 | 263 |
| esde | 196 | 10 | 46 | 84 | 84 | 252 |
| duckstation | 216 | 18 | 12 | 87 | 87 | 246 |
| azahar | 198 | 17 | 27 | 88 | 88 | 242 |
| ryujinx | 185 | 19 | 24 | 84 | 84 | 228 |
| rpcs3 | 188 | 16 | 12 | 78 | 78 | 216 |
| cemu | 189 | 15 | 8 | 80 | 80 | 212 |
| xenia | 170 | 16 | 20 | 79 | 79 | 206 |
| shadps4 | 170 | 16 | 16 | 81 | 81 | 202 |
| srm | 171 | 10 | 15 | 76 | 76 | 196 |
| vita3k | 172 | 15 | 5 | 68 | 68 | 192 |
| cloudsync | 114 | 4 | 61 | 60 | 60 | 179 |
| ra | 87 | 11 | 11 | 35 | 35 | 109 |
| dolphin | 82 | 11 | 13 | 34 | 34 | 106 |
| ppsspp | 74 | 10 | 20 | 31 | 31 | 104 |
| melonds | 70 | 9 | 10 | 31 | 31 | 89 |
| mgba | 71 | 8 | 5 | 35 | 35 | 84 |
| xemu | 62 | 8 | 12 | 26 | 26 | 82 |
| primehack | 63 | 8 | 9 | 23 | 23 | 80 |
| model2 | 57 | 8 | 2 | 22 | 22 | 67 |
| scummvm | 55 | 6 | 6 | 22 | 22 | 67 |
| supermodel | 56 | 8 | 1 | 21 | 21 | 65 |
| bigpemu | 47 | 3 | 1 | 18 | 18 | 51 |
| armsx2 | 15 | 18 | 0 | 13 | 13 | 33 |
| flycast | 20 | 1 | 2 | 9 | 9 | 23 |
| rmg | 15 | 3 | 0 | 6 | 6 | 18 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
