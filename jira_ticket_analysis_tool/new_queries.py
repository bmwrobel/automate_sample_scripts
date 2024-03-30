dict_of_queries = {
    "open": {
        "Version_1": 'project = YOURPROJECT AND type = IssueType AND status in (Status1, Status2) AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_1)',
        "Version_2": 'project = YOURPROJECT AND type = IssueType AND status in (Status1, Status2) AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_2)',
        # Add more versions as needed
    },
    "in_progress": {
        "Version_1": 'project = YOURPROJECT AND type = IssueType AND status in ("In Progress") AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_1)',
        "Version_2": 'project = YOURPROJECT AND type = IssueType AND status in ("In Progress") AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_2)',
        # Add more versions as needed
    },
    "done": {
        "Version_1": 'project = YOURPROJECT AND type = IssueType AND status in (Closed,Resolved) AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_1)',
        "Version_2": 'project = YOURPROJECT AND type = IssueType AND status in (Closed,Resolved) AND component in '
                     '(Component1, "Component2", Component3) AND (affectedVersion ~ "VersionPattern-*" OR '
                     'affectedVersion is EMPTY) AND (fixVersion ~ "VersionPattern-*" OR fixVersion is EMPTY OR '
                     'fixVersion = NOT_APPLICABLE) AND fixVersion in(Version_2)',
        # Add more versions as needed
    }
}

# Explanation and Guidelines: - `YOURPROJECT`: Replace with your actual JIRA project key. - `IssueType`: Replace with
# the type of issue you're querying for (e.g., Bug, Task). - `Status1, Status2`: Replace with the statuses you're
# interested in (e.g., New, Open, Pending). - `Component1, "Component2", Component3`: Replace with the actual
# components from your project. Use quotes if the component name contains spaces. - `VersionPattern-*`: Use a pattern
# matching your project's versioning scheme. - `Version_1`, `Version_2`: These are placeholders for actual version
# names or numbers in your project. - Adjust the `status in (...)` and `fixVersion in(...)` clauses according to your
# needs.
