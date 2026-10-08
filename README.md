# Estadísticas de EmuDeck

Actualizado: 2026-10-08 03:48 UTC. Las gráficas no incluyen el día de hoy porque aún está incompleto.

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
| linux | 34 | 34 | 34 | 70 |
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
| Instalaciones early | 29 | 29 | 69 |
| Con CloudSync | 58 | 58 | 152 |
| % con CloudSync | | | 220% |

### Por emulador

| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |
|---|---|---|---|---|---|---|
| esde | 162 | 9 | 39 | 84 | 84 | 210 |
| pcsx2 | 181 | 4 | 23 | 95 | 95 | 208 |
| azahar | 168 | 12 | 20 | 88 | 88 | 200 |
| duckstation | 173 | 12 | 8 | 87 | 87 | 193 |
| ryujinx | 145 | 14 | 16 | 84 | 84 | 175 |
| rpcs3 | 154 | 11 | 8 | 78 | 78 | 173 |
| cemu | 153 | 11 | 6 | 80 | 80 | 170 |
| shadps4 | 143 | 12 | 10 | 81 | 81 | 165 |
| xenia | 140 | 12 | 13 | 79 | 79 | 165 |
| vita3k | 144 | 11 | 4 | 68 | 68 | 159 |
| cloudsync | 95 | 3 | 58 | 60 | 60 | 156 |
| srm | 130 | 8 | 10 | 76 | 76 | 148 |
| dolphin | 66 | 6 | 9 | 34 | 34 | 81 |
| ppsspp | 60 | 5 | 16 | 31 | 31 | 81 |
| ra | 68 | 5 | 7 | 35 | 35 | 80 |
| melonds | 57 | 5 | 7 | 31 | 31 | 69 |
| mgba | 57 | 8 | 2 | 35 | 35 | 67 |
| xemu | 51 | 5 | 9 | 26 | 26 | 65 |
| primehack | 50 | 4 | 7 | 23 | 23 | 61 |
| scummvm | 47 | 4 | 4 | 22 | 22 | 55 |
| model2 | 48 | 5 | 0 | 22 | 22 | 53 |
| supermodel | 47 | 5 | 0 | 21 | 21 | 52 |
| bigpemu | 39 | 3 | 0 | 18 | 18 | 42 |
| armsx2 | 12 | 13 | 0 | 13 | 13 | 25 |
| flycast | 17 | 1 | 1 | 9 | 9 | 19 |
| rmg | 14 | 1 | 0 | 6 | 6 | 15 |
| mame | 10 | 0 | 1 | 2 | 2 | 11 |
| eden | 8 | 0 | 0 | 0 | 0 | 8 |
| pegasus | 3 | 0 | 0 | 1 | 1 | 3 |
| ares | 0 | 1 | 0 | 1 | 1 | 1 |
