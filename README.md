# Data Cleaning Project

## 📁 project structure

(Updated v1.2 05/04/2025)
project/
├── data/                    # Raw CSV data
├── cleaned_data/            # Data after preliminary cleaning
├── cleaned_data_strict/     # Store deduplicated or deeply cleaned data
├── config/
│   ├── column_types_master.csv
│   └── column_types_dictionaries.csv     # New: Column Dictionary
├── reports/
│   ├── missing_values_report.csv
│   └── relation_integrity_report.csv
├── logs/
│   ├── removed_rows/        # To store removed/duplicated data
│   ├── filled_personnumber_log.csv  # New: Fill log for PersonNumber
│   └── main.log             # Main program run log
└── scripts/
    ├── main.py
    ├── clean_missing.py
    ├── clean_format.py
    ├── clean_relations.py
    ├── clean_missing_strict.py
    └── fill_person_number.py     # New: Fill missing PersonNumber based on name

## 🧩 What the module does

### `clean_missing.py`
- Count the number of missing values per column in each CSV file
- Output: 'reports/missing_values_report.csv'

### `clean_format.py`
- Clean each column according to 'column_types_master.csv'
- Types supported: integer, real, date, timestamp, text
- Output: 'cleaned_data/'

### `clean_relations.py`
- Automatic identification of many-to-many relational tables
- Check if foreign key fields are missing or duplicated
- Output: 'reports/relation_integrity_report.csv'

### `main.py`
- Main controller script
- Supports modular execution via command-line arguments
- Writes full log to logs/main.log

### `clean_missing_strict.py`
- Load only 19GrantByPersonByDate.csv from cleaned_data/
- Remove full-duplicate rows
- Output:
  - Cleaned file → cleaned_data_strict/
  - Deleted rows log → logs/removed_rows/

## Update this week

### `fill_person_number.py`
- Fill missing PersonNumber in 08OutputToInvolvedPerson.csv
- Match using FirstName + Surname against 04Person.csv
- Only fills if exactly one match is found
- Output:
  - Cleaned file → cleaned_data_strict/08OutputToInvolvedPerson_filled.csv
  - Fill log → logs/filled_personnumber_log.csv

### 📚 Column Dictionary

- File Location: config/column_types_dictionaries.csv
- File Description:
  - column_name: The original field name
  - type: Expected data type (text, date, real, integer, etc.)
  - description: Human-readable explanation of what the field means

## ✅ Start up

```bash

python scripts/main.py
python scripts/main.py --strict_only
python scripts/main.py --fill-personnumber