"""
dashboard_update.py
Sample script to update Google Sheets with invoice processing status.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
import json

# Usage: python dashboard_update.py <status_json> <sheet_name>

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'path/to/credentials.json'  # Replace with your Google API credentials file


def update_dashboard(status_json, sheet_name):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    with open(status_json) as f:
        data = json.load(f)
    # Example: append a row with invoice ID, vendor, amount, status
    row = [data.get('invoice_id'), data.get('vendor_name'), data.get('amount'), data.get('status')]
    sheet.append_row(row)
    print(f"Row appended to {sheet_name}: {row}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python dashboard_update.py <status_json> <sheet_name>")
        sys.exit(1)
    status_json = sys.argv[1]
    sheet_name = sys.argv[2]
    update_dashboard(status_json, sheet_name)


if __name__ == "__main__":
    main()
