# Estadísticas de EmuDeck

Actualizado: 2026-10-08 04:46 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 74 |
| linux-arm | 1 | 1 | 1 | 5 |
| windows | 5 | 5 | 5 | 17 |

### Por mes

| Mes | Linux | Linux ARM | Windows | Total |
|---|---|---|---|---|
| 2026-10 | 34 | 1 | 5 | 40 |

### Canal early (early + early-unstable)

Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.

| | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|
| Instalaciones early | 29 | 29 | 73 |
| Con CloudSync | 58 | 58 | 154 |
| % con CloudSync | | | 211% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 186 | 4 | 23 | 95 | 95 | 213 |
| esde | 164 | 9 | 39 | 84 | 84 | 212 |
| azahar | 173 | 12 | 20 | 88 | 88 | 205 |
| duckstation | 179 | 12 | 8 | 87 | 87 | 199 |
| ryujinx | 150 | 14 | 16 | 84 | 84 | 180 |
| rpcs3 | 159 | 11 | 8 | 78 | 78 | 178 |
| cemu | 158 | 11 | 6 | 80 | 80 | 175 |
| shadps4 | 148 | 12 | 10 | 81 | 81 | 170 |
| xenia | 145 | 12 | 13 | 79 | 79 | 170 |
| vita3k | 149 | 11 | 4 | 68 | 68 | 164 |
| cloudsync | 97 | 3 | 58 | 60 | 60 | 158 |
| srm | 134 | 8 | 10 | 76 | 76 | 152 |
| dolphin | 71 | 6 | 9 | 34 | 34 | 86 |
| ppsspp | 65 | 5 | 16 | 31 | 31 | 86 |
| ra | 73 | 5 | 7 | 35 | 35 | 85 |
| melonds | 61 | 5 | 7 | 31 | 31 | 73 |
| mgba | 59 | 8 | 2 | 35 | 35 | 69 |
| xemu | 55 | 5 | 9 | 26 | 26 | 69 |
| primehack | 54 | 4 | 7 | 23 | 23 | 65 |
| scummvm | 51 | 4 | 4 | 22 | 22 | 59 |
| model2 | 52 | 5 | 0 | 22 | 22 | 57 |
| supermodel | 51 | 5 | 0 | 21 | 21 | 56 |
| bigpemu | 41 | 3 | 0 | 18 | 18 | 44 |
| armsx2 | 13 | 13 | 0 | 13 | 13 | 26 |
| flycast | 18 | 1 | 1 | 9 | 9 | 20 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 1 | 2 | 2 | 12 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
