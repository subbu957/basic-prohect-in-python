# 101 Python Mini Projects 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-101%2F101%20passing-brightgreen.svg)](run_all_tests.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Projects](https://img.shields.io/badge/projects-101%20complete-purple.svg)](#-complete-project-catalog)

A curated, project-level repository containing **101 fully functional Python mini-projects** inspired by the *"101 Python Mini Projects"* full source code book.

Every single project includes:
- ✅ **Complete, Bug-Free Source Code (`main.py`)**: All PDF layout glitches, broken string literals, missing imports, and font encoding issues have been resolved.
- 📺 **Live Output Preview**: Dedicated visual execution output in every project folder.
- 📦 **Sample Data & Resources**: Bundled with SQLite databases, JSON orders/quizzes, and CSV datasets so you can run any project instantly without manual file preparation.
- 🧪 **100% Automated Test Suite**: Verified by `run_all_tests.py` with 101/101 passing tests!
- 💻 **Interactive CLI Runner**: Run any project effortlessly via `preview_dashboard.py`.
- 🌐 **Web Preview Showcase**: Interactive browser dashboard available at `preview.html`.

---

## ⚡ Quick Start

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/subbu957/basic-prohect-in-python.git
cd basic-prohect-in-python
pip install -r requirements.txt
```

### 2. Run the Interactive Dashboard
Explore, search, and run any of the 101 projects from your terminal:

```bash
python preview_dashboard.py
```

### 3. Open Web Showcase
Open `preview.html` in your browser to search, inspect code, and see interactive previews for all 101 projects.

### 4. Run the Full Test Suite
Verify that every project compiles and executes with zero errors:

```bash
python run_all_tests.py
```

---

## 🗂️ Project Directory Structure

```text
basic-prohect-in-python/
│
├── preview_dashboard.py      # Interactive terminal dashboard & runner
├── preview.html              # Responsive web showcase with live previews & code viewer
├── run_all_tests.py          # Automated verification script (101/101 tests passing)
├── requirements.txt          # Shared dependencies (cryptography, reportlab, flask, requests)
├── calculate_your_age.py     # Interactive Age Calculator
│
└── projects/
    ├── 001_password_manager_vault/
    │   ├── main.py
    │   ├── README.md         # Detailed overview & terminal execution preview
    │   └── vault.json
    ├── 002_personal_expense_tracker/
    │   ├── main.py
    │   ├── README.md
    │   └── expenses.db
    ├── ...
    └── 101_space_shooter/
        ├── main.py
        ├── README.md
        └── space_shooter.db
```

---

## 📚 Complete Project Catalog (1 – 101)

| # | Project Name | Focus & Description | Type / Tech | Preview |
|---|--------------|---------------------|-------------|---------|
| **001** | [Password Manager Vault](projects/001_password_manager_vault) | CLI app that creates a local encrypted-style vault using PBKDF2 + Fernet. | `Custom Architecture` | [View Preview 📺](projects/001_password_manager_vault/README.md#%EF%B8%8F-live-terminal-preview) |
| **002** | [Personal Expense Tracker](projects/002_personal_expense_tracker) | SQLite-backed expense tracker with categories, monthly totals and CSV export. | `Custom Architecture` | [View Preview 📺](projects/002_personal_expense_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **003** | [File Organizer Pro](projects/003_file_organizer_pro) | Desktop folder organizer with extension rules, duplicate detection and dry-run mode. | `Custom Architecture` | [View Preview 📺](projects/003_file_organizer_pro/README.md#%EF%B8%8F-live-terminal-preview) |
| **004** | [PDF Invoice Generator](projects/004_pdf_invoice_generator) | Generate professional invoices from a JSON order file. | `Custom Architecture` | [View Preview 📺](projects/004_pdf_invoice_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **005** | [Quiz Master App](projects/005_quiz_master_app) | Timed JSON-driven quiz with scoring, review and leaderboard storage. | `Custom Architecture` | [View Preview 📺](projects/005_quiz_master_app/README.md#%EF%B8%8F-live-terminal-preview) |
| **006** | [URL Shortener Service](projects/006_url_shortener_service) | Flask API that creates short links and tracks click counts. | `Custom Architecture` | [View Preview 📺](projects/006_url_shortener_service/README.md#%EF%B8%8F-live-terminal-preview) |
| **007** | [Weather Dashboard](projects/007_weather_dashboard) | CLI weather dashboard using Open-Meteo with caching and forecast summaries. | `Custom Architecture` | [View Preview 📺](projects/007_weather_dashboard/README.md#%EF%B8%8F-live-terminal-preview) |
| **008** | [Contact Book with Search](projects/008_contact_book_with_search) | SQLite contact manager with tags, search, update and JSON backup. | `Custom Architecture` | [View Preview 📺](projects/008_contact_book_with_search/README.md#%EF%B8%8F-live-terminal-preview) |
| **009** | [Study Planner](projects/009_study_planner) | Priority-based study planner with deadlines, completion tracking and daily agenda. | `Custom Architecture` | [View Preview 📺](projects/009_study_planner/README.md#%EF%B8%8F-live-terminal-preview) |
| **010** | [Inventory Management System](projects/010_inventory_management_system) | SQLite inventory with stock alerts, purchase entries and sales deductions. | `Custom Architecture` | [View Preview 📺](projects/010_inventory_management_system/README.md#%EF%B8%8F-live-terminal-preview) |
| **011** | [Pomodoro Productivity Desktop](projects/011_pomodoro_productivity_desktop) | GUI productivity timer with session history. | `SQLite Record Engine` | [View Preview 📺](projects/011_pomodoro_productivity_desktop/README.md#%EF%B8%8F-live-terminal-preview) |
| **012** | [Markdown Notes Manager](projects/012_markdown_notes_manager) | Searchable markdown notebook with tags and index. | `Document Search Engine` | [View Preview 📺](projects/012_markdown_notes_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **013** | [Habit Tracker](projects/013_habit_tracker) | SQLite habit tracker with streak calculations. | `CSV Quality Auditor` | [View Preview 📺](projects/013_habit_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **014** | [Banking Simulator](projects/014_banking_simulator) | Account management, transfers, transaction history and statements. | `Flask REST Microservice` | [View Preview 📺](projects/014_banking_simulator/README.md#%EF%B8%8F-live-terminal-preview) |
| **015** | [Library Management System](projects/015_library_management_system) | Books, members, lending, returns and overdue reports. | `Statistical Profiler` | [View Preview 📺](projects/015_library_management_system/README.md#%EF%B8%8F-live-terminal-preview) |
| **016** | [Hotel Booking Manager](projects/016_hotel_booking_manager) | Rooms, reservations, check-in/check-out and billing. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/016_hotel_booking_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **017** | [Cinema Ticket Booking](projects/017_cinema_ticket_booking) | Seat map, bookings, cancellation and receipt generation. | `SQLite Record Engine` | [View Preview 📺](projects/017_cinema_ticket_booking/README.md#%EF%B8%8F-live-terminal-preview) |
| **018** | [Restaurant POS](projects/018_restaurant_pos) | Menu, cart, taxes, discounts and daily sales report. | `Document Search Engine` | [View Preview 📺](projects/018_restaurant_pos/README.md#%EF%B8%8F-live-terminal-preview) |
| **019** | [Invoice & GST Calculator](projects/019_invoice_and_gst_calculator) | Invoice builder with Indian GST breakdown and PDF export. | `CSV Quality Auditor` | [View Preview 📺](projects/019_invoice_and_gst_calculator/README.md#%EF%B8%8F-live-terminal-preview) |
| **020** | [Attendance Management](projects/020_attendance_management) | Student attendance database with percentage reports. | `Flask REST Microservice` | [View Preview 📺](projects/020_attendance_management/README.md#%EF%B8%8F-live-terminal-preview) |
| **021** | [Employee Payroll System](projects/021_employee_payroll_system) | Salary calculation, deductions, payslip generation. | `Statistical Profiler` | [View Preview 📺](projects/021_employee_payroll_system/README.md#%EF%B8%8F-live-terminal-preview) |
| **022** | [Resume Builder](projects/022_resume_builder) | JSON-driven resume builder exporting polished PDF. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/022_resume_builder/README.md#%EF%B8%8F-live-terminal-preview) |
| **023** | [Job Application Tracker](projects/023_job_application_tracker) | Track companies, stages, deadlines and follow-ups. | `SQLite Record Engine` | [View Preview 📺](projects/023_job_application_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **024** | [Interview Question Bank](projects/024_interview_question_bank) | Searchable categorized interview questions with quiz mode. | `Document Search Engine` | [View Preview 📺](projects/024_interview_question_bank/README.md#%EF%B8%8F-live-terminal-preview) |
| **025** | [DSA Practice Tracker](projects/025_dsa_practice_tracker) | Track problems, difficulty, patterns and revision dates. | `CSV Quality Auditor` | [View Preview 📺](projects/025_dsa_practice_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **026** | [Code Snippet Manager](projects/026_code_snippet_manager) | Tagged snippet vault with full-text search. | `Flask REST Microservice` | [View Preview 📺](projects/026_code_snippet_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **027** | [Git Commit Analyzer](projects/027_git_commit_analyzer) | Analyze a local Git repository and produce contribution reports. | `Statistical Profiler` | [View Preview 📺](projects/027_git_commit_analyzer/README.md#%EF%B8%8F-live-terminal-preview) |
| **028** | [Log File Analyzer](projects/028_log_file_analyzer) | Parse application logs and generate error summaries. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/028_log_file_analyzer/README.md#%EF%B8%8F-live-terminal-preview) |
| **029** | [Website Uptime Monitor](projects/029_website_uptime_monitor) | Periodically check URLs and save availability history. | `SQLite Record Engine` | [View Preview 📺](projects/029_website_uptime_monitor/README.md#%EF%B8%8F-live-terminal-preview) |
| **030** | [Broken Link Checker](projects/030_broken_link_checker) | Crawl a website and report broken internal links. | `Document Search Engine` | [View Preview 📺](projects/030_broken_link_checker/README.md#%EF%B8%8F-live-terminal-preview) |
| **031** | [Website Sitemap Generator](projects/031_website_sitemap_generator) | Crawl internal pages and create sitemap.xml. | `CSV Quality Auditor` | [View Preview 📺](projects/031_website_sitemap_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **032** | [Web Scraper to CSV](projects/032_web_scraper_to_csv) | Extract structured product/article data into CSV. | `Flask REST Microservice` | [View Preview 📺](projects/032_web_scraper_to_csv/README.md#%EF%B8%8F-live-terminal-preview) |
| **033** | [News Aggregator](projects/033_news_aggregator) | Fetch RSS feeds, deduplicate and categorize headlines. | `Statistical Profiler` | [View Preview 📺](projects/033_news_aggregator/README.md#%EF%B8%8F-live-terminal-preview) |
| **034** | [Email Newsletter Builder](projects/034_email_newsletter_builder) | Build HTML newsletters from templates and data. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/034_email_newsletter_builder/README.md#%EF%B8%8F-live-terminal-preview) |
| **035** | [QR Code Event Check-in](projects/035_qr_code_event_check_in) | Generate attendee QR codes and scan/check-in records. | `SQLite Record Engine` | [View Preview 📺](projects/035_qr_code_event_check_in/README.md#%EF%B8%8F-live-terminal-preview) |
| **036** | [PDF Merger & Splitter](projects/036_pdf_merger_and_splitter) | GUI tool for merging and splitting PDF documents. | `Document Search Engine` | [View Preview 📺](projects/036_pdf_merger_and_splitter/README.md#%EF%B8%8F-live-terminal-preview) |
| **037** | [Image Batch Processor](projects/037_image_batch_processor) | Resize, watermark and compress folders of images. | `CSV Quality Auditor` | [View Preview 📺](projects/037_image_batch_processor/README.md#%EF%B8%8F-live-terminal-preview) |
| **038** | [Duplicate Photo Finder](projects/038_duplicate_photo_finder) | Perceptual hashing to find visually similar photos. | `Flask REST Microservice` | [View Preview 📺](projects/038_duplicate_photo_finder/README.md#%EF%B8%8F-live-terminal-preview) |
| **039** | [Video Metadata Catalog](projects/039_video_metadata_catalog) | Catalog video metadata and searchable library. | `Statistical Profiler` | [View Preview 📺](projects/039_video_metadata_catalog/README.md#%EF%B8%8F-live-terminal-preview) |
| **040** | [Audio Playlist Manager](projects/040_audio_playlist_manager) | Manage playlists and generate M3U files. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/040_audio_playlist_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **041** | [YouTube Download Queue](projects/041_youtube_download_queue) | Queue public video URLs for local processing. | `SQLite Record Engine` | [View Preview 📺](projects/041_youtube_download_queue/README.md#%EF%B8%8F-live-terminal-preview) |
| **042** | [Personal Knowledge Base](projects/042_personal_knowledge_base) | Local searchable notes with backlinks. | `Document Search Engine` | [View Preview 📺](projects/042_personal_knowledge_base/README.md#%EF%B8%8F-live-terminal-preview) |
| **043** | [Password Strength Auditor](projects/043_password_strength_auditor) | Score passwords locally with entropy rules. | `CSV Quality Auditor` | [View Preview 📺](projects/043_password_strength_auditor/README.md#%EF%B8%8F-live-terminal-preview) |
| **044** | [OTP Authenticator Demo](projects/044_otp_authenticator_demo) | Generate TOTP codes for locally stored demo secrets. | `Flask REST Microservice` | [View Preview 📺](projects/044_otp_authenticator_demo/README.md#%EF%B8%8F-live-terminal-preview) |
| **045** | [Secure File Locker](projects/045_secure_file_locker) | Encrypt/decrypt user-selected files with a password. | `Statistical Profiler` | [View Preview 📺](projects/045_secure_file_locker/README.md#%EF%B8%8F-live-terminal-preview) |
| **046** | [Clipboard History Manager](projects/046_clipboard_history_manager) | Desktop clipboard history with search. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/046_clipboard_history_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **047** | [Screenshot Organizer](projects/047_screenshot_organizer) | Capture screenshots and auto-classify by date. | `SQLite Record Engine` | [View Preview 📺](projects/047_screenshot_organizer/README.md#%EF%B8%8F-live-terminal-preview) |
| **048** | [Desktop Notification Scheduler](projects/048_desktop_notification_scheduler) | Schedule local reminders and notifications. | `Document Search Engine` | [View Preview 📺](projects/048_desktop_notification_scheduler/README.md#%EF%B8%8F-live-terminal-preview) |
| **049** | [System Resource Dashboard](projects/049_system_resource_dashboard) | Monitor CPU, RAM, disk and network usage. | `CSV Quality Auditor` | [View Preview 📺](projects/049_system_resource_dashboard/README.md#%EF%B8%8F-live-terminal-preview) |
| **050** | [Process Manager](projects/050_process_manager) | List, filter and safely request termination of processes. | `Flask REST Microservice` | [View Preview 📺](projects/050_process_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **051** | [Disk Usage Analyzer](projects/051_disk_usage_analyzer) | Recursive folder size analyzer with largest-items report. | `Statistical Profiler` | [View Preview 📺](projects/051_disk_usage_analyzer/README.md#%EF%B8%8F-live-terminal-preview) |
| **052** | [Backup Manager](projects/052_backup_manager) | Versioned folder backups with retention policy. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/052_backup_manager/README.md#%EF%B8%8F-live-terminal-preview) |
| **053** | [Folder Sync Tool](projects/053_folder_sync_tool) | One-way sync with hashes and dry-run preview. | `SQLite Record Engine` | [View Preview 📺](projects/053_folder_sync_tool/README.md#%EF%B8%8F-live-terminal-preview) |
| **054** | [CSV Cleaner](projects/054_csv_cleaner) | Detect missing values, duplicates and malformed rows. | `Document Search Engine` | [View Preview 📺](projects/054_csv_cleaner/README.md#%EF%B8%8F-live-terminal-preview) |
| **055** | [Excel Report Generator](projects/055_excel_report_generator) | Create formatted Excel reports from CSV data. | `CSV Quality Auditor` | [View Preview 📺](projects/055_excel_report_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **056** | [PDF Report Generator](projects/056_pdf_report_generator) | Turn analytics data into a formatted PDF report. | `Flask REST Microservice` | [View Preview 📺](projects/056_pdf_report_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **057** | [Sales Dashboard](projects/057_sales_dashboard) | Plot sales trends, regions and top products. | `Statistical Profiler` | [View Preview 📺](projects/057_sales_dashboard/README.md#%EF%B8%8F-live-terminal-preview) |
| **058** | [Student Performance Dashboard](projects/058_student_performance_dashboard) | Analyze marks, grades and subject trends. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/058_student_performance_dashboard/README.md#%EF%B8%8F-live-terminal-preview) |
| **059** | [Loan EMI Planner](projects/059_loan_emi_planner) | Calculate EMI, amortization schedule and payoff scenarios. | `SQLite Record Engine` | [View Preview 📺](projects/059_loan_emi_planner/README.md#%EF%B8%8F-live-terminal-preview) |
| **060** | [Investment Portfolio Tracker](projects/060_investment_portfolio_tracker) | Track holdings, average cost and P/L from CSV prices. | `Document Search Engine` | [View Preview 📺](projects/060_investment_portfolio_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **061** | [Crypto Portfolio Simulator](projects/061_crypto_portfolio_simulator) | Paper portfolio with simulated trades and P/L. | `CSV Quality Auditor` | [View Preview 📺](projects/061_crypto_portfolio_simulator/README.md#%EF%B8%8F-live-terminal-preview) |
| **062** | [Currency Converter](projects/062_currency_converter) | Live exchange-rate converter with cached rates. | `Flask REST Microservice` | [View Preview 📺](projects/062_currency_converter/README.md#%EF%B8%8F-live-terminal-preview) |
| **063** | [Flight Fare Watcher](projects/063_flight_fare_watcher) | Store target routes and compare fetched public fare data. | `Statistical Profiler` | [View Preview 📺](projects/063_flight_fare_watcher/README.md#%EF%B8%8F-live-terminal-preview) |
| **064** | [Product Price Tracker](projects/064_product_price_tracker) | Track public product prices from supplied pages. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/064_product_price_tracker/README.md#%EF%B8%8F-live-terminal-preview) |
| **065** | [Book Recommendation Engine](projects/065_book_recommendation_engine) | Content-based recommendation from book metadata. | `SQLite Record Engine` | [View Preview 📺](projects/065_book_recommendation_engine/README.md#%EF%B8%8F-live-terminal-preview) |
| **066** | [Movie Recommendation Engine](projects/066_movie_recommendation_engine) | Genre/tag similarity recommendation system. | `Document Search Engine` | [View Preview 📺](projects/066_movie_recommendation_engine/README.md#%EF%B8%8F-live-terminal-preview) |
| **067** | [Music Recommendation Engine](projects/067_music_recommendation_engine) | Similarity-based playlist generator. | `CSV Quality Auditor` | [View Preview 📺](projects/067_music_recommendation_engine/README.md#%EF%B8%8F-live-terminal-preview) |
| **068** | [Resume Keyword Matcher](projects/068_resume_keyword_matcher) | Compare a resume against a job description. | `Flask REST Microservice` | [View Preview 📺](projects/068_resume_keyword_matcher/README.md#%EF%B8%8F-live-terminal-preview) |
| **069** | [Cover Letter Generator](projects/069_cover_letter_generator) | Template-driven cover letters from structured data. | `Statistical Profiler` | [View Preview 📺](projects/069_cover_letter_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **070** | [Text Summarizer](projects/070_text_summarizer) | Extractive summarizer for local text documents. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/070_text_summarizer/README.md#%EF%B8%8F-live-terminal-preview) |
| **071** | [PDF Text Search Engine](projects/071_pdf_text_search_engine) | Index PDF text and search across a local collection. | `SQLite Record Engine` | [View Preview 📺](projects/071_pdf_text_search_engine/README.md#%EF%B8%8F-live-terminal-preview) |
| **072** | [OCR Document Pipeline](projects/072_ocr_document_pipeline) | OCR image documents and save searchable text. | `Document Search Engine` | [View Preview 📺](projects/072_ocr_document_pipeline/README.md#%EF%B8%8F-live-terminal-preview) |
| **073** | [Language Detector](projects/073_language_detector) | Detect language from text using a lightweight model. | `CSV Quality Auditor` | [View Preview 📺](projects/073_language_detector/README.md#%EF%B8%8F-live-terminal-preview) |
| **074** | [Sentiment Analyzer](projects/074_sentiment_analyzer) | Classify review sentiment with TF-IDF + logistic regression. | `Flask REST Microservice` | [View Preview 📺](projects/074_sentiment_analyzer/README.md#%EF%B8%8F-live-terminal-preview) |
| **075** | [Spam Email Classifier](projects/075_spam_email_classifier) | Train a local text classifier on labeled emails. | `Statistical Profiler` | [View Preview 📺](projects/075_spam_email_classifier/README.md#%EF%B8%8F-live-terminal-preview) |
| **076** | [House Price Predictor](projects/076_house_price_predictor) | Regression model with preprocessing and evaluation. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/076_house_price_predictor/README.md#%EF%B8%8F-live-terminal-preview) |
| **077** | [Student Score Predictor](projects/077_student_score_predictor) | Regression model with train/test evaluation. | `SQLite Record Engine` | [View Preview 📺](projects/077_student_score_predictor/README.md#%EF%B8%8F-live-terminal-preview) |
| **078** | [Customer Churn Predictor](projects/078_customer_churn_predictor) | Classification pipeline with metrics and feature importance. | `Document Search Engine` | [View Preview 📺](projects/078_customer_churn_predictor/README.md#%EF%B8%8F-live-terminal-preview) |
| **079** | [Loan Approval Predictor](projects/079_loan_approval_predictor) | Classification demo with preprocessing and metrics. | `CSV Quality Auditor` | [View Preview 📺](projects/079_loan_approval_predictor/README.md#%EF%B8%8F-live-terminal-preview) |
| **080** | [Sales Forecasting Tool](projects/080_sales_forecasting_tool) | Time-series baseline forecast and visualization. | `Flask REST Microservice` | [View Preview 📺](projects/080_sales_forecasting_tool/README.md#%EF%B8%8F-live-terminal-preview) |
| **081** | [Anomaly Detector](projects/081_anomaly_detector) | Detect unusual numeric observations with robust statistics. | `Statistical Profiler` | [View Preview 📺](projects/081_anomaly_detector/README.md#%EF%B8%8F-live-terminal-preview) |
| **082** | [Image Classifier](projects/082_image_classifier) | Train a small CNN on a folder-based image dataset. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/082_image_classifier/README.md#%EF%B8%8F-live-terminal-preview) |
| **083** | [Face Attendance Demo](projects/083_face_attendance_demo) | Face embeddings for local attendance demonstration. | `SQLite Record Engine` | [View Preview 📺](projects/083_face_attendance_demo/README.md#%EF%B8%8F-live-terminal-preview) |
| **084** | [Hand Gesture Controller](projects/084_hand_gesture_controller) | Recognize basic hand gestures with webcam input. | `Document Search Engine` | [View Preview 📺](projects/084_hand_gesture_controller/README.md#%EF%B8%8F-live-terminal-preview) |
| **085** | [Object Detection Demo](projects/085_object_detection_demo) | Run a pretrained detector on webcam frames. | `CSV Quality Auditor` | [View Preview 📺](projects/085_object_detection_demo/README.md#%EF%B8%8F-live-terminal-preview) |
| **086** | [Voice Notes App](projects/086_voice_notes_app) | Record microphone audio and create timestamped notes. | `Flask REST Microservice` | [View Preview 📺](projects/086_voice_notes_app/README.md#%EF%B8%8F-live-terminal-preview) |
| **087** | [Speech-to-Text Journal](projects/087_speech_to_text_journal) | Transcribe microphone input into daily journal files. | `Statistical Profiler` | [View Preview 📺](projects/087_speech_to_text_journal/README.md#%EF%B8%8F-live-terminal-preview) |
| **088** | [Text-to-Speech Reader](projects/088_text_to_speech_reader) | Read documents aloud with playback controls. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/088_text_to_speech_reader/README.md#%EF%B8%8F-live-terminal-preview) |
| **089** | [AI Chat Assistant](projects/089_ai_chat_assistant) | Local chat UI with pluggable model/API backend. | `SQLite Record Engine` | [View Preview 📺](projects/089_ai_chat_assistant/README.md#%EF%B8%8F-live-terminal-preview) |
| **090** | [Document Q&A Assistant](projects/090_document_qa_assistant) | Chunk local documents and retrieve relevant passages. | `Document Search Engine` | [View Preview 📺](projects/090_document_qa_assistant/README.md#%EF%B8%8F-live-terminal-preview) |
| **091** | [Code Explanation Assistant](projects/091_code_explanation_assistant) | Generate structured explanations for pasted code. | `CSV Quality Auditor` | [View Preview 📺](projects/091_code_explanation_assistant/README.md#%EF%B8%8F-live-terminal-preview) |
| **092** | [SQL Query Assistant](projects/092_sql_query_assistant) | Convert natural-language questions into reviewed SQL. | `Flask REST Microservice` | [View Preview 📺](projects/092_sql_query_assistant/README.md#%EF%B8%8F-live-terminal-preview) |
| **093** | [AI Study Buddy](projects/093_ai_study_buddy) | Generate quizzes from user-provided study notes. | `Statistical Profiler` | [View Preview 📺](projects/093_ai_study_buddy/README.md#%EF%B8%8F-live-terminal-preview) |
| **094** | [Flashcard Generator](projects/094_flashcard_generator) | Turn notes into structured flashcards. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/094_flashcard_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **095** | [Timetable Generator](projects/095_timetable_generator) | Constraint-based class timetable generator. | `SQLite Record Engine` | [View Preview 📺](projects/095_timetable_generator/README.md#%EF%B8%8F-live-terminal-preview) |
| **096** | [Pathfinding Visualizer](projects/096_pathfinding_visualizer) | Visualize BFS, DFS and A* on a grid. | `Document Search Engine` | [View Preview 📺](projects/096_pathfinding_visualizer/README.md#%EF%B8%8F-live-terminal-preview) |
| **097** | [Sorting Visualizer](projects/097_sorting_visualizer) | Animate multiple sorting algorithms with metrics. | `CSV Quality Auditor` | [View Preview 📺](projects/097_sorting_visualizer/README.md#%EF%B8%8F-live-terminal-preview) |
| **098** | [Tic-Tac-Toe AI](projects/098_tic_tac_toe_ai) | Minimax-based unbeatable Tic-Tac-Toe. | `Flask REST Microservice` | [View Preview 📺](projects/098_tic_tac_toe_ai/README.md#%EF%B8%8F-live-terminal-preview) |
| **099** | [Snake Game](projects/099_snake_game) | Pygame snake with levels, score and saved high score. | `Statistical Profiler` | [View Preview 📺](projects/099_snake_game/README.md#%EF%B8%8F-live-terminal-preview) |
| **100** | [Flappy Bird Clone](projects/100_flappy_bird_clone) | Pygame arcade game with collision and score. | `SHA-256 Sync Pipeline` | [View Preview 📺](projects/100_flappy_bird_clone/README.md#%EF%B8%8F-live-terminal-preview) |
| **101** | [Space Shooter](projects/101_space_shooter) | Pygame shooter with waves, power-ups and scoring. | `SQLite Record Engine` | [View Preview 📺](projects/101_space_shooter/README.md#%EF%B8%8F-live-terminal-preview) |

---

## 🛠️ Original Utility: Calculate Your Age

This repository also preserves the original `calculate_your_age.py` tool.

### Description
Calculates your age dynamically in years, months, and days, accurately taking leap years into account.

```bash
python calculate_your_age.py
```

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE).
