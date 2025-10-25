import argparse
import logging
import schedule
import time
import pandas as pd
from app.utils import fetch_data, process_data, save_report

# -------------------------------------------------
# Logging Setup
# -------------------------------------------------
logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------------------------
# Main Function
# -------------------------------------------------
def main(run_once=False):
    parser = argparse.ArgumentParser(description="DevOps Capstone Project with ArgParser Demo")
    parser.add_argument("--limit", type=int, default=5, help="Number of records to fetch")
    args = parser.parse_args()

    logging.info("Fetching data from API...")
    data = fetch_data(limit=args.limit)

    if not data:
        logging.warning("No data fetched from API.")
        print("⚠️  No data fetched. Check your internet connection or API URL.")
        return

    logging.info("Processing data with pandas...")
    df = process_data(data)

    logging.info("Saving report...")
    filename = save_report(df)

    logging.info("Pipeline completed successfully!")
    print(f"✅ Report generated successfully: {filename}")
    print(df.head())  # Display a small preview for users

    # Exit if running once (CLI mode)
    if run_once:
        return

    # -------------------------------------------------
    # Scheduler (demo: every 1 minute)
    # -------------------------------------------------
    schedule.every(1).minutes.do(main, run_once=True)
    while True:
        schedule.run_pending()
        time.sleep(1)