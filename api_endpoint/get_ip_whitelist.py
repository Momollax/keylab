import requests 

def get_ip_whitelist(api_token, gitlab_url, group_id):
    print(f"\n[+] Getting project ip whitelist...")
    url = f"{gitlab_url}/api/v4/groups/{group_id}/allowed_ip"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"    [-] Unable to get projects info : {response.status_code}")
        print("     ", response.json())