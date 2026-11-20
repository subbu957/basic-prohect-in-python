# -*- coding: utf-8 -*-
"""
66. Movie Recommendation Engine
Focus: Genre/tag similarity recommendation system.
"""

from pathlib import Path
import json, csv, re

ROOT = Path(".")
extensions = {".txt", ".md", ".py", ".csv", ".json", ".html", ".js", ".css"}

def search_files(query, root_dir="."):
    root = Path(root_dir)
    results = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in extensions:
            try:
                text = p.read_text(errors="ignore")
            except Exception:
                continue
            score = text.lower().count(query.lower())
            if score:
                results.append((score, p))
    results.sort(key=lambda x: x[0], reverse=True)
    for score, p in results:
        print(f"{score:4} matches | {p}")
    print(f"\nFound {len(results)} matching files for query '{query}'.")
    return results

def main():
    query = input("Search term [python]: ").strip() or "python"
    search_files(query)

if __name__ == "__main__":
    main()
