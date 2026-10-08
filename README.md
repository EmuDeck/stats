# Estadísticas de EmuDeck

Actualizado: 2026-10-08 15:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 81 |
| linux-arm | 1 | 1 | 1 | 7 |
| windows | 5 | 5 | 5 | 20 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 80 |
| Con CloudSync | 58 | 58 | 167 |
| % con CloudSync | | | 209% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 213 | 6 | 31 | 95 | 95 | 250 |
| esde | 184 | 10 | 42 | 84 | 84 | 236 |
| duckstation | 206 | 15 | 12 | 87 | 87 | 233 |
| azahar | 192 | 14 | 25 | 88 | 88 | 231 |
| ryujinx | 169 | 16 | 22 | 84 | 84 | 207 |
| rpcs3 | 180 | 13 | 12 | 78 | 78 | 205 |
| cemu | 182 | 14 | 8 | 80 | 80 | 204 |
| xenia | 162 | 15 | 19 | 79 | 79 | 196 |
| shadps4 | 164 | 15 | 15 | 81 | 81 | 194 |
| vita3k | 165 | 14 | 5 | 68 | 68 | 184 |
| srm | 159 | 9 | 14 | 76 | 76 | 182 |
| cloudsync | 109 | 4 | 60 | 60 | 60 | 173 |
| dolphin | 77 | 8 | 13 | 34 | 34 | 98 |
| ra | 79 | 6 | 11 | 35 | 35 | 96 |
| ppsspp | 69 | 7 | 19 | 31 | 31 | 95 |
| melonds | 64 | 8 | 10 | 31 | 31 | 82 |
| mgba | 68 | 8 | 5 | 35 | 35 | 81 |
| xemu | 58 | 7 | 11 | 26 | 26 | 76 |
| primehack | 60 | 5 | 9 | 23 | 23 | 74 |
| scummvm | 53 | 5 | 6 | 22 | 22 | 64 |
| model2 | 54 | 7 | 2 | 22 | 22 | 63 |
| supermodel | 53 | 7 | 1 | 21 | 21 | 61 |
| bigpemu | 46 | 3 | 1 | 18 | 18 | 50 |
| armsx2 | 15 | 15 | 0 | 13 | 13 | 30 |
| flycast | 19 | 1 | 2 | 9 | 9 | 22 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
