# Estadísticas de EmuDeck

Actualizado: 2026-10-08 17:41 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 88 |
| linux-arm | 1 | 1 | 1 | 9 |
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
| Con CloudSync | 58 | 58 | 172 |
| % con CloudSync | | | 212% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 222 | 8 | 31 | 95 | 95 | 261 |
| esde | 196 | 10 | 42 | 84 | 84 | 248 |
| duckstation | 215 | 17 | 12 | 87 | 87 | 244 |
| azahar | 197 | 16 | 26 | 88 | 88 | 239 |
| ryujinx | 184 | 18 | 23 | 84 | 84 | 225 |
| rpcs3 | 187 | 15 | 12 | 78 | 78 | 214 |
| cemu | 189 | 14 | 8 | 80 | 80 | 211 |
| xenia | 170 | 15 | 19 | 79 | 79 | 204 |
| shadps4 | 170 | 15 | 15 | 81 | 81 | 200 |
| srm | 169 | 9 | 14 | 76 | 76 | 192 |
| vita3k | 172 | 14 | 5 | 68 | 68 | 191 |
| cloudsync | 114 | 4 | 60 | 60 | 60 | 178 |
| ra | 86 | 10 | 11 | 35 | 35 | 107 |
| dolphin | 81 | 10 | 13 | 34 | 34 | 104 |
| ppsspp | 73 | 9 | 19 | 31 | 31 | 101 |
| melonds | 70 | 8 | 10 | 31 | 31 | 88 |
| mgba | 70 | 8 | 5 | 35 | 35 | 83 |
| xemu | 62 | 7 | 12 | 26 | 26 | 81 |
| primehack | 62 | 7 | 9 | 23 | 23 | 78 |
| model2 | 57 | 7 | 2 | 22 | 22 | 66 |
| scummvm | 55 | 5 | 6 | 22 | 22 | 66 |
| supermodel | 56 | 7 | 1 | 21 | 21 | 64 |
| bigpemu | 47 | 3 | 1 | 18 | 18 | 51 |
| armsx2 | 15 | 17 | 0 | 13 | 13 | 32 |
| flycast | 20 | 1 | 2 | 9 | 9 | 23 |
| rmg | 15 | 2 | 0 | 6 | 6 | 17 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
