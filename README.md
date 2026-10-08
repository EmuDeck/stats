# Estadísticas de EmuDeck

Actualizado: 2026-10-08 07:01 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| Con CloudSync | 58 | 58 | 156 |
| % con CloudSync | | | 214% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 190 | 5 | 24 | 95 | 95 | 219 |
| esde | 167 | 10 | 40 | 84 | 84 | 217 |
| azahar | 176 | 13 | 21 | 88 | 88 | 210 |
| duckstation | 184 | 13 | 10 | 87 | 87 | 207 |
| ryujinx | 154 | 15 | 18 | 84 | 84 | 187 |
| rpcs3 | 162 | 12 | 9 | 78 | 78 | 183 |
| cemu | 161 | 12 | 7 | 80 | 80 | 180 |
| xenia | 148 | 13 | 15 | 79 | 79 | 176 |
| shadps4 | 151 | 13 | 11 | 81 | 81 | 175 |
| vita3k | 152 | 12 | 5 | 68 | 68 | 169 |
| cloudsync | 100 | 3 | 58 | 60 | 60 | 161 |
| srm | 138 | 9 | 10 | 76 | 76 | 157 |
| ppsspp | 65 | 5 | 17 | 31 | 31 | 87 |
| ra | 73 | 5 | 9 | 35 | 35 | 87 |
| dolphin | 71 | 6 | 9 | 34 | 34 | 86 |
| melonds | 61 | 5 | 8 | 31 | 31 | 74 |
| mgba | 61 | 8 | 3 | 35 | 35 | 72 |
| xemu | 55 | 5 | 11 | 26 | 26 | 71 |
| primehack | 54 | 4 | 8 | 23 | 23 | 66 |
| scummvm | 51 | 4 | 6 | 22 | 22 | 61 |
| model2 | 52 | 5 | 1 | 22 | 22 | 58 |
| supermodel | 51 | 5 | 1 | 21 | 21 | 57 |
| bigpemu | 43 | 3 | 0 | 18 | 18 | 46 |
| armsx2 | 14 | 14 | 0 | 13 | 13 | 28 |
| flycast | 18 | 1 | 1 | 9 | 9 | 20 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 1 | 2 | 2 | 12 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
