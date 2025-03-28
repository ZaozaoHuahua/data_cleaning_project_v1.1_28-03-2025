# Data Cleaning Project

## 📁 project structure

(Updated v1.1 28/03/2025)
project/
├── data/                    # Raw CSV data
├── cleaned_data/            # Data after preliminary cleaning
├── cleaned_data_strict/     # Store deduplicated data
├── config/
│   └── column_types_master.csv
├── reports/
│   ├── missing_values_report.csv
│   └── relation_integrity_report.csv
├── logs/
│   ├── removed_rows/        # To store deleted data
│   └── main.log             # Main program run log
└── scripts/
    ├── main.py
    ├── clean_missing.py
    ├── clean_format.py
    ├── clean_relations.py
    └── clean_missing_strict.py

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
- Main program entry point
- All three modules are called sequentially
- Automatically log runs to 'logs/main.log'

### `clean_missing_strict.py`
- Load only 19GrantByPersonByDate.csv from cleaned_data/
- Remove full-duplicate rows
- Save cleaned version into cleaned_data_strict/
- Save duplicate log to logs/removed_rows/


## ✅ Start up

```bash
python scripts/main.py
python scripts/main.py --strict_only