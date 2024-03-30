# JIRA Toolkit 🛠️

This repository contains two directories, each with a Python script for interacting with the JIRA API to extract and analyze ticket data:

- `extraction_jira_to_excel`: Contains a script to export JIRA issues to an Excel file.
- `jira_ticket_analysis_tool`: Includes a script for analyzing JIRA ticket data and a module with predefined queries.

## Directory Structure

```plaintext
.
├── extraction_jira_to_excel
│   ├── main.py           # Script to extract issues from JIRA and export to Excel.
│   └── readme.md         # Instructions specific to the extraction process.
├── jira_ticket_analysis_tool
│   ├── main.py           # Script for in-depth JIRA ticket analysis.
│   ├── new_queries.py    # Module containing the JQL queries used by main.py.
│   └── readme.md         # Instructions for ticket analysis tool.

extraction_jira_to_excel
Navigate into extraction_jira_to_excel for a script that connects to JIRA and exports selected issues to an Excel spreadsheet. See the local readme.md for detailed usage instructions.

jira_ticket_analysis_tool
In jira_ticket_analysis_tool, you'll find a script that performs detailed analysis of JIRA tickets based on dynamic queries, which are defined in new_queries.py. The accompanying readme.md provides guidance on configuring and running the analysis.

Setup
Clone this repository to your local machine.
Navigate to the subdirectory corresponding to the task you wish to perform.
Follow the instructions in the readme.md within each subdirectory to set up your environment.
Contributing
We welcome contributions to improve these scripts or documentation. Feel free to fork, make your changes, and submit a pull request!

Contact
For questions or support, please open an issue in this repository.
