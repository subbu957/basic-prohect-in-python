# -*- coding: utf-8 -*-
"""
101 Python Mini Projects - Interactive Preview Dashboard & Runner
Run this script to interactively explore and test any of the 101 projects!
Usage:
    python preview_dashboard.py
"""

import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = BASE_DIR / "projects"

def get_project_list():
    folders = sorted([f for f in PROJECTS_DIR.iterdir() if f.is_dir()])
    projects = []
    for f in folders:
        readme = f / "README.md"
        focus = ""
        title = f.name
        if readme.exists():
            for line in readme.read_text(encoding="utf-8").splitlines():
                if line.startswith("# Project"):
                    title = line.replace("#", "").strip()
                elif line.startswith("> **Focus:**"):
                    focus = line.replace("> **Focus:**", "").strip()
        projects.append({
            "folder": f,
            "title": title,
            "focus": focus,
            "num": int(f.name[:3]) if f.name[:3].isdigit() else 0
        })
    return projects

def display_menu():
    projects = get_project_list()
    print("=" * 76)
    print("           🌟 101 PYTHON MINI PROJECTS - INTERACTIVE DASHBOARD 🌟")
    print("=" * 76)
    print("Commands:")
    print("  <number>        : View details and preview for project (1 to 101)")
    print("  run <number>    : Run the project script directly")
    print("  list [query]    : Search or list projects")
    print("  test            : Run the automated test suite across all 101 projects")
    print("  q / exit        : Exit dashboard\n")

    while True:
        try:
            cmd = input("Dashboard > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not cmd:
            continue
        if cmd.lower() in ["q", "exit", "quit"]:
            print("Goodbye!")
            break
        elif cmd.lower() == "test":
            subprocess.run([sys.executable, "run_all_tests.py"], cwd=str(BASE_DIR))
        elif cmd.lower().startswith("list"):
            parts = cmd.split(maxsplit=1)
            query = parts[1].lower() if len(parts) > 1 else ""
            matches = [p for p in projects if query in p["title"].lower() or query in p["focus"].lower()]
            print(f"\nFound {len(matches)} projects:")
            for p in matches[:25]:
                print(f"  [{p['num']:03d}] {p['title']:<38} | {p['focus']}")
            if len(matches) > 25:
                print(f"  ... and {len(matches) - 25} more. Refine your query with: list <term>")
            print()
        elif cmd.lower().startswith("run "):
            parts = cmd.split(maxsplit=1)
            try:
                num = int(parts[1])
                match = next((p for p in projects if p["num"] == num), None)
                if match:
                    print(f"\n🚀 Launching {match['title']} ({match['folder'].name}/main.py)...")
                    subprocess.run([sys.executable, "main.py"], cwd=str(match["folder"]))
                else:
                    print(f"Project #{num} not found.")
            except ValueError:
                print("Please specify a valid project number, e.g.: run 1")
        elif cmd.isdigit():
            num = int(cmd)
            match = next((p for p in projects if p["num"] == num), None)
            if match:
                readme = match["folder"] / "README.md"
                if readme.exists():
                    print("\n" + "=" * 76)
                    print(readme.read_text(encoding="utf-8"))
                    print("=" * 76)
                    run_now = input(f"Run {match['title']} now? [y/N]: ").strip().lower()
                    if run_now == "y":
                        subprocess.run([sys.executable, "main.py"], cwd=str(match["folder"]))
                else:
                    print(f"No README found for {match['title']}.")
            else:
                print(f"Project #{num} not found. Enter 1 to 101.")
        else:
            print("Unknown command. Type a number (1-101), 'run <num>', 'list <query>', 'test', or 'q'.")

if __name__ == "__main__":
    display_menu()
