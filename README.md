# EmailBot Project Documentation

## Overview
EmailBot automates invoice and email processing for organizations using UiPath and LLM API. It streamlines inbox monitoring, document classification, field extraction, business rule validation, response generation, and dashboard updates.

## Modules
- **UiPath Workflow**: Automates email monitoring, attachment download, and process orchestration.
- **AI Integration**: Python script for document classification and field extraction using LLM API.
- **Dashboard Integration**: Python script to update Google Sheets with invoice processing status.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/NandiniPahuja/EmailBot.git`
2. Open the UiPath workflow in UiPath Studio (`uipath/EmailBot/Main.xaml`).
3. Configure email account and ERP/Excel file paths in the workflow.
4. Set up LLM API credentials in `ai/llm_api_integration.py`.
5. Set up Google API credentials in `dashboard/dashboard_update.py`.
6. Install required Python packages:
   - `pip install requests gspread oauth2client`
7. Run the workflow and scripts as per your automation needs.

## File Structure
- `uipath/EmailBot/Main.xaml` - Main UiPath workflow
- `uipath/EmailBot/ai/llm_api_integration.py` - LLM API integration script
- `uipath/EmailBot/dashboard/dashboard_update.py` - Dashboard update script

## Customization
- Modify workflow steps in UiPath Studio for your business rules.
- Update Python scripts for your LLM API and dashboard requirements.

## License
MIT

---
Update this documentation as the project evolves.
