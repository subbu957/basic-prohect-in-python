# -*- coding: utf-8 -*-
"""
39. Video Metadata Catalog
Focus: Catalog video metadata and searchable library.
"""

import csv, math
from collections import defaultdict

def profile_csv(filepath="sample.csv"):
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("CSV is empty")
    print(f"\n=== Dataset Summary: {filepath} ===")
    print(f"Total rows: {len(rows)}")
    for k in rows[0]:
        vals = []
        for r in rows:
            try:
                vals.append(float(r[k]))
            except Exception:
                pass
        if vals:
            mean = sum(vals) / len(vals)
            var = sum((x - mean) ** 2 for x in vals) / len(vals)
            sd = math.sqrt(var)
            print(f"{k:20} n={len(vals):5} mean={mean:.2f} min={min(vals):.2f} max={max(vals):.2f} sd={sd:.2f}")
        else:
            counts = defaultdict(int)
            for r in rows:
                counts[r[k]] += 1
            top = sorted(counts.items(), key=lambda x: -x[1])[:5]
            print(f"{k:20} categories={len(counts):<3} top={top}")

def main():
    filepath = input("Data CSV [sample.csv]: ").strip() or "sample.csv"
    profile_csv(filepath)

if __name__ == "__main__":
    main()
