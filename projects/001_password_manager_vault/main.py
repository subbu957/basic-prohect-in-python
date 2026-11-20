# -*- coding: utf-8 -*-
"""
1. Password Manager Vault
CLI app that creates a local encrypted-style vault using PBKDF2 + Fernet.
"""

import os, json, base64, getpass, sys
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac

FILE = "vault.json"

def key_from_password(password: str, salt: bytes) -> bytes:
    raw = pbkdf2_hmac("sha256", password.encode(), salt, 200_000, 32)
    return base64.urlsafe_b64encode(raw)

def load():
    if not os.path.exists(FILE):
        return None
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def prompt_pass(msg="Password: "):
    if not sys.stdin.isatty():
        line = sys.stdin.readline()
        return line.strip() if line else ""
    try:
        return getpass.getpass(msg)
    except Exception:
        return input(msg)

def main():
    print("=== Password Manager Vault ===")
    master = prompt_pass("Master password: ")
    data = load()
    if data:
        salt = base64.b64decode(data["salt"])
        key = key_from_password(master, salt)
        f = Fernet(key)
        try:
            records = json.loads(f.decrypt(data["blob"].encode()).decode())
        except Exception:
            raise SystemExit("Wrong password or damaged vault.")
    else:
        print("[*] Creating a new encrypted vault...")
        salt = os.urandom(16)
        key = key_from_password(master, salt)
        f = Fernet(key)
        records = {}

    while True:
        print("\n1.Add  2.List  3.Get  4.Delete  5.Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            site = input("Site: ").strip()
            user = input("Username: ").strip()
            pwd = prompt_pass("Password: ")
            records[site] = {"username": user, "password": pwd}
            print(f"[+] Stored credentials for {site}")
        elif choice == "2":
            if not records:
                print("[!] No credentials stored yet.")
            else:
                print("--- Stored Sites ---")
                print(*records.keys(), sep="\n")
        elif choice == "3":
            site = input("Site: ").strip()
            item = records.get(site)
            if item:
                print(f"Username: {item['username']} | Password: {item['password']}")
            else:
                print("Not found")
        elif choice == "4":
            site = input("Site to delete: ").strip()
            if records.pop(site, None):
                print(f"[-] Deleted {site}")
            else:
                print("Not found")
        elif choice == "5":
            blob = f.encrypt(json.dumps(records).encode()).decode()
            with open(FILE, "w", encoding="utf-8") as fp:
                json.dump({"salt": base64.b64encode(salt).decode(), "blob": blob}, fp)
            print("[*] Vault saved securely. Goodbye!")
            break

if __name__ == "__main__":
    main()
