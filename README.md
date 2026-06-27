# Calculate Your Age

A simple, interactive command-line Python script that calculates your age in years, months, and days based on the user's age input and local time.

## Description

This program prompts the user for their name and age. It then dynamically calculates:
- The age in **years**
- The age in **months**
- The total age in **days** (accurately taking leap years into account)

## Features

- **Leap Year Verification:** Uses the `calendar.isleap` library to accurately determine leap years and add `366` days instead of `365` for those years.
- **Dynamic Local Time:** Uses Python's `time` module to read the current system year, month, and day for correct calculations.

## How to Run

Ensure you have Python 3 installed. Run the script using:

```bash
python calculate_your_age.py
```

### Example Input/Output:

```text
input your name: bvs subbu
input your age: 34
bvs subbu's age is 34 years or 414 months or 12597 days
```
