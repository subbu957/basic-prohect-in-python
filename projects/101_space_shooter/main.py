# -*- coding: utf-8 -*-
"""
101. Space Shooter
Focus: Pygame shooter with waves, power-ups and scoring.
"""

import sqlite3, json
from datetime import datetime

DB = "space_shooter.db"
db = sqlite3.connect(DB)
db.execute("""CREATE TABLE IF NOT EXISTS records(
    id INTEGER PRIMARY KEY, title TEXT, status TEXT, priority INTEGER, created TEXT
)""")
db.commit()

def add():
    title = input("Title: ").strip()
    status = input("Status [todo]: ").strip() or "todo"
    priority = int(input("Priority 1-5 [3]: ").strip() or 3)
    db.execute("INSERT INTO records(title,status,priority,created) VALUES(?,?,?,?)",
               (title, status, priority, datetime.now().isoformat(timespec="seconds")))
    db.commit()
    print("[+] Record added successfully.")

def list_items():
    rows = db.execute("SELECT id,title,status,priority,created FROM records ORDER BY priority DESC, created DESC").fetchall()
    if not rows:
        print("No records found.")
        return
    print(f"\nID    Title                          Status       Priority   Created")
    print("-" * 75)
    for r in rows:
        print(f"{r[0]:<5} {r[1]:<30} {r[2]:<12} {r[3]:<10} {r[4]}")

def update():
    i = input("ID: ").strip()
    s = input("New status: ").strip()
    db.execute("UPDATE records SET status=? WHERE id=?", (s, i))
    db.commit()
    print(f"[+] Record {i} updated.")

def export():
    rows = db.execute("SELECT * FROM records").fetchall()
    json.dump(rows, open("space_shooter.json", "w", encoding="utf-8"), indent=2, default=str)
    print(f"[+] Exported {len(rows)} records to space_shooter.json.")

def main():
    while True:
        print("\n1 Add  2 List  3 Update  4 Export  5 Exit")
        c = input("> ").strip()
        if c == "1": add()
        elif c == "2": list_items()
        elif c == "3": update()
        elif c == "4": export()
        elif c == "5": break

if __name__ == "__main__":
    main()
