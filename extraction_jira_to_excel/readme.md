"""
# JIRA Issue Extractor and Excel Exporter

This Python script connects to the JIRA API to retrieve issues based on a specified JQL query,
extracts and formats the relevant data, and then exports this data to an Excel file.

## Features

- Connects to any JIRA instance using API tokens.
- Filters issues based on a customizable JQL query.
- Extracts specified fields from issues, including custom fields.
- Exports the data into a well-structured Excel file.

## Requirements

To run this script, you need Python installed on your system along with the following Python packages:
- `jira`
- `xlsxwriter`
- `re` (part of the standard library)

You can install the necessary packages using pip:

```sh
pip install jira xlsxwriter
