import os
from jira import JIRA

def create_and_attach():
    # 1. Setup Connection
    server = os.getenv("JIRA_SERVER")
    email = os.getenv("JIRA_EMAIL")
    token = os.getenv("JIRA_API_TOKEN")
    jira = JIRA(server=server, basic_auth=(email, token))

    # 2. Define Issue Details (Update 'BTU' to your project key)
    issue_dict = {
        'project': {'key': 'KAN'},
        'summary': 'Cell Validation Report - Automated Upload',
        'description': 'Automated ticket created by GitHub Actions with cell validation results.',
        'issuetype': {'name': 'Task'}, # Or 'Bug' / 'Story'
    }

    try:
        # 3. Create the Issue
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"✅ Ticket Created: {new_issue.key}")

        # 4. Attach the CSV
        csv_file_path = 'latest_results.csv' # Ensure this matches your filename
        
        if os.path.exists(csv_file_path):
            with open(csv_file_path, 'rb') as f:
                jira.add_attachment(issue=new_issue, attachment=f)
            print(f"📎 File '{csv_file_path}' attached successfully to {new_issue.key}")
        else:
            print(f"❌ Error: {csv_file_path} not found in directory.")

    except Exception as e:
        print(f"❌ Failed to complete Jira task: {e}")

if __name__ == "__main__":
    create_and_attach()
