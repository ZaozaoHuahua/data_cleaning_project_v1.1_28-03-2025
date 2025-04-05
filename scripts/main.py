# Main script to run all processes

import logging
import os
import sys
from clean_missing import run_missing_check
from clean_format import run_format_cleaning
from clean_relations import run_relation_analysis
from clean_missing_strict import clean_duplicates
from fill_person_number import fill_missing_person_numbers # New imports

# Logging configuration
os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/main.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode="w"
)

def main():
    # Mode One: Only strict deduplication is performed
    if "--strict_only" in sys.argv:
        logging.info("Executing ONLY strict duplicate cleaning (--strict_only)")
        print("Running strict duplicate cleaning only...")
        try:
            clean_duplicates()
            logging.info("Strict duplicate cleaning completed")
            print("Strict duplicate cleaning executed successfully.")
        except Exception as e:
            logging.error(f"Strict duplicate cleaning failed: {e}")
            print("Strict duplicate cleaning failed:", e)
        return

    # Mode two: Only the PersonNumber fill is performed
    if "--fill-personnumber" in sys.argv:
        logging.info("Executing ONLY PersonNumber fill (--fill-personnumber)")
        print("Running fill_missing_person_numbers only...")
        try:
            fill_missing_person_numbers()
            logging.info("PersonNumber fill completed")
            print("PersonNumber filling executed successfully.")
        except Exception as e:
            logging.error(f"PersonNumber fill failed: {e}")
            print("PersonNumber fill failed:", e)
        return

    # Normal main flow
    logging.info("Start execution of the data cleaning main program")

    try:
        logging.info("Step 1: Count the missing values")
        run_missing_check()
        logging.info("Missing values were counted")
    except Exception as e:
        logging.error(f"The missing values count failed: {e}")

    try:
        logging.info("Step 2: Format unified cleaning")
        run_format_cleaning()
        logging.info("Format cleaning completed")
    except Exception as e:
        logging.error(f"Format cleaning failure: {e}")

    try:
        logging.info("Step 3: Relationship integrity analysis")
        run_relation_analysis()
        logging.info("Many-to-many relationship analysis is complete")
    except Exception as e:
        logging.error(f"Many-to-many relationship analysis failed: {e}")

    logging.info("All tasks have been completed")
    print("Main cleaning workflow completed (strict mode not triggered).")

if __name__ == "__main__":
    main()
