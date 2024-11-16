import requests
import base64
import os

def upload_file_to_repo(api_token, gitlab_url, project_id, file_path):
    print(f"\n[+] Uploading {file_path} to the repository...")
    print(project_id)
    try:
        with open(file_path, "rb") as file:
            file_content = base64.b64encode(file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"    [-] File {file_path} not found.")
        return

    # Extraire le nom de fichier sans le chemin local
    file_name = os.path.basename(file_path)
    url = f"{gitlab_url}/api/v4/projects/{project_id}/repository/files/{file_name}"
    
    headers = {
        "PRIVATE-TOKEN": api_token
    }
    params = {
        "ref": "main"
    }
    
    check_response = requests.get(url, headers=headers, params=params)

    if check_response.status_code == 200:
        method = "PUT"
        print("    [*] File exists, updating...")
    elif check_response.status_code == 404:
        method = "POST"
        print("    [*] File does not exist, creating...")
    else:
        print(f"    [-] Failed to check file existence: {check_response.status_code}")
        print("     ", check_response.json())
        return

    data = {
        "branch": "main",
        "content": file_content,
        "commit_message": ".",
        "encoding": "base64"
    }
    action = ""
    response = requests.request(method, url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        action = "created" if method == "POST" else "updated"
        print(f"    [+] File {file_name} successfully {action}.")
    else:
        print(f"    [-] Failed to {action} file: {response.status_code}")
        print("     ", response.json())