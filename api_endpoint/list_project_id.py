import requests 

def list_project_id(api_token, gitlab_url):
    print("\n[+] Listing project ID...")
    url = f"{gitlab_url}/api/v4/projects?membership=true"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    projects = []
    repo_name = []
    if response.status_code == 200:
        project_id = response.json()
        for project in project_id:
            print(f"    [+] - Project Name: {project['name']}")
            print(f"        - ID : {project['id']}")
            print(f"        - path with namespace : {project['path_with_namespace']}")
            print(f"        - http url : {project['http_url_to_repo']}")
            print(f"        - parent id : {project['namespace']['parent_id']}")
            print(f"        - empty repo : {project['empty_repo']}")
            print(f"        - ssh url : {project['ssh_url_to_repo']}")
            projects.append(project['id'])
            repo_name.append(project['name'])
    else:
        print(f"    [-] Unable to get projects info : {response.status_code}")
        print("     ", response.json())
    return projects, repo_name