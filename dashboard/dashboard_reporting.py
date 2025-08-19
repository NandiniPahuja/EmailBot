"""
dashboard_reporting.py
Dashboard & reporting for EmailBot: updates Power BI/Excel sheet with analytics.
"""
import openpyxl
import sys
import json

# Usage: python dashboard_reporting.py <analytics_json> <excel_file>


def update_dashboard(analytics_json, excel_file):
    with open(analytics_json) as f:
        data = json.load(f)
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active
    # Example: append a row with analytics
    row = [
        data.get('date'),
        data.get('invoices_processed'),
        data.get('amount_approved'),
        data.get('amount_rejected'),
        data.get('avg_turnaround_time'),
        data.get('exceptions_pending')
    ]
    ws.append(row)
    wb.save(excel_file)
    print(f"Dashboard updated in {excel_file} with row: {row}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python dashboard_reporting.py <analytics_json> <excel_file>")
        sys.exit(1)
    analytics_json = sys.argv[1]
    excel_file = sys.argv[2]
    update_dashboard(analytics_json, excel_file)


if __name__ == "__main__":
    main()
