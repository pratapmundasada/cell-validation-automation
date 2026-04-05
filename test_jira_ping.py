import os
from jira import JIRA

def connect():
    # os.getenv searches the environment variables of the GitHub Runner
    server = os.getenv("JIRA_SERVER")
    email = os.getenv("JIRA_EMAIL")
    token = os.getenv("JIRA_API_TOKEN")

    # Principal Check: Ensure variables actually arrived
    if not server:
        print("❌ Error: JIRA_SERVER variable is empty. Check your YAML!")
        return

    try:
        jira = JIRA(server=server, basic_auth=(email, token))
        print(f"✅ Success! Connected to: {jira.server_info()['serverTitle']}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    connect()
