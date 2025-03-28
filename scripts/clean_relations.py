# Manages relationships

import pandas as pd
import os

# Load the field type mapping table
def load_column_types(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)
    return dict(zip(df["column"], df["type"]))

# Determines whether a column is a foreign key field
def is_foreign_key_field(col_name: str, col_type: str) -> bool:
    return (
        ("id" in col_name.lower() or "number" in col_name.lower()) and
        col_type.lower() in ["integer", "text"]
    )

# Check whether a single file conforms to a many-to-many relational table structure and analyze it
def check_relation_integrity(file_path: str, filename: str, column_types: dict, excluded_files: set):
    if filename in excluded_files:
        print(f"⏭ The main table has been excluded：{filename}\n")
        return None

    try:
        df = pd.read_csv(file_path)
        key_fields = [
            col for col in df.columns
            if is_foreign_key_field(col, column_types.get(col, ""))
        ]

        if len(key_fields) < 2:
            print(f" skip {filename}（Only {len(key_fields)} foreign key fields are identified）")
            return None

        print(f" Checking for: {filename}")
        print(f" Foreign key fields: {key_fields}")

        null_counts = df[key_fields].isnull().sum()
        total_null = int(null_counts.sum())
        null_fields = int((null_counts > 0).sum())
        duplicate_count = int(df.duplicated(subset=key_fields).sum())

        return {
            "file": filename,
            "key_fields": ", ".join(key_fields),
            "null_field_count": null_fields,
            "null_cell_count": total_null,
            "duplicate_count": duplicate_count,
            "total_rows": len(df)
        }

    except Exception as e:
        print(f" Fail to load: {filename}，Error: {e}")
        return None

# Main function
def run_relation_analysis():
    COLUMN_TYPE_FILE = "../config/column_types_master.csv"
    DATA_FOLDER = "../data/"
    EXCLUDED_FILES = {"01Grant.csv", "04Person.csv"}

    column_types = load_column_types(COLUMN_TYPE_FILE)
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

    results = []
    for filename in files:
        path = os.path.join(DATA_FOLDER, filename)
        result = check_relation_integrity(path, filename, column_types, EXCLUDED_FILES)
        if result:
            results.append(result)

    # Output report
    if results:
        output_path = "../reports/relation_integrity_report.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.DataFrame(results).to_csv(output_path, index=False)
        print(f"\n The analysis report has been saved to: {output_path}")