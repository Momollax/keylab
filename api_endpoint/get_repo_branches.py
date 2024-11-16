import requests

def get_repo_branches(api_token, gitlab_url, project_id):
    print(f"\n[+] Getting repository branches for project {project_id}...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}/repository/branches"
    headers = {
        "PRIVATE-TOKEN": api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        branches = response.json()
        for branch in branches:
            print(f"    [+] Branch Name: {branch['name']}")
            print(f"        - Protected: {branch['protected']}")
            print(f"        - Default Branch: {branch['default']}")
            print(f"        - Last Commit ID: {branch['commit']['short_id']}")
            print(f"        - Last Commit Message: {branch['commit']['message'].strip()}")
            print(f"        - Last Commit Author: {branch['commit']['author_name']} ({branch['commit']['author_email']})")
            print(f"        - Last Commit Date: {branch['commit']['committed_date']}")
            print(f"        - Branch URL: {branch['web_url']}\n")
    else:
        print(f"    [-] Unable to get branches info: {response.status_code}")
        print("     ", response.json())
