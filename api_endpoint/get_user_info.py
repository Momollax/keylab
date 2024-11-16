import requests 

def get_user_info(api_token, gitlab_url):
    print("\n[+] Getting user info...")
    url = f"{gitlab_url}/api/v4/user"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print(f"    [+] - Username: {user_info['username']}")
        print(f"        - Compete name : {user_info['name']}")
        print(f"        - Email : {user_info['email']}")
        print(f"        - ID : {user_info['id']}")
    else:
        print(f"    [-] Unable to get User info : {response.status_code}")
        print("     ", response.json())