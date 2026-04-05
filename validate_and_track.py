import pandas as pd
import os
from jira import JIRA

def connect_to_jira():
    """Secure connection using GitHub Secrets"""
    return JIRA(
        server=os.getenv("JIRA_SERVER"), 
        basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
    )

def sync_results_to_jira():
    # 1. Load the data the dashboard is showing
    if not os.path.exists('latest_results.csv'):
        print("❌ CSV not found. Nothing to sync.")
        return
        
    df = pd.read_csv('latest_results.csv')
    jira = connect_to_jira()
    
    # 2. Filter for FAILURES (e.g., Cell 3, Cell 7, Cell 10)
    failures = df[df['status'] == 'FAIL']
    
    for _, row in failures.iterrows():
        cell_id = row['cell_id']
        summary = f"Validation Failure: {cell_id}"
        
        # 3. Principal Move: Check if ticket already exists to avoid duplicates
        existing_issues = jira.search_issues(f'project=BTU AND summary ~ "{cell_id}" AND status != Closed')
        
        if len(existing_issues) == 0:
            print(f"🚀 Creating new ticket for {cell_id}...")
            issue_dict = {
                'project': 'KAN',
                'summary': summary,
                'description': (
                    f"Automated Alert from Agratas CI Pipeline\n"
                    f"----------------------------------------\n"
                    f"Cell ID: {cell_id}\n"
                    f"Capacity: {row['discharge_capacity_ah']} Ah\n"
                    f"Max Temp: {row['max_temp_c']}°C\n"
                    f"DCR: {row['dcr_mOhm']} mOhm\n"
                    f"Test Stage: {row['test_stage']}"
                ),
                'issuetype': {'name': 'Bug'},
                'priority': {'name': 'High'}
            }
            jira.create_issue(fields=issue_dict)
        else:
            print(f"ℹ️ Ticket for {cell_id} already exists. Skipping.")

if __name__ == "__main__":
    sync_results_to_jira()
