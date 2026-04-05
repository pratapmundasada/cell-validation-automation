import os
from jira import JIRA

def test_connection():
    server = os.getenv("JIRA_SERVER")
    email = os.getenv("os.getenv('JIRA_EMAIL')") # Matches the YML env name
    token = os.getenv("JIRA_API_TOKEN")

    print(f"Checking connection to: {server}")

    if not server or "localhost" in server:
        print("❌ Error: JIRA_SERVER is not being passed correctly from GitHub Secrets.")
        return

    try:
        # The actual handshake
        jira = JIRA(server=server, basic_auth=(email, token))
        print(f"✅ Success! Connected to Jira: {jira.server_info()['serverTitle']}")
    except Exception as e:
        print(f"❌ Connection Failed. Details: {e}")

if __name__ == "__main__":
    test_connection()
