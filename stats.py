#!/usr/bin/env python3
import csv
import datetime
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RELEASES_CSV = DATA / "releases.csv"
BEACONS_CSV = DATA / "beacons.csv"
BEACONS_REPO = os.environ.get("GITHUB_REPOSITORY", "EmuDeck/stats")
CHART_DAYS = 60

APP_REPOS = ["emudeck-electron", "emudeck-electron-beta", "emudeck-electron-early", "emudeck-electron-early-unstable"]
# Release files: the latest*.yml are downloaded on every app start (update check), the rest on installs and updates
KINDS = {
    "launches-linux": lambda n: n == "latest-linux.yml",
    "launches-linux-arm": lambda n: n == "latest-linux-arm64.yml",
    "launches-windows": lambda n: n == "latest.yml",
    "launches-mac": lambda n: n == "latest-mac.yml",
    "installers-linux": lambda n: n.endswith(".appimage") and "arm64" not in n,
    "installers-linux-arm": lambda n: n.endswith(".appimage") and "arm64" in n,
    "installers-windows": lambda n: n.endswith(".exe"),
    "installers-mac": lambda n: n.endswith(".dmg"),
    "updates-windows": lambda n: n.endswith(".exe.blockmap"),
}
LABELS = {
    "launches-linux": "Arranques Linux x86",
    "launches-linux-arm": "Arranques Linux ARM",
    "launches-windows": "Arranques Windows",
    "launches-mac": "Arranques Mac",
}


def api(path, token=""):
    """GETs a GitHub API path and returns its JSON."""
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "EmuDeck-stats"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com{path}", headers=headers), timeout=60) as response:
        return json.load(response)


def read_csv(path):
    """Rows of a data CSV, or none if it does not exist yet."""
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    """Writes a data CSV sorted by its fields."""
    path.parent.mkdir(exist_ok=True)
    rows = sorted(rows, key=lambda r: tuple(r[f] for f in fields))
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def collect_releases(problems):
    """Saves today's accumulated downloads of each kind of release file, per app channel."""
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    rows = [r for r in read_csv(RELEASES_CSV) if r["date"] != today]
    for repo in APP_REPOS:
        totals = dict.fromkeys(KINDS, 0)
        page = 1
        try:
            while True:
                releases = api(f"/repos/EmuDeck/{repo}/releases?per_page=100&page={page}", os.environ.get("GH_TOKEN", ""))
                if not releases:
                    break
                for release in releases:
                    for asset in release.get("assets", []):
                        name = asset["name"].lower()
                        for kind, matches in KINDS.items():
                            if matches(name):
                                totals[kind] += asset["download_count"]
                page += 1
        except urllib.error.HTTPError as error:
            if error.code != 404:
                problems.append(f"EmuDeck/{repo}: {error}")
            continue
        rows += [{"date": today, "channel": repo, "kind": kind, "total": total} for kind, total in totals.items()]
    write_csv(RELEASES_CSV, rows, ["date", "channel", "kind", "total"])


def collect_beacons(problems):
    """Saves today's accumulated downloads of each beacon file (systems and installed emulators)."""
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    rows = [r for r in read_csv(BEACONS_CSV) if r["date"] != today]
    try:
        release = api(f"/repos/{BEACONS_REPO}/releases/tags/beacons", os.environ.get("GH_TOKEN", ""))
    except urllib.error.HTTPError as error:
        problems.append(f"beacons: {error}")
        return
    for asset in release.get("assets", []):
        rows.append({"date": today, "name": asset["name"].removesuffix(".txt"), "total": asset["download_count"]})
    write_csv(BEACONS_CSV, rows, ["date", "name", "total"])


def daily_beacons():
    """Beacon downloads per day and name, from the difference between consecutive accumulated totals."""
    totals = {}
    for row in read_csv(BEACONS_CSV):
        totals.setdefault(row["date"], {})[row["name"]] = int(row["total"])
    dates = sorted(totals)
    daily = {}
    for before, after in zip(dates, dates[1:]):
        daily[after] = {name: total - totals[before].get(name, 0) for name, total in totals[after].items()}
    return totals, daily


def by_period(dates, values):
    """Daily points, or weekly sums labelled by their first day when there are more than 90 days to draw."""
    if len(dates) <= 90:
        return [d[5:] for d in dates], values
    labels, sums = [], []
    for start in range(0, len(dates), 7):
        labels.append(dates[start][2:])
        sums.append(sum(values[start:start + 7]))
    return labels, sums


def beacons_section(today):
    """README lines with every install counted by the beacons since the first day: per system, per month and per emulator."""
    totals, daily = daily_beacons()
    lines = ["## Instalaciones de EmuDeck (beacons)", "",
             "Cada `setup` descarga `system-<sistema>.txt` y cada instalación de un emulador `<emulador>-<plataforma>.txt`. "
             "Los emuladores cuentan también las actualizaciones. Histórico completo desde el primer día.", ""]
    if not totals:
        return lines + ["Todavía no hay datos.", ""]
    last_totals = totals[max(totals)]
    dates = sorted(d for d in daily if d < today)
    platforms = ("linux", "linux-arm", "windows")
    in_days = lambda name, days: sum(daily[d].get(name, 0) for d in dates[-days:])

    systems = [f"system-{p}" for p in platforms]
    lines += ["| Sistema | Ayer | Últimos 7 días | Últimos 30 días | Total |", "|---|---|---|---|---|"]
    for name in systems:
        yesterday = daily[dates[-1]].get(name, 0) if dates else "–"
        week, month = (in_days(name, 7), in_days(name, 30)) if dates else ("–", "–")
        lines.append(f"| {name.removeprefix('system-')} | {yesterday} | {week} | {month} | {last_totals.get(name, 0)} |")
    lines.append("")

    if len(dates) > 1:
        for name in systems:
            labels, values = by_period(dates, [daily[d].get(name, 0) for d in dates])
            if any(values):
                lines += [chart(f"Instalaciones - {name.removeprefix('system-')}", labels, values, "Instalaciones"), ""]
        cumulative = [sum(totals[d].get(name, 0) for name in systems) for d in sorted(totals) if d < today]
        labels = [d[5:] for d in sorted(totals) if d < today]
        if len(cumulative) > 90:
            labels, cumulative = labels[::7], cumulative[::7]
        lines += [chart("Instalaciones acumuladas (todos los sistemas)", labels, cumulative, "Total"), ""]

    months = sorted({d[:7] for d in dates})
    if months:
        lines += ["### Por mes", "", "| Mes | Linux | Linux ARM | Windows | Total |", "|---|---|---|---|---|"]
        for month in reversed(months):
            cells = [sum(daily[d].get(name, 0) for d in dates if d.startswith(month)) for name in systems]
            lines.append(f"| {month} | {' | '.join(str(c) for c in cells)} | {sum(cells)} |")
        lines.append("")

    channel = [f"{app}-{p}" for app in ("early", "early-cloudsync") for p in platforms]
    early = lambda d, app: sum(daily[d].get(f"{app}-{p}", 0) for p in platforms)
    early_total = lambda app: sum(last_totals.get(f"{app}-{p}", 0) for p in platforms)
    early_days = lambda app, days: sum(early(d, app) for d in dates[-days:])
    lines += ["### Canal early (early + early-unstable)", "",
              "Instalaciones de EmuDeck con el backend en una rama early, y cuántas de ellas instalan CloudSync.", "",
              "| | Últimos 7 días | Últimos 30 días | Total |", "|---|---|---|---|"]
    for app, label in (("early", "Instalaciones early"), ("early-cloudsync", "Con CloudSync")):
        week, month = (early_days(app, 7), early_days(app, 30)) if dates else ("–", "–")
        lines.append(f"| {label} | {week} | {month} | {early_total(app)} |")
    if early_total("early"):
        lines.append(f"| % con CloudSync | | | {round(100 * early_total('early-cloudsync') / early_total('early'))}% |")
    lines.append("")
    if len(dates) > 1:
        labels, installs = by_period(dates, [early(d, "early") for d in dates])
        _, cloudsync = by_period(dates, [early(d, "early-cloudsync") for d in dates])
        if any(installs) or any(cloudsync):
            lines += ["Línea de arriba: instalaciones early. Línea de abajo: de ellas, con CloudSync.", "",
                      chart("Canal early: instalaciones y CloudSync", labels, [installs, cloudsync], "Instalaciones"), ""]

    apps = sorted({n.removesuffix("-linux-arm").removesuffix("-linux").removesuffix("-windows") for n in last_totals
                   if not n.startswith("system-") and n not in channel})
    app_total = lambda app: sum(last_totals.get(f"{app}-{p}", 0) for p in platforms)
    app_days = lambda app, days: sum(in_days(f"{app}-{p}", days) for p in platforms)
    lines += ["### Por emulador", "", "| Emulador | Linux (total) | Linux ARM (total) | Windows (total) | Últimos 7 días | Últimos 30 días | Total |", "|---|---|---|---|---|---|---|"]
    for app in sorted(apps, key=lambda a: -app_total(a)):
        if not app_total(app):
            continue
        per_platform = " | ".join(str(last_totals.get(f"{app}-{p}", 0)) for p in platforms)
        week, month = (app_days(app, 7), app_days(app, 30)) if dates else ("–", "–")
        lines.append(f"| {app} | {per_platform} | {week} | {month} | {app_total(app)} |")
    lines.append("")
    return lines


def daily_releases():
    """Downloads per day and kind, from the difference between consecutive accumulated totals of all channels."""
    totals = {}
    for row in read_csv(RELEASES_CSV):
        totals.setdefault(row["date"], {}).setdefault(row["kind"], 0)
        totals[row["date"]][row["kind"]] += int(row["total"])
    dates = sorted(totals)
    daily = {}
    for before, after in zip(dates, dates[1:]):
        daily[after] = {kind: totals[after].get(kind, 0) - totals[before].get(kind, 0) for kind in KINDS}
    return daily


def chart(title, labels, values, y_label):
    """Mermaid line chart GitHub draws inside the README; values can be a list of series to draw several lines."""
    labels = ", ".join(f'"{label}"' for label in labels)
    series = values if values and isinstance(values[0], list) else [values]
    return "\n".join([
        "```mermaid",
        "xychart-beta",
        f'    title "{title}"',
        f"    x-axis [{labels}]",
        f'    y-axis "{y_label}"',
        *[f"    line [{', '.join(str(v) for v in line)}]" for line in series],
        "```",
    ])


def write_readme(problems):
    """Regenerates README.md with the summary tables and the charts of the last CHART_DAYS days."""
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    lines = ["# Estadísticas de EmuDeck", "",
             f"Actualizado: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC. "
             "Las gráficas no incluyen el día de hoy porque aún está incompleto.", ""]

    daily = {d: v for d, v in daily_releases().items() if d < today}
    dates = sorted(daily)[-CHART_DAYS:]
    lines += ["## Arranques de la app (comprobaciones de actualización)", "",
              "Cada arranque descarga el `latest*.yml` de su sistema. Cuenta arranques, no personas.", ""]
    if dates:
        week = dates[-7:]
        lines += ["| Sistema | Ayer | Últimos 7 días |", "|---|---|---|"]
        for kind, label in LABELS.items():
            lines.append(f"| {label.replace('Arranques ', '')} | {daily[dates[-1]][kind]} | {sum(daily[d][kind] for d in week)} |")
        installs = sum(daily[d]["installers-windows"] - daily[d]["updates-windows"] for d in week)
        lines += ["", f"Instalaciones nuevas estimadas en Windows (7 días, `.exe` menos `.blockmap`): **{installs}**", ""]
        for kind, label in LABELS.items():
            values = [daily[d][kind] for d in dates]
            if len(dates) > 1 and any(values):
                lines += [chart(label, [d[5:] for d in dates], values, "Arranques"), ""]
    else:
        lines += ["Hacen falta al menos dos días de datos para calcular arranques diarios.", ""]

    lines += beacons_section(today)

    if problems:
        lines += ["## Avisos de la última ejecución", ""] + [f"- {p}" for p in problems] + [""]
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    """Collects today's data, saves it in data/ and rebuilds the README."""
    problems = []
    collect_releases(problems)
    collect_beacons(problems)
    write_readme(problems)
    for text in problems:
        print(f"! {text}")


if __name__ == "__main__":
    main()
