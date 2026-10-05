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
CLONES_CSV = DATA / "clones.csv"
RELEASES_CSV = DATA / "releases.csv"
CHART_DAYS = 60

# Backend repos: Linux and Mac clone the bash one, Windows the PowerShell one
BACKENDS = {
    "dragoonDorise/EmuDeck": "Linux + Mac",
    "EmuDeck/emudeck-we": "Windows",
}
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


def backend_token(repo):
    """Token allowed to read a backend's traffic: one per owner, or TRAFFIC_TOKEN for both."""
    owner = repo.split("/")[0].upper()
    return os.environ.get(f"TRAFFIC_TOKEN_{owner}") or os.environ.get("TRAFFIC_TOKEN", "")


def collect_clones(problems):
    """Adds the last 14 days of clones and unique cloners of each backend to clones.csv (GitHub keeps no more)."""
    rows = {(r["date"], r["repo"]): r for r in read_csv(CLONES_CSV)}
    for repo in BACKENDS:
        token = backend_token(repo)
        if not token:
            problems.append(f"{repo}: falta el token de tráfico")
            continue
        try:
            traffic = api(f"/repos/{repo}/traffic/clones?per=day", token)
        except urllib.error.HTTPError as error:
            problems.append(f"{repo}: {error}")
            continue
        for day in traffic.get("clones", []):
            date = day["timestamp"][:10]
            rows[(date, repo)] = {"date": date, "repo": repo, "count": day["count"], "uniques": day["uniques"]}
    write_csv(CLONES_CSV, rows.values(), ["date", "repo", "count", "uniques"])


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


def chart(title, dates, values, y_label):
    """Mermaid line chart GitHub draws inside the README."""
    labels = ", ".join(f'"{d[5:]}"' for d in dates)
    return "\n".join([
        "```mermaid",
        "xychart-beta",
        f'    title "{title}"',
        f"    x-axis [{labels}]",
        f'    y-axis "{y_label}"',
        f"    line [{', '.join(str(v) for v in values)}]",
        "```",
    ])


def write_readme(problems):
    """Regenerates README.md with the summary tables and the charts of the last CHART_DAYS days."""
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    lines = ["# Estadísticas de EmuDeck", "",
             f"Actualizado: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC. "
             "Las gráficas no incluyen el día de hoy porque aún está incompleto.", ""]

    clones = [r for r in read_csv(CLONES_CSV) if r["date"] < today]
    lines += ["## Usuarios que actualizan el backend (clonados de git)", "",
              "| Backend | Únicos ayer | Clonados ayer | Únicos medios (7 días) |", "|---|---|---|---|"]
    for repo, label in BACKENDS.items():
        days = sorted((r for r in clones if r["repo"] == repo), key=lambda r: r["date"])
        if not days:
            lines.append(f"| {label} | – | – | – |")
            continue
        last = days[-1]
        week = days[-7:]
        average = round(sum(int(r["uniques"]) for r in week) / len(week))
        lines.append(f"| {label} | {last['uniques']} | {last['count']} | {average} |")
    lines.append("")
    for repo, label in BACKENDS.items():
        days = sorted((r for r in clones if r["repo"] == repo), key=lambda r: r["date"])[-CHART_DAYS:]
        if len(days) > 1:
            lines += [chart(f"Únicos diarios - {label}", [r["date"] for r in days], [int(r["uniques"]) for r in days], "Usuarios"), ""]

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
                lines += [chart(label, dates, values, "Arranques"), ""]
    else:
        lines += ["Hacen falta al menos dos días de datos para calcular arranques diarios.", ""]

    if problems:
        lines += ["## Avisos de la última ejecución", ""] + [f"- {p}" for p in problems] + [""]
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    """Collects today's data, saves it in data/ and rebuilds the README."""
    problems = []
    collect_clones(problems)
    collect_releases(problems)
    write_readme(problems)
    for text in problems:
        print(f"! {text}")


if __name__ == "__main__":
    main()
