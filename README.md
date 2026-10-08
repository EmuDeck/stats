# Estadísticas de EmuDeck

Actualizado: 2026-10-08 02:53 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 66 |
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
| Instalaciones early | 29 | 29 | 65 |
| Con CloudSync | 58 | 58 | 145 |
| % con CloudSync | | | 223% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| esde | 154 | 9 | 39 | 84 | 84 | 202 |
| pcsx2 | 172 | 4 | 23 | 95 | 95 | 199 |
| azahar | 159 | 12 | 20 | 88 | 88 | 191 |
| duckstation | 167 | 12 | 8 | 87 | 87 | 187 |
| ryujinx | 141 | 14 | 16 | 84 | 84 | 171 |
| rpcs3 | 146 | 11 | 8 | 78 | 78 | 165 |
| cemu | 147 | 11 | 6 | 80 | 80 | 164 |
| xenia | 134 | 12 | 13 | 79 | 79 | 159 |
| shadps4 | 136 | 12 | 10 | 81 | 81 | 158 |
| vita3k | 139 | 11 | 4 | 68 | 68 | 154 |
| cloudsync | 89 | 3 | 57 | 60 | 60 | 149 |
| srm | 125 | 8 | 10 | 76 | 76 | 143 |
| dolphin | 63 | 6 | 9 | 34 | 34 | 78 |
| ppsspp | 57 | 5 | 16 | 31 | 31 | 78 |
| ra | 66 | 5 | 7 | 35 | 35 | 78 |
| melonds | 55 | 5 | 7 | 31 | 31 | 67 |
| mgba | 53 | 8 | 2 | 35 | 35 | 63 |
| xemu | 48 | 5 | 9 | 26 | 26 | 62 |
| primehack | 47 | 4 | 7 | 23 | 23 | 58 |
| scummvm | 45 | 4 | 4 | 22 | 22 | 53 |
| model2 | 44 | 5 | 0 | 22 | 22 | 49 |
| supermodel | 43 | 5 | 0 | 21 | 21 | 48 |
| bigpemu | 38 | 3 | 0 | 18 | 18 | 41 |
| armsx2 | 12 | 13 | 0 | 13 | 13 | 25 |
| flycast | 15 | 1 | 1 | 9 | 9 | 17 |
| rmg | 14 | 1 | 0 | 6 | 6 | 15 |
| mame | 8 | 0 | 1 | 2 | 2 | 9 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
