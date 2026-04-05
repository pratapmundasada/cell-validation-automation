import os
from jira import JIRA

def ping_jira():
    try:
        # Pull secrets from GitHub environment
        server = os.getenv("JIRA_SERVER")
        email = os.getenv("JIRA_EMAIL")
        token = os.getenv("JIRA_API_TOKEN")

        print(f"📡 Attempting to connect to: {server}")
        
        jira = JIRA(server=server, basic_auth=(email, token))
        
        # Get server info - this proves the connection works
        info = jira.server_info()
        print(f"✅ Success! Connected to Jira version: {info.get('version')}")
        print(f"🏢 Server Title: {info.get('serverTitle')}")
        
    except Exception as e:
        print(f"❌ Connection Failed!")
        print(f"Error Details: {e}")

if __name__ == "__main__":
    ping_jira()
