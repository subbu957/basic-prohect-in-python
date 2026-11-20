# -*- coding: utf-8 -*-
"""
3. File Organizer Pro
Desktop folder organizer with extension rules, duplicate detection and dry-run mode.
"""

from pathlib import Path
import hashlib, shutil

rules = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def organize(root_dir="demo_files", dry_run=True):
    ROOT = Path(root_dir).expanduser().resolve()
    ROOT.mkdir(parents=True, exist_ok=True)
    seen = {}
    print(f"Scanning target: {ROOT} (dry_run={dry_run})")
    for p in ROOT.iterdir():
        if not p.is_file(): continue
        folder = next((k for k, v in rules.items() if p.suffix.lower() in v), "Others")
        target = ROOT / folder
        target.mkdir(exist_ok=True)
        key = (p.stat().st_size, digest(p))
        if key in seen:
            print(f"[DUPLICATE] {p.name} => matched {seen[key].name}")
            continue
        seen[key] = p
        dest = target / p.name
        print(f"  {p.name} -> {folder}/{p.name}")
        if not dry_run:
            shutil.move(str(p), str(dest))
    print("[*] Organization process completed.")

def main():
    root_input = input("Folder to organize [demo_files]: ").strip() or "demo_files"
    dry_input = input("Dry run? y/n [y]: ").strip().lower()
    dry_run = dry_input != "n"
    organize(root_input, dry_run)

if __name__ == "__main__":
    main()
