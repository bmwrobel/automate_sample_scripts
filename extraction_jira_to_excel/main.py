from jira import JIRA
import re
import xlsxwriter

# Constants for Jira API connection. Replace placeholders with your actual values.
JIRA_API_URL = 'http://your-jira-url.com'  # Example: 'https://yourcompany.atlassian.net'
JIRA_BEARER_TOKEN = 'your_token_here'  # Your JIRA API token
JIRA_JQL_QUERY = 'project = YOURPROJECT AND status = "To Do"'  # Example JQL query


def get_jira_items(url: str, token: str, query: str) -> list:
    """
    Connect to the Jira API and retrieve selected issues based on a JQL query.

    Args:
    - url (str): JIRA API URL
    - token (str): Authentication token for JIRA
    - query (str): JQL query to filter issues

    Returns:
    - list: List of issues matching the JQL query
    """
    jira = JIRA(server=url, token_auth=token)
    # Retrieve issues without a limit on the number of results
    query_issues = jira.search_issues(query, maxResults=False, fields="*all")
    return query_issues


def extract_and_format_data(issues: list) -> list:
    """
    Extract and format data from Jira issues into a list of dictionaries.

    Args:
    - issues (list): List of Jira issues

    Returns:
    - list: List of dictionaries containing the extracted data
    """
    # Regex to match a specific pattern in the external ID field
    pattern = r'(?:-\s)?[A-Za-z]+_[A-Za-z]+_[0-9]+'
    formatted_data = []

    for issue in issues:
        # Extract data from custom fields and other properties
        external_id = issue.raw['fields']['customfield_10315']
        fix_version = issue.raw['fields'].get('fixVersions', [])[-1]['name'] if issue.raw['fields'].get(
            'fixVersions') else 'None'
        filtered_ids = re.findall(pattern, external_id)

        for pos in filtered_ids:
            formatted_data.append({
                "Jira_ticket": issue.key,
                "External_ID": pos.replace(" ", ""),
                "Fix_version": fix_version
            })

    return formatted_data


def export_to_excel(data: list, filename: str):
    """
    Export a list of dictionaries to an Excel file.

    Args:
    - data (list): Data to export
    - filename (str): Name of the output Excel file
    """
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Define headers and write them to the first row of the Excel file
    headers = ["Jira ticket", "External ID", "Fix version"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Iterate over the data and write each item to the Excel file
    for row, item in enumerate(data, start=1):
        worksheet.write(row, 0, item["Jira_ticket"])
        worksheet.write(row, 1, item["External_ID"])
        worksheet.write(row, 2, item["Fix_version"])
    worksheet.autofit()
    workbook.close()


def main():
    """
    Main function to orchestrate the script execution.
    """
    # Connect to JIRA, extract and format data, then export to Excel
    issues = get_jira_items(JIRA_API_URL, JIRA_BEARER_TOKEN, JIRA_JQL_QUERY)
    formatted_data = extract_and_format_data(issues)
    export_to_excel(formatted_data, "extracted_ids_excel.xlsx")


if __name__ == "__main__":
    main()
