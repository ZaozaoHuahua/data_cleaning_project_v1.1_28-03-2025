# Standardizes data format

import pandas as pd
import os

# Field type map file path
TYPE_MAPPING_FILE = "../config/column_types_master.csv"

# load field type mappings
def load_column_types(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)
    return dict(zip(df["column"], df["type"]))

# Perform cleaning by field type
def clean_column(df: pd.DataFrame, column: str, dtype: str) -> pd.Series:
    if column not in df.columns:
        return df[column]

    if dtype == "integer":
        return pd.to_numeric(df[column], errors="coerce").astype("Int64")
    elif dtype == "real":
        return pd.to_numeric(df[column], errors="coerce")
    elif dtype in ["date", "timestamp"]:
        return pd.to_datetime(df[column], errors="coerce", dayfirst=False)
    elif dtype == "text":
        return df[column].astype(str).str.strip()
    else:
        return df[column]

# Main function: processes all data files
def run_format_cleaning():
    column_types = load_column_types(TYPE_MAPPING_FILE)
    DATA_FOLDER = "../data/"
    OUTPUT_FOLDER = "../cleaned_data/"
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".csv"):
            input_path = os.path.join(DATA_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, filename)

            try:
                df = pd.read_csv(input_path)
                for col in df.columns:
                    dtype = column_types.get(col)
                    if dtype:
                        df[col] = clean_column(df, col, dtype)

                df.to_csv(output_path, index=False)
                print(f" It has been cleaned and stored: {filename}")

            except Exception as e:
                print(f" Handling failures: {filename}，Error message: {e}")