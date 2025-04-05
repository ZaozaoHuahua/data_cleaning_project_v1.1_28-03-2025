import pandas as pd

# Path configuration
FILENAME = "08OutputToInvolvedPerson.csv"
REF_FILE = "04Person.csv"
INPUT_PATH = "cleaned_data/" + FILENAME
REF_PATH = "cleaned_data/" + REF_FILE
OUTPUT_PATH = "cleaned_data_strict/08OutputToInvolvedPerson_filled.csv"
LOG_PATH = "logs/filled_personnumber_log.csv"

def fill_missing_person_numbers():
    print("Filling missing PersonNumber in 08OutputToInvolvedPerson.csv...")

    # Reading input data
    df = pd.read_csv(INPUT_PATH)
    ref = pd.read_csv(REF_PATH)

    # Convert PersonNumber column to string to avoid dtype warning
    df['PersonNumber'] = df['PersonNumber'].astype(str)

    # Prepare lookup table from reference file
    ref_lookup = ref[['FirstName', 'Surname', 'PersonNumber']].dropna()

    # Collect filling log
    log = []

    for idx, row in df[df['PersonNumber'].isin(["nan", "NaN"])].iterrows():
        fn, sn = row['FirstName'], row['Surname']
        matches = ref_lookup[(ref_lookup['FirstName'] == fn) & (ref_lookup['Surname'] == sn)]

        if len(matches) == 1:
            person_id = matches.iloc[0]['PersonNumber']
            df.at[idx, 'PersonNumber'] = person_id
            log.append({
                'index': idx,
                'FirstName': fn,
                'Surname': sn,
                'Filled_PersonNumber': person_id
            })

    # Save results and logs
    df.to_csv(OUTPUT_PATH, index=False)
    pd.DataFrame(log).to_csv(LOG_PATH, index=False)

    print(f"Filled {len(log)} PersonNumber values.")
    print(f"Output saved to: {OUTPUT_PATH}")
    print(f"Fill log saved to: {LOG_PATH}")