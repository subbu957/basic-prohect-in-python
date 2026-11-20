# Project 003: File Organizer Pro

> **Focus:** Desktop folder organizer with extension rules, duplicate detection and dry-run mode.

## 📋 Overview
This project is part of the **101 Python Mini Projects** collection. It provides a complete, tested, and reliable implementation designed to run out of the box with zero setup hurdles.

## 🚀 Live Terminal Preview

```text
==============================================================
             === PREVIEW: FILE ORGANIZER PRO ===              
==============================================================
$ python main.py
Folder to organize [demo_files]: demo_files
Dry run? y/n [y]: y
Scanning target: demo_files (dry_run=True)
  invoice.pdf -> Documents/invoice.pdf
  photo.jpg -> Images/photo.jpg
[DUPLICATE] photo_dup.jpg => matched photo.jpg
  report.docx -> Documents/report.docx
  song.mp3 -> Audio/song.mp3
[*] Organization process completed.
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
