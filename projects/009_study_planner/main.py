# -*- coding: utf-8 -*-
"""
9. Study Planner
Priority-based study planner with deadlines, completion tracking and daily agenda.
"""

import sqlite3
from datetime import date

db = sqlite3.connect("study.db")
db.execute("""CREATE TABLE IF NOT EXISTS tasks(
 id INTEGER PRIMARY KEY, subject TEXT, task TEXT, due TEXT, priority INTEGER, done INTEGER DEFAULT 0)""")
db.commit()

def add():
    s = input("Subject: ").strip()
    t = input("Task: ").strip()
    d = input("Due YYYY-MM-DD: ").strip() or str(date.today())
    p = int(input("Priority 1-5 [3]: ").strip() or 3)
    db.execute("INSERT INTO tasks(subject,task,due,priority) VALUES(?,?,?,?)", (s, t, d, p))
    db.commit()
    print("[+] Study task scheduled.")

def agenda():
    rows = db.execute("""SELECT id, subject, task, due, priority FROM tasks
                         WHERE done=0 ORDER BY due, priority DESC""").fetchall()
    if not rows:
        print("No active pending study tasks.")
    else:
        print(f"\n{'ID':<4} {'Subject':<18} {'Task':<28} {'Due Date':<12} Priority")
        print("-" * 70)
        for r in rows:
            print(f"{r[0]:<4} {r[1]:<18} {r[2]:<28} {r[3]:<12} {r[4]}")

def done():
    i = input("Task ID to complete: ").strip()
    db.execute("UPDATE tasks SET done=1 WHERE id=?", (i,))
    db.commit()
    print(f"[+] Task {i} marked as completed!")

def main():
    while True:
        print("\n1 Add  2 Agenda  3 Complete  4 Exit")
        c = input("> ").strip()
        if c == "1": add()
        elif c == "2": agenda()
        elif c == "3": done()
        else: break

if __name__ == "__main__":
    main()
