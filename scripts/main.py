# Main script to run all processes

import logging
from clean_missing import run_missing_check
from clean_format import run_format_cleaning
from clean_relations import run_relation_analysis
import os

# Logging configuration
os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/main.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode="w"
)

def main():
    logging.info("Start execution of the data cleaning main program")

    try:
        logging.info("Step 1: Count the missing values")
        run_missing_check()
        logging.info("Missing values were counted")
    except Exception as e:
        logging.error(f" The missing values count failed：{e}")

    try:
        logging.info("Step two: Format unified cleaning")
        run_format_cleaning()
        logging.info("Format cleaning completed")
    except Exception as e:
        logging.error(f"Format cleaning failure：{e}")

    try:
        logging.info("Step 3: Relationship integrity analysis")
        run_relation_analysis()
        logging.info("Many-to-many relationship analysis is complete")
    except Exception as e:
        logging.error(f"Many-to-many relationship analysis failed：{e}")

    logging.info("All tasks have been completed")

if __name__ == "__main__":
    main()
