# Estadísticas de EmuDeck

Actualizado: 2026-10-08 22:14 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 96 |
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
| Instalaciones early | 29 | 29 | 90 |
| Con CloudSync | 58 | 58 | 180 |
| % con CloudSync | | | 200% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| pcsx2 | 238 | 11 | 33 | 95 | 95 | 282 |
| esde | 213 | 12 | 47 | 84 | 84 | 272 |
| azahar | 213 | 22 | 28 | 88 | 88 | 263 |
| duckstation | 229 | 20 | 13 | 87 | 87 | 262 |
| ryujinx | 202 | 21 | 26 | 84 | 84 | 249 |
| rpcs3 | 203 | 19 | 14 | 78 | 78 | 236 |
| cemu | 205 | 20 | 9 | 80 | 80 | 234 |
| xenia | 184 | 18 | 23 | 79 | 79 | 225 |
| srm | 187 | 17 | 16 | 76 | 76 | 220 |
| shadps4 | 182 | 20 | 17 | 81 | 81 | 219 |
| vita3k | 185 | 17 | 6 | 68 | 68 | 208 |
| cloudsync | 118 | 4 | 64 | 60 | 60 | 186 |
| ra | 93 | 15 | 12 | 35 | 35 | 120 |
| dolphin | 88 | 15 | 14 | 34 | 34 | 117 |
| ppsspp | 80 | 12 | 21 | 31 | 31 | 113 |
| melonds | 77 | 11 | 11 | 31 | 31 | 99 |
| mgba | 78 | 10 | 6 | 35 | 35 | 94 |
| xemu | 69 | 11 | 13 | 26 | 26 | 93 |
| primehack | 70 | 11 | 10 | 23 | 23 | 91 |
| model2 | 65 | 12 | 2 | 22 | 22 | 79 |
| scummvm | 62 | 8 | 7 | 22 | 22 | 77 |
| supermodel | 62 | 12 | 2 | 21 | 21 | 76 |
| bigpemu | 49 | 3 | 1 | 18 | 18 | 53 |
| armsx2 | 16 | 21 | 0 | 13 | 13 | 37 |
| flycast | 23 | 1 | 2 | 9 | 9 | 26 |
| rmg | 19 | 5 | 0 | 6 | 6 | 24 |
| mame | 16 | 0 | 4 | 2 | 2 | 20 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
