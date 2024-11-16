import requests 

def get_groups_access_request(api_token, gitlab_url, project_id):
    print(f"\n[+] Getting group access requests...")
    url = f"{gitlab_url}/api/v4/groups/{project_id}/access_requests"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json)
    else:
        print(f"    [-] Unable to get group access info : {response.status_code}")
        print("     ", response.json())

def get_project_access_request(api_token, gitlab_url, project_id):
    print(f"\n[+] Getting project access requests...")
    url = f"{gitlab_url}/api/v4/project/{project_id}/access_requests"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json)
    else:
        print(f"    [-] Unable to get group access info : {response.status_code}")
        print("     ", response.json())