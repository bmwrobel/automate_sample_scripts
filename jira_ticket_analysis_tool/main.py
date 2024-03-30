import pandas as pd
from jira import JIRA
from new_queries import dict_of_queries  # Ensure this module contains anonymized query details

# Constants for Jira API connection - Replace placeholders with your actual values
JIRA_API_URL = 'https://your-jira-instance.com'
JIRA_BEARER_TOKEN = 'your_jira_api_token_here'


def get_jira_client(url: str, token: str) -> JIRA:
    """
    Initialize and return a JIRA client using the given URL and token.

    Parameters:
    - url (str): JIRA API endpoint.
    - token (str): Personal API token for authentication.

    Returns:
    - JIRA client object.
    """
    return JIRA(url, token_auth=token)


def retrieve_jira_tickets(jira_client: JIRA, queries_dict: dict) -> pd.DataFrame:
    """
    Retrieve Jira tickets based on the provided query dictionary and return the results as a DataFrame.

    Parameters:
    - jira_client (JIRA): Authenticated JIRA client.
    - queries_dict (dict): Dictionary mapping statuses to JQL queries.

    Returns:
    - DataFrame with columns ['version', 'status', 'amount'].
    """
    rows_list = []
    for status, versions_queries in queries_dict.items():
        for version, query in versions_queries.items():
            result_tickets = jira_client.search_issues(query, maxResults=False)
            rows_list.append({"version": version, "status": status, "amount": len(result_tickets)})
    return pd.DataFrame(rows_list)


def prepare_dataframe(df: pd.DataFrame, order: list) -> pd.DataFrame:
    """
    Sort and pivot the DataFrame according to the defined order and return the pivoted DataFrame.

    Parameters:
    - df (pd.DataFrame): Original DataFrame.
    - order (list): List defining the order of statuses.

    Returns:
    - Pivoted DataFrame.
    """
    df['status'] = pd.Categorical(df['status'], categories=order, ordered=True)
    df.sort_values('status', inplace=True)
    pivot_df = df.pivot(index='status', columns='version', values='amount')
    pivot_df.loc['All'] = pivot_df.sum()
    pivot_df.fillna(0, inplace=True)
    return pivot_df.astype(int)


def save_to_excel(df: pd.DataFrame, file_name: str):
    """
    Save the given DataFrame to an Excel file with the specified file name.

    Parameters:
    - df (pd.DataFrame): DataFrame to save.
    - file_name (str): Name of the output Excel file.
    """
    df.to_excel(file_name, sheet_name='Sheet1')


def main():
    """
    Main function to execute the script.
    Connects to JIRA, retrieves tickets based on queries, sorts, pivots the data, and saves it to an Excel file.
    """
    jira_client = get_jira_client(JIRA_API_URL, JIRA_BEARER_TOKEN)
    tickets_df = retrieve_jira_tickets(jira_client, dict_of_queries)
    status_order = ['open', 'in_progress', 'done']
    sorted_df = prepare_dataframe(tickets_df, status_order)
    save_to_excel(sorted_df, 'extracted_numbers_of_tickets.xlsx')


if __name__ == "__main__":
    main()
