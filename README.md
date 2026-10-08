# Estadísticas de EmuDeck

Actualizado: 2026-10-08 19:40 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 90 |
| linux-arm | 1 | 1 | 1 | 11 |
| windows | 5 | 5 | 5 | 21 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 85 |
| Con CloudSync | 58 | 58 | 175 |
| % con CloudSync | | | 206% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 227 | 8 | 32 | 95 | 95 | 267 |
| esde | 205 | 10 | 46 | 84 | 84 | 261 |
| duckstation | 220 | 19 | 12 | 87 | 87 | 251 |
| azahar | 203 | 18 | 27 | 88 | 88 | 248 |
| ryujinx | 190 | 20 | 25 | 84 | 84 | 235 |
| rpcs3 | 192 | 17 | 13 | 78 | 78 | 222 |
| cemu | 195 | 16 | 8 | 80 | 80 | 219 |
| xenia | 173 | 17 | 20 | 79 | 79 | 210 |
| shadps4 | 174 | 17 | 16 | 81 | 81 | 207 |
| srm | 175 | 11 | 15 | 76 | 76 | 201 |
| vita3k | 176 | 16 | 5 | 68 | 68 | 197 |
| cloudsync | 115 | 4 | 62 | 60 | 60 | 181 |
| ra | 88 | 12 | 11 | 35 | 35 | 111 |
| dolphin | 83 | 12 | 13 | 34 | 34 | 108 |
| ppsspp | 75 | 11 | 20 | 31 | 31 | 106 |
| melonds | 72 | 10 | 10 | 31 | 31 | 92 |
| mgba | 73 | 8 | 5 | 35 | 35 | 86 |
| xemu | 64 | 9 | 12 | 26 | 26 | 85 |
| primehack | 64 | 9 | 9 | 23 | 23 | 82 |
| model2 | 59 | 9 | 2 | 22 | 22 | 70 |
| scummvm | 57 | 7 | 6 | 22 | 22 | 70 |
| supermodel | 57 | 9 | 1 | 21 | 21 | 67 |
| bigpemu | 47 | 3 | 1 | 18 | 18 | 51 |
| armsx2 | 15 | 19 | 0 | 13 | 13 | 34 |
| flycast | 20 | 1 | 2 | 9 | 9 | 23 |
| rmg | 15 | 4 | 0 | 6 | 6 | 19 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
