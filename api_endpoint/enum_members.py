import requests

def enum_members(api_token, gitlab_url, project_id):
    print(f"\n[+] Listing members for project {project_id}...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}/members/all"
    headers = {
        "PRIVATE-TOKEN": api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        members = response.json()
        for member in members:
            print(f"    [+] Member Name: {member['name']}")
            print(f"        - Username: {member['username']}")
            print(f"        - Access Level: {member['access_level']}")
            print(f"        - State: {member['state']}")
            print(f"        - Created At: {member['created_at']}")
            print(f"        - Membership State: {member['membership_state']}")
            print(f"        - Expires At: {member['expires_at'] if member['expires_at'] else 'No expiration'}")
            print(f"        - Profile URL: {member['web_url']}\n")
    else:
        print(f"    [-] Unable to get project members info: {response.status_code}")
        print("     ", response.json())
