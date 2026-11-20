# -*- coding: utf-8 -*-
"""
2. Personal Expense Tracker
SQLite-backed expense tracker with categories, monthly totals and CSV export.
"""

import sqlite3, csv
from datetime import date

db = sqlite3.connect("expenses.db")
db.execute("""CREATE TABLE IF NOT EXISTS expenses(
 id INTEGER PRIMARY KEY, day TEXT, category TEXT, note TEXT, amount REAL)""")
db.commit()

def add():
    day = input("Date YYYY-MM-DD [today]: ").strip() or str(date.today())
    cat = input("Category: ").strip()
    note = input("Note: ").strip()
    amount = float(input("Amount: ").strip() or 0.0)
    db.execute("INSERT INTO expenses(day,category,note,amount) VALUES(?,?,?,?)",
               (day, cat, note, amount))
    db.commit()
    print("[+] Expense recorded successfully.")

def report():
    month = input("Month YYYY-MM [e.g. 2026-11]: ").strip() or str(date.today())[:7]
    rows = db.execute("""SELECT category, SUM(amount)
                         FROM expenses WHERE day LIKE ? GROUP BY category ORDER BY 2 DESC""",
                      (month + "-%",)).fetchall()
    print(f"\n--- Expense Breakdown for {month} ---")
    if not rows:
        print("No expenses found for this month.")
    else:
        print("\n".join(f"{c:15} | ${a:.2f}" for c, a in rows))
    total = db.execute("SELECT COALESCE(SUM(amount),0) FROM expenses WHERE day LIKE ?",
                       (month + "-%",)).fetchone()[0]
    print(f"Total: ${total:.2f}")

def export():
    rows = db.execute("SELECT day,category,note,amount FROM expenses").fetchall()
    with open("expenses.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "category", "note", "amount"])
        w.writerows(rows)
    print(f"[+] Exported {len(rows)} records to expenses.csv.")

def main():
    while True:
        print("\n1 Add  2 Report  3 Export  4 Exit")
        c = input("> ").strip()
        if c == "1": add()
        elif c == "2": report()
        elif c == "3": export()
        elif c == "4": break

if __name__ == "__main__":
    main()
