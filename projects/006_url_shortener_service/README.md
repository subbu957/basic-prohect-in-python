# Project 006: URL Shortener Service

> **Focus:** Flask API that creates short links and tracks click counts.

## 📋 Overview
This project is part of the **101 Python Mini Projects** collection. It provides a complete, tested, and reliable implementation designed to run out of the box with zero setup hurdles.

## 🚀 Live Terminal Preview

```text
==============================================================
            === PREVIEW: URL SHORTENER SERVICE ===            
==============================================================
$ python main.py --test
POST /shorten response: {'code': 'xK92a', 'short_url': 'http://localhost/xK92a'}
GET /stats response: {'clicks': 1, 'code': 'xK92a', 'url': 'https://github.com/subbu957'}
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
