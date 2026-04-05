from jira import JIRA

# 1. Hardcode for a 1-time local test
JIRA_SERVER = https://revo-tech.atlassian.net/
JIRA_EMAIL =  pratap.mundasada@revo-tech.co.uk
JIRA_API_TOKEN = ATATT3xFfGF0nNdopLS2-LiiykzJ3kHRyiJDWC1UddiCq7YZDSp4DK2qoUcskfpZfbcYIUa3X3R7cEgvHmoYWZjRHY7aVGPrHLiVzC513ErUHIC3FZDnb7VnHVx__wRXZC6CGN_QScEuCtWhpyWF1Y-6d0eXpaY7L2ZaQL8UrbooZ6p6vAkiCEs=FA028563


def check():
    try:
        # Use the variables defined above
        j = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))
        print(f"✅ Connected to: {j.server_info()['serverTitle']}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    check()
