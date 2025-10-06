import requests
import pandas as pd
import logging
from datetime import datetime

# -------------------------------------------------
# Fetch data from JSONPlaceholder API
# -------------------------------------------------
def fetch_data(limit=5):
    url = f"https://jsonplaceholder.typicode.com/posts?_limit={limit}"
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to fetch data from API (status {response.status_code})")
        return []
    return response.json()

# -------------------------------------------------
# Process data using pandas
# -------------------------------------------------
def process_data(data):
    df = pd.DataFrame(data)
    # Example: Count posts per user
    report = df.groupby("userId")["id"].count().reset_index()
    report.columns = ["UserID", "PostCount"]
    return report

# -------------------------------------------------
# Save report with timestamped filename
# -------------------------------------------------
def save_report(df, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    logging.info(f"Report saved to {filename}")
    return filename