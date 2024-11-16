import requests

def get_project(api_token, gitlab_url, project_id):
    print(f"\n[+] Getting project {project_id} data...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}"
    headers = {
        "PRIVATE-TOKEN": api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        project_info = response.json()
        
        # Displaying the most interesting project information
        print(f"    [+] - Project Name: {project_info['name']}")
        print(f"        - Full Name with Namespace: {project_info['name_with_namespace']}")
        print(f"        - Project ID: {project_info['id']}")
        print(f"        - Default Branch: {project_info['default_branch']}")
        print(f"        - Created At: {project_info['created_at']}")
        print(f"        - Last Activity At: {project_info['last_activity_at']}")
        print(f"        - SSH URL to Repo: {project_info['ssh_url_to_repo']}")
        print(f"        - HTTP URL to Repo: {project_info['http_url_to_repo']}")
        print(f"        - Web URL: {project_info['web_url']}")
        print(f"        - Description: {project_info['description'] if project_info['description'] else 'N/A'}")
        print(f"        - Visibility: {project_info['visibility']}")
        print(f"        - Star Count: {project_info['star_count']}")
        print(f"        - Forks Count: {project_info['forks_count']}")
        print(f"        - Issues Enabled: {project_info['issues_enabled']}")
        print(f"        - Merge Requests Enabled: {project_info['merge_requests_enabled']}")
        print(f"        - Jobs Enabled: {project_info['jobs_enabled']}")
        print(f"        - Wiki Enabled: {project_info['wiki_enabled']}")
        try:
            print(f"        - Owner: {project_info['owner']['name']} (ID: {project_info['owner']['id']})")
        except:
            print(f"    [-] Unknow Owner")
        print(f"        - Container Registry Enabled: {project_info['container_registry_enabled']}")
        print(f"        - Packages Enabled: {project_info['packages_enabled']}")
        print(f"        - Shared Runners Enabled: {project_info['shared_runners_enabled']}")
        print(f"        - Open Issues Count: {project_info['open_issues_count']}")
        print(f"        - Container Registry Image Prefix: {project_info['container_registry_image_prefix']}")
        
    else:
        print(f"    [-] Unable to get project info: {response.status_code}")
        print("     ", response.json())