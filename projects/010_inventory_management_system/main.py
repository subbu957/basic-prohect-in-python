# -*- coding: utf-8 -*-
"""
10. Inventory Management System
SQLite inventory with stock alerts, purchase entries and sales deductions.
"""

import sqlite3

db = sqlite3.connect("inventory.db")
db.execute("""CREATE TABLE IF NOT EXISTS items(
 sku TEXT PRIMARY KEY, name TEXT, stock INTEGER, price REAL, reorder INTEGER)""")
db.commit()

def add_item():
    sku = input("SKU: ").strip()
    name = input("Name: ").strip()
    stock = int(input("Stock: ").strip() or 0)
    price = float(input("Price: ").strip() or 0.0)
    reorder = int(input("Reorder level: ").strip() or 10)
    db.execute("INSERT OR REPLACE INTO items VALUES(?,?,?,?,?)", (sku, name, stock, price, reorder))
    db.commit()
    print(f"[+] Item '{name}' saved.")

def sell():
    sku = input("SKU: ").strip()
    qty = int(input("Qty to sell: ").strip() or 1)
    row = db.execute("SELECT stock, name FROM items WHERE sku=?", (sku,)).fetchone()
    if not row or row[0] < qty:
        print("[!] Insufficient stock or SKU not found.")
        return
    db.execute("UPDATE items SET stock=stock-? WHERE sku=?", (qty, sku))
    db.commit()
    print(f"[+] Sold {qty} units of {row[1]}. Remaining: {row[0] - qty}")

def report():
    print(f"\n{'SKU':<10} {'Name':<22} {'Stock':<8} {'Price':<10} {'Reorder':<8} Status")
    print("-" * 68)
    for r in db.execute("SELECT sku, name, stock, price, reorder FROM items ORDER BY stock"):
        flag = " [LOW STOCK]" if r[2] <= r[4] else " [OK]"
        print(f"{r[0]:<10} {r[1]:<22} {r[2]:<8} ${r[3]:<9.2f} {r[4]:<8}{flag}")

def main():
    while True:
        print("\n1 Add/Update  2 Sell  3 Report  4 Exit")
        c = input("> ").strip()
        if c == "1": add_item()
        elif c == "2": sell()
        elif c == "3": report()
        else: break

if __name__ == "__main__":
    main()
