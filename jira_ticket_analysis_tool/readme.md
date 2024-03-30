# JIRA Ticket Analysis Tool

This Python script interfaces with the JIRA API to fetch ticket data according to specified JQL queries, organizes the data into a meaningful structure, and outputs the results to an Excel file for further analysis.

## Features

- Fetches data from JIRA based on custom JQL queries.
- Processes and organizes data using pandas DataFrames.
- Outputs data to Excel for easy viewing and analysis.

## Requirements

- Python 3.x
- pandas
- jira-python
- openpyxl (for pandas Excel output functionality)

## Setup

1. Install required Python packages:

```bash
pip install pandas jira openpyxl
