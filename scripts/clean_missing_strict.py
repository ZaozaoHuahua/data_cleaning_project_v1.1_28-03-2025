# Further processing the data

import pandas as pd

# File path Configuration
FILENAME = "19GrantByPersonByDate.csv"
INPUT_PATH = "cleaned_data/" + FILENAME
OUTPUT_PATH = "cleaned_data_strict/" + FILENAME
LOG_PATH = "logs/removed_rows/19GrantByPersonByDate_duplicates_log.csv"

def clean_duplicates():
    print("Strict cleaning for duplicates in:", FILENAME)

    try:
        df = pd.read_csv(INPUT_PATH)

        # Get duplicate rows (full column duplicates)
        duplicates = df[df.duplicated(keep=False)]

        # Remove duplicate rows and keep only the first one
        df_cleaned = df.drop_duplicates()

        # Saving the results
        df_cleaned.to_csv(OUTPUT_PATH, index=False)
        duplicates.to_csv(LOG_PATH, index=False)

        print(f"Completed: {FILENAME}")
        print(f"Duplicates removed: {len(duplicates)}")
        print(f"Cleaned file saved to: {OUTPUT_PATH}")
        print(f"Duplicates log saved to: {LOG_PATH}")

    except Exception as e:
        print("Error during duplicate cleaning:", e)