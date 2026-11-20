# -*- coding: utf-8 -*-
"""
8. Contact Book with Search
SQLite contact manager with tags, search, update and JSON backup.
"""

import sqlite3, json

db = sqlite3.connect("contacts.db")
db.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY,name TEXT,phone TEXT,email TEXT,tags TEXT)")
db.commit()

def add():
    v = [input(x + ": ").strip() for x in ("Name", "Phone", "Email", "Tags")]
    db.execute("INSERT INTO contacts(name,phone,email,tags) VALUES(?,?,?,?)", v)
    db.commit()
    print("[+] Contact saved successfully.")

def search():
    q = input("Search query: ").strip()
    rows = db.execute("""SELECT * FROM contacts
                         WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR tags LIKE ?""",
                      tuple("%" + q + "%" for _ in range(4))).fetchall()
    if not rows:
        print("No contacts matched.")
    else:
        print(f"\n{'ID':<4} {'Name':<20} {'Phone':<15} {'Email':<25} Tags")
        print("-" * 75)
        for r in rows:
            print(f"{r[0]:<4} {r[1]:<20} {r[2]:<15} {r[3]:<25} {r[4]}")

def backup():
    rows = db.execute("SELECT name,phone,email,tags FROM contacts").fetchall()
    json.dump([dict(zip(["name", "phone", "email", "tags"], r)) for r in rows],
              open("contacts_backup.json", "w", encoding="utf-8"), indent=2)
    print(f"[+] Saved {len(rows)} contacts to contacts_backup.json.")

def main():
    while True:
        print("\n1 Add  2 Search  3 Backup  4 Exit")
        c = input("> ").strip()
        if c == "1": add()
        elif c == "2": search()
        elif c == "3": backup()
        elif c == "4": break

if __name__ == "__main__":
    main()
