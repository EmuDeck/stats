#!/usr/bin/env python3
import json
import os
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = os.environ.get("GITHUB_REPOSITORY", "EmuDeck/stats")
TAG = "beacons"


def beacon_names():
    """Every beacon file the backends can download: system-<system>.txt and <app>-<platform>.txt."""
    config = json.loads((ROOT / "beacons.json").read_text(encoding="utf-8"))
    names = [f"system-{system}.txt" for system in config["systems"]]
    names += [f"{app}-{platform}.txt" for app in config["apps"] for platform in config["platforms"]]
    return names


def gh(*args, capture=False):
    """Runs a gh CLI command against this repo."""
    return subprocess.run(["gh", *args, "-R", REPO], check=True, capture_output=capture, text=True)


def main():
    """Creates the beacons release if needed and uploads the 1-byte files it is missing."""
    if subprocess.run(["gh", "release", "view", TAG, "-R", REPO], capture_output=True).returncode != 0:
        gh("release", "create", TAG, "--title", "Beacons", "--latest=false",
           "--notes", "1-byte files EmuDeck downloads to count systems and installed emulators. Do not delete them.")
    existing = {asset["name"] for asset in json.loads(gh("release", "view", TAG, "--json", "assets", capture=True).stdout)["assets"]}
    missing = [name for name in beacon_names() if name not in existing]
    if not missing:
        print("All beacons exist")
        return
    folder = Path(tempfile.mkdtemp())
    files = []
    for name in missing:
        path = folder / name
        path.write_text("1", encoding="utf-8")
        files.append(str(path))
    gh("release", "upload", TAG, *files)
    print(f"Uploaded {len(missing)} beacons")


if __name__ == "__main__":
    main()
