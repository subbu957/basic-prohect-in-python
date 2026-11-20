# -*- coding: utf-8 -*-
"""
6. URL Shortener Service
Flask API that creates short links and tracks click counts.
"""

from flask import Flask, request, redirect, jsonify
import secrets, sqlite3

app = Flask(__name__)
db = sqlite3.connect("links.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS links(code TEXT PRIMARY KEY, url TEXT, clicks INTEGER DEFAULT 0)")
db.commit()

@app.post("/shorten")
def shorten():
    data = request.json or {}
    url = data.get("url", "")
    code = secrets.token_urlsafe(5)
    db.execute("INSERT INTO links(code, url) VALUES(?, ?)", (code, url))
    db.commit()
    return jsonify({"code": code, "short_url": request.host_url + code})

@app.get("/<code>")
def go(code):
    row = db.execute("SELECT url FROM links WHERE code=?", (code,)).fetchone()
    if not row:
        return "Not found", 404
    db.execute("UPDATE links SET clicks=clicks+1 WHERE code=?", (code,))
    db.commit()
    return redirect(row[0])

@app.get("/stats/<code>")
def stats(code):
    row = db.execute("SELECT code, url, clicks FROM links WHERE code=?", (code,)).fetchone()
    return jsonify(dict(zip(["code", "url", "clicks"], row))) if row else ("Not found", 404)

if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        client = app.test_client()
        r1 = client.post("/shorten", json={"url": "https://github.com/subbu957"})
        print("POST /shorten response:", r1.json)
        code = r1.json["code"]
        client.get(f"/{code}")
        r2 = client.get(f"/stats/{code}")
        print("GET /stats response:", r2.json)
    else:
        app.run(debug=True, port=5000)
