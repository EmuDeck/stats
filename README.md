# Estadísticas de EmuDeck

Actualizado: 2026-10-08 20:42 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 92 |
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
| Instalaciones early | 29 | 29 | 86 |
| Con CloudSync | 58 | 58 | 177 |
| % con CloudSync | | | 206% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 231 | 11 | 33 | 95 | 95 | 275 |
| esde | 207 | 10 | 47 | 84 | 84 | 264 |
| duckstation | 223 | 20 | 13 | 87 | 87 | 256 |
| azahar | 207 | 20 | 28 | 88 | 88 | 255 |
| ryujinx | 194 | 21 | 26 | 84 | 84 | 241 |
| rpcs3 | 196 | 19 | 14 | 78 | 78 | 229 |
| cemu | 198 | 17 | 9 | 80 | 80 | 224 |
| xenia | 177 | 18 | 23 | 79 | 79 | 218 |
| shadps4 | 176 | 20 | 16 | 81 | 81 | 212 |
| srm | 180 | 12 | 16 | 76 | 76 | 208 |
| vita3k | 179 | 17 | 6 | 68 | 68 | 202 |
| cloudsync | 115 | 4 | 64 | 60 | 60 | 183 |
| ra | 89 | 13 | 12 | 35 | 35 | 114 |
| dolphin | 84 | 14 | 14 | 34 | 34 | 112 |
| ppsspp | 76 | 12 | 21 | 31 | 31 | 109 |
| melonds | 73 | 11 | 11 | 31 | 31 | 95 |
| xemu | 65 | 11 | 13 | 26 | 26 | 89 |
| mgba | 73 | 8 | 6 | 35 | 35 | 87 |
| primehack | 66 | 11 | 10 | 23 | 23 | 87 |
| model2 | 61 | 12 | 2 | 22 | 22 | 75 |
| scummvm | 58 | 8 | 7 | 22 | 22 | 73 |
| supermodel | 58 | 12 | 2 | 21 | 21 | 72 |
| bigpemu | 48 | 3 | 1 | 18 | 18 | 52 |
| armsx2 | 16 | 21 | 0 | 13 | 13 | 37 |
| flycast | 20 | 1 | 2 | 9 | 9 | 23 |
| rmg | 16 | 4 | 0 | 6 | 6 | 20 |
| mame | 13 | 0 | 4 | 2 | 2 | 17 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
