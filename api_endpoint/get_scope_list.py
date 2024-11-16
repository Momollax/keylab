import requests 

def get_scope_list(api_token, gitlab_url, project_id):
    print(f"\n[+] Getting project {project_id} token scope data...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}/job_token_scope"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"    [-] Unable to get projects info : {response.status_code}")
        print("     ", response.json())