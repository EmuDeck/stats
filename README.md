# Estadísticas de EmuDeck

Actualizado: 2026-10-08 13:43 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 79 |
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
| Con CloudSync | 58 | 58 | 164 |
| % con CloudSync | | | 205% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 205 | 6 | 30 | 95 | 95 | 241 |
| esde | 180 | 10 | 41 | 84 | 84 | 231 |
| duckstation | 200 | 15 | 12 | 87 | 87 | 227 |
| azahar | 186 | 14 | 25 | 88 | 88 | 225 |
| ryujinx | 161 | 16 | 21 | 84 | 84 | 198 |
| cemu | 175 | 14 | 8 | 80 | 80 | 197 |
| rpcs3 | 172 | 13 | 11 | 78 | 78 | 196 |
| xenia | 155 | 15 | 18 | 79 | 79 | 188 |
| shadps4 | 158 | 15 | 13 | 81 | 81 | 186 |
| vita3k | 159 | 14 | 5 | 68 | 68 | 178 |
| srm | 151 | 9 | 13 | 76 | 76 | 173 |
| cloudsync | 107 | 3 | 59 | 60 | 60 | 169 |
| ra | 78 | 6 | 11 | 35 | 35 | 95 |
| dolphin | 75 | 8 | 11 | 34 | 34 | 94 |
| ppsspp | 68 | 7 | 19 | 31 | 31 | 94 |
| melonds | 63 | 8 | 10 | 31 | 31 | 81 |
| mgba | 64 | 8 | 5 | 35 | 35 | 77 |
| xemu | 57 | 7 | 11 | 26 | 26 | 75 |
| primehack | 58 | 5 | 9 | 23 | 23 | 72 |
| scummvm | 52 | 5 | 6 | 22 | 22 | 63 |
| model2 | 53 | 7 | 2 | 22 | 22 | 62 |
| supermodel | 52 | 7 | 1 | 21 | 21 | 60 |
| bigpemu | 45 | 3 | 1 | 18 | 18 | 49 |
| armsx2 | 14 | 15 | 0 | 13 | 13 | 29 |
| flycast | 19 | 1 | 2 | 9 | 9 | 22 |
| rmg | 15 | 1 | 0 | 6 | 6 | 16 |
| mame | 11 | 0 | 3 | 2 | 2 | 14 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
