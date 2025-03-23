# Handles missing values

import pandas as pd
import os

# Output path (used to hold missing data statistical reports)
REPORT_FOLDER = "../reports/"
os.makedirs(REPORT_FOLDER, exist_ok=True)

# Missing values statistics main function
def run_missing_check():
    DATA_FOLDER = "../data/"
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

    summary_list = []

    for filename in files:
        file_path = os.path.join(DATA_FOLDER, filename)
        try:
            df = pd.read_csv(file_path)
            missing_counts = df.isnull().sum()
            total_rows = len(df)

            for column, missing in missing_counts.items():
                summary_list.append({
                    "file": filename,
                    "column": column,
                    "missing_count": missing,
                    "missing_percent": round(missing / total_rows * 100, 2) if total_rows > 0 else 0
                })

            print(f" Missing values were counted: {filename}")

        except Exception as e:
            print(f" Handling failures: {filename}，Error message: {e}")

    # Output as a DataFrame and save the report
    report_df = pd.DataFrame(summary_list)
    report_path = os.path.join(REPORT_FOLDER, "missing_values_report.csv")
    report_df.to_csv(report_path, index=False)
    print(f"\n Missing values statistics have been saved to：{report_path}")