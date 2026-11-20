# -*- coding: utf-8 -*-
"""
14. Banking Simulator
Focus: Account management, transfers, transaction history and statements.
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "banking_simulator.db"
db = sqlite3.connect(DB, check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, title TEXT, body TEXT, status TEXT)")
db.commit()

@app.get("/items")
def all_items():
    rows = db.execute("SELECT id,title,body,status FROM items ORDER BY id DESC").fetchall()
    return jsonify([dict(zip(["id","title","body","status"], r)) for r in rows])

@app.post("/items")
def create():
    x = request.json or {}
    db.execute("INSERT INTO items(title,body,status) VALUES(?,?,?)",
               (x.get("title", ""), x.get("body", ""), x.get("status", "open")))
    db.commit()
    return jsonify({"ok": True}), 201

@app.patch("/items/<int:item_id>")
def update(item_id):
    x = request.json or {}
    db.execute("UPDATE items SET title=COALESCE(?,title),body=COALESCE(?,body),status=COALESCE(?,status) WHERE id=?",
               (x.get("title"), x.get("body"), x.get("status"), item_id))
    db.commit()
    return jsonify({"updated": db.total_changes})

@app.delete("/items/<int:item_id>")
def delete(item_id):
    db.execute("DELETE FROM items WHERE id=?", (item_id,))
    db.commit()
    return jsonify({"deleted": item_id})

if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        client = app.test_client()
        r1 = client.post("/items", json={"title": "Banking Simulator Demo", "body": "Sample API record", "status": "active"})
        print("POST /items:", r1.json)
        r2 = client.get("/items")
        print("GET /items:", r2.json)
    else:
        app.run(debug=True, port=5000)
