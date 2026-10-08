# Estadísticas de EmuDeck

Actualizado: 2026-10-08 16:44 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 85 |
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
| Con CloudSync | 58 | 58 | 170 |
| % con CloudSync | | | 210% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 220 | 7 | 31 | 95 | 95 | 258 |
| esde | 191 | 10 | 42 | 84 | 84 | 243 |
| duckstation | 213 | 16 | 12 | 87 | 87 | 241 |
| azahar | 196 | 15 | 26 | 88 | 88 | 237 |
| ryujinx | 177 | 17 | 22 | 84 | 84 | 216 |
| rpcs3 | 184 | 14 | 12 | 78 | 78 | 210 |
| cemu | 186 | 14 | 8 | 80 | 80 | 208 |
| xenia | 168 | 15 | 19 | 79 | 79 | 202 |
| shadps4 | 167 | 15 | 15 | 81 | 81 | 197 |
| vita3k | 172 | 14 | 5 | 68 | 68 | 191 |
| srm | 166 | 9 | 14 | 76 | 76 | 189 |
| cloudsync | 112 | 4 | 60 | 60 | 60 | 176 |
| dolphin | 80 | 9 | 13 | 34 | 34 | 102 |
| ra | 83 | 7 | 11 | 35 | 35 | 101 |
| ppsspp | 72 | 8 | 19 | 31 | 31 | 99 |
| melonds | 68 | 8 | 10 | 31 | 31 | 86 |
| mgba | 70 | 8 | 5 | 35 | 35 | 83 |
| xemu | 61 | 7 | 12 | 26 | 26 | 80 |
| primehack | 62 | 6 | 9 | 23 | 23 | 77 |
| model2 | 57 | 7 | 2 | 22 | 22 | 66 |
| scummvm | 55 | 5 | 6 | 22 | 22 | 66 |
| supermodel | 56 | 7 | 1 | 21 | 21 | 64 |
| bigpemu | 47 | 3 | 1 | 18 | 18 | 51 |
| armsx2 | 15 | 16 | 0 | 13 | 13 | 31 |
| flycast | 20 | 1 | 2 | 9 | 9 | 23 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
