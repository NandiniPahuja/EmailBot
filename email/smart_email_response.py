"""
smart_email_response.py
Generates smart email responses using LLM for valid/invalid invoices.
"""
import requests
import json
import sys

# Usage: python smart_email_response.py <validation_results_json> <output_email_file>

LLM_API_URL = "https://api.example.com/generate-email"  # Replace with actual endpoint
API_KEY = "YOUR_API_KEY"  # Replace with your API key


def generate_email(validation_results):
    with open(validation_results) as f:
        data = json.load(f)
    payload = {
        "vendor_name": data.get("vendor_name"),
        "invoice_id": data.get("invoice_number"),
        "status": data.get("status"),
        "issues": data.get("issues", [])
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    if len(sys.argv) != 3:
        print("Usage: python smart_email_response.py <validation_results_json> <output_email_file>")
        sys.exit(1)
    validation_results = sys.argv[1]
    output_email_file = sys.argv[2]
    result = generate_email(validation_results)
    with open(output_email_file, "w") as out:
        json.dump(result, out, indent=2)
    print(f"Email draft saved to {output_email_file}")


if __name__ == "__main__":
    main()
