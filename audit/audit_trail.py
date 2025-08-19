"""
audit_trail.py
Logs every action for audit trail & compliance, with optional digital signature/ID.
"""
import json
import sys
from datetime import datetime

# Usage: python audit_trail.py <action_json> <audit_log_file> [user_id]


def log_action(action_json, audit_log_file, user_id=None):
    with open(action_json) as f:
        data = json.load(f)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": data.get("action"),
        "invoice_id": data.get("invoice_id"),
        "user": user_id or data.get("user"),
        "details": data.get("details"),
        "response": data.get("response"),
        "digital_signature": data.get("digital_signature")
    }
    try:
        with open(audit_log_file, "r") as logf:
            logs = json.load(logf)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
    logs.append(log_entry)
    with open(audit_log_file, "w") as logf:
        json.dump(logs, logf, indent=2)
    print(f"Audit log updated in {audit_log_file} with entry: {log_entry}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python audit_trail.py <action_json> <audit_log_file> [user_id]")
        sys.exit(1)
    action_json = sys.argv[1]
    audit_log_file = sys.argv[2]
    user_id = sys.argv[3] if len(sys.argv) > 3 else None
    log_action(action_json, audit_log_file, user_id)


if __name__ == "__main__":
    main()
