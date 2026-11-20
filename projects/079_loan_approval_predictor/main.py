# -*- coding: utf-8 -*-
"""
79. Loan Approval Predictor
Focus: Classification demo with preprocessing and metrics.
"""

import csv, statistics
from collections import Counter, defaultdict

def audit_csv(filepath="sample.csv"):
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    print(f"\n=== CSV Quality Report: {filepath} ===")
    print("Rows:", len(rows))
    columns = list(rows[0]) if rows else []
    print("Columns:", columns)
    print("\n--- Column Quality & Missing Values ---")
    for col in columns:
        values = [r[col] for r in rows]
        missing = sum(v.strip() == "" for v in values)
        unique_cnt = len(set(values))
        print(f"{col:20} missing={missing:<3} | unique={unique_cnt:<3}")

    # Duplicate report
    keys = [tuple(r.values()) for r in rows]
    dups = Counter(keys)
    dup_count = sum(n - 1 for n in dups.values() if n > 1)
    print(f"\nDuplicate rows found: {dup_count}")

def main():
    filepath = input("CSV file [sample.csv]: ").strip() or "sample.csv"
    audit_csv(filepath)

if __name__ == "__main__":
    main()
