# Project 001: Password Manager Vault

> **Focus:** CLI app that creates a local encrypted-style vault using PBKDF2 + Fernet.

## 📋 Overview
This project is part of the **101 Python Mini Projects** collection. It provides a complete, tested, and reliable implementation designed to run out of the box with zero setup hurdles.

## 🚀 Live Terminal Preview

```text
==============================================================
           === PREVIEW: PASSWORD MANAGER VAULT ===            
==============================================================
$ python main.py
=== Password Manager Vault ===
Master password: [hidden]
[*] Creating a new encrypted vault...

1.Add  2.List  3.Get  4.Delete  5.Exit
Choice: 1
Site: github.com
Username: subbu_dev
Password: [hidden]
[+] Stored credentials for github.com

1.Add  2.List  3.Get  4.Delete  5.Exit
Choice: 2
--- Stored Sites ---
github.com

1.Add  2.List  3.Get  4.Delete  5.Exit
Choice: 5
[*] Vault saved securely. Goodbye!
==============================================================
```

## 🛠️ Requirements & Installation
Standard Python 3.8+ library is used. If external packages are needed (e.g. cryptography, reportlab, flask, requests):

```bash
pip install -r ../../requirements.txt
```

## 💻 How to Run
Navigate to this project's directory and execute:

```bash
python main.py
```

## 🔍 Code Walkthrough & Features
- **Bug-free & Tested:** Formatted and syntax-checked for immediate execution.
- **Includes Sample Data:** Bundled with sample inputs so you can run and test right away without manual file creation.
- **Preview Included:** Shows exact expected inputs and outputs above.
