# Estadísticas de EmuDeck

Actualizado: 2026-10-08 15:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 80 |
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
| pcsx2 | 209 | 6 | 31 | 95 | 95 | 246 |
| esde | 180 | 10 | 42 | 84 | 84 | 232 |
| duckstation | 203 | 15 | 12 | 87 | 87 | 230 |
| azahar | 190 | 14 | 25 | 88 | 88 | 229 |
| ryujinx | 166 | 16 | 22 | 84 | 84 | 204 |
| cemu | 178 | 14 | 8 | 80 | 80 | 200 |
| rpcs3 | 176 | 13 | 11 | 78 | 78 | 200 |
| xenia | 159 | 15 | 18 | 79 | 79 | 192 |
| shadps4 | 161 | 15 | 15 | 81 | 81 | 191 |
| vita3k | 162 | 14 | 5 | 68 | 68 | 181 |
| srm | 155 | 9 | 13 | 76 | 76 | 177 |
| cloudsync | 109 | 4 | 60 | 60 | 60 | 173 |
| dolphin | 76 | 8 | 12 | 34 | 34 | 96 |
| ra | 79 | 6 | 11 | 35 | 35 | 96 |
| ppsspp | 69 | 7 | 19 | 31 | 31 | 95 |
| melonds | 64 | 8 | 10 | 31 | 31 | 82 |
| mgba | 64 | 8 | 5 | 35 | 35 | 77 |
| xemu | 58 | 7 | 11 | 26 | 26 | 76 |
| primehack | 59 | 5 | 9 | 23 | 23 | 73 |
| scummvm | 53 | 5 | 6 | 22 | 22 | 64 |
| model2 | 54 | 7 | 2 | 22 | 22 | 63 |
| supermodel | 53 | 7 | 1 | 21 | 21 | 61 |
| bigpemu | 45 | 3 | 1 | 18 | 18 | 49 |
| armsx2 | 14 | 15 | 0 | 13 | 13 | 29 |
| flycast | 19 | 1 | 2 | 9 | 9 | 22 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
