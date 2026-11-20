# -*- coding: utf-8 -*-
"""
94. Flashcard Generator
Focus: Turn notes into structured flashcards.
"""

import argparse, shutil, hashlib
from pathlib import Path

def digest(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1024 * 1024), b""):
            h.update(c)
    return h.hexdigest()

def sync_backup(source_dir, backup_dir, dry_run=False):
    source = Path(source_dir).resolve()
    backup = Path(backup_dir).resolve()
    print(f"Syncing from '{source}' -> '{backup}' (dry_run={dry_run})")
    copied = 0
    for src in source.rglob("*"):
        if not src.is_file(): continue
        dst = backup / src.relative_to(source)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists() and digest(src) == digest(dst):
            continue
        print(f"  {src.name} -> {dst.name}")
        if not dry_run:
            shutil.copy2(src, dst)
        copied += 1
    print(f"Backup complete. {copied} files synced.")

def main():
    parser = argparse.ArgumentParser(description="Flashcard Generator Backup Sync")
    parser.add_argument("source", nargs="?", default="demo_source", type=Path, help="Source directory")
    parser.add_argument("backup", nargs="?", default="demo_backup", type=Path, help="Backup destination directory")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without copying")
    args = parser.parse_args()

    # Create demo files if demo_source is used and empty
    if str(args.source) == "demo_source" and not args.source.exists():
        args.source.mkdir(parents=True, exist_ok=True)
        (args.source / "project_asset.txt").write_text("Asset file for backup sync.", encoding="utf-8")
        (args.source / "config.json").write_text('{"version": 1.0}', encoding="utf-8")

    sync_backup(args.source, args.backup, args.dry_run)

if __name__ == "__main__":
    main()
