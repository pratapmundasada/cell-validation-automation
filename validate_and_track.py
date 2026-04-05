import os
import pandas as pd
import numpy as np
from jira import JIRA

# 1. Connect to Jira using GitHub Secrets
jira_server = os.getenv("JIRA_SERVER")
jira_email = os.getenv("JIRA_EMAIL")
jira_token = os.getenv("JIRA_API_TOKEN")

# Initialize Jira client
jira = JIRA(server=jira_server, basic_auth=(jira_email, jira_token))

def run_validation():
    # Simulate loading a dataset
    data = {'cell_id': [f'C-{i}' for i in range(10)], 
            'voltage': np.random.uniform(3.0, 4.5, 10)}
    df = pd.DataFrame(data)
    
    # Logic: Identify any cell with voltage > 4.2 (Overcharged)
    failures = df[df['voltage'] > 4.2]
    
    for _, row in failures.iterrows():
        summary = f"CRITICAL: Cell {row['cell_id']} Overcharged"
        description = f"Validation failed. Voltage detected at {row['voltage']}V."
        
        # Create issue in Jira
        jira.create_issue(project='CELL', summary=summary, 
                          description=description, issuetype={'name': 'Bug'})
        print(f"Logged Jira Bug for {row['cell_id']}")

    df.to_csv("latest_results.csv", index=False)

if __name__ == "__main__":
    run_validation()
