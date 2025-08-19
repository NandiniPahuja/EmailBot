"""
document_understanding.py
Enhanced AI-powered document understanding for EmailBot.
"""
import requests
import json
import sys

# Usage: python document_understanding.py <input_file> <output_file>

LLM_API_URL = "https://api.example.com/document-understanding"  # Replace with actual endpoint
API_KEY = "YOUR_API_KEY"  # Replace with your API key

# Example fields to extract
FIELDS = ["vendor_name", "invoice_number", "amount", "due_date", "tax_id"]


def classify_and_extract(input_file):
    with open(input_file, "rb") as f:
        files = {"file": f}
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {"fields": FIELDS}
        response = requests.post(LLM_API_URL, files=files, headers=headers, data={"fields": json.dumps(FIELDS)})
        response.raise_for_status()
        return response.json()


def main():
    if len(sys.argv) != 3:
        print("Usage: python document_understanding.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    result = classify_and_extract(input_file)
    with open(output_file, "w") as out:
        json.dump(result, out, indent=2)
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
