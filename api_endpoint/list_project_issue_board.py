import requests

def list_project_issue_board(api_token, gitlab_url, project_id):
    print(f"\n[+] Listing Issue Boards for project {project_id}...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}/boards"
    headers = {
        "PRIVATE-TOKEN": api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        boards = response.json()
        for board in boards:
            print(f"    [+] Board Name: {board['name']}")
            print(f"        - Board ID: {board['id']}")
            print(f"        - Project Name: {board['project']['name']}")
            print(f"        - Web URL: {board['project']['web_url']}")
            print(f"        - Last Activity At: {board['project']['last_activity_at']}")
            print(f"        - Hide Backlog List: {board['hide_backlog_list']}")
            print(f"        - Hide Closed List: {board['hide_closed_list']}\n")
    else:
        print(f"    [-] Unable to get issue boards info: {response.status_code}")
        print("     ", response.json())
