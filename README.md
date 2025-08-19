# Enhanced EmailBot Project Documentation

## Features
1. **Multi-Channel Document Intake**
   - Email attachments
   - Shared folders (Dropbox/SharePoint)
   - Scanned PDFs (OCR via UiPath + AI Computer Vision)
2. **AI-Powered Document Understanding**
   - Document classification (Invoice, PO, Quotation, Other)
   - Key field extraction (Vendor Name, Invoice Number, Amount, Due Date, Tax IDs)
   - Handles unstructured layouts
3. **ERP / Database Validation**
   - Vendor master list validation
   - Duplicate invoice prevention
   - Payment terms check
4. **Smart Email Response Generation**
   - Acknowledgment for valid invoices
   - Rejection/correction request for invalid invoices
   - Dynamic placeholders in emails
5. **Exception Handling & Escalations**
   - Escalate to human reviewer if extraction confidence is low
   - Summary email with issues
   - Exception queue logging
6. **Dashboard & Reporting**
   - Real-time dashboard (UiPath Orchestrator, Power BI, Excel)
   - Analytics: processed, approved/rejected, turnaround, pending exceptions
7. **Audit Trail & Compliance**
   - Action logging (timestamps, user, response)
   - Optional digital signature/ID

## Folder Structure
- `/uipath/EmailBot/Main.xaml` - Main workflow
- `/uipath/EmailBot/intake/` - Multi-channel intake workflows
- `/uipath/EmailBot/ai/` - AI/LLM integration scripts
- `/uipath/EmailBot/validation/` - ERP/database validation workflows/scripts
- `/uipath/EmailBot/email/` - Smart email response templates/scripts
- `/uipath/EmailBot/exception/` - Exception handling workflows/scripts
- `/uipath/EmailBot/dashboard/` - Dashboard/reporting scripts
- `/uipath/EmailBot/audit/` - Audit trail & compliance logs/scripts

## Setup & Usage
- See individual module README files for setup and usage instructions.

# EmailBot User Guide

## Quick Start
1. Clone the repository:
   ```sh
   git clone https://github.com/NandiniPahuja/EmailBot.git
   ```
2. Edit `config.json` with your email, folder paths, API keys, and ERP file names.
3. Install Python and UiPath Studio (see UiPath docs).
4. Open a terminal in the EmailBot folder and run:
   ```sh
   python setup_env.py
   ```
5. Open `Main.xaml` in UiPath Studio. Run the workflow.
   - The bot will read config.json, process documents, validate, send emails, update dashboard, and log actions.
   - Use the GUI form to select folders or toggle features (OCR, AI email response, dry run).
6. Check logs and dashboard for results.

## Features
- Centralized config: all settings in `config.json`
- Modular Python scripts (see requirements.txt)
- One-click execution via Main.xaml
- Built-in logging and exception handling
- Portable: all paths are relative
- UiPath Orchestrator support for scheduling

## Troubleshooting
- See `log.txt` for errors and status messages
- For first-time setup, use dry run mode to test without sending emails

## Advanced
- Move/copy the folder to any machine—no reconfiguration needed
- Add triggers in UiPath Orchestrator for scheduled runs
- See the included user guide PDF for tips and tooltips

# EmailBot Plugin Installation Guide

## How to Install
1. Download the EmailBot zip file from the release page or repository.
2. Unzip to any folder on your machine.
3. Open UiPath Studio and go to 'Manage Packages' or 'Import Project'.
4. Select the EmailBot folder (with project.json and Main.xaml).
5. Edit `config.json` with your details (email, API keys, folders).
6. Run `setup_env.py` to install Python dependencies.
7. Open and run `Main.xaml` in UiPath Studio.

## Features
- No cloning or git required—just download and use
- All settings in one config file
- Modular, portable, and easy to move
- Step-by-step instructions and user guide included

## Support
- See `user_guide.pdf` for tips and troubleshooting
- All logs and errors are saved in `log.txt`

---
Update this documentation as features are implemented.
