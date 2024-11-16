import requests
import subprocess

def download_project_http(api_token, gitlab_url, project_id, repo_name):
    print(f"\n[+] Downloading project {project_id} via http data...")
    url = f"{gitlab_url}/api/v4/projects/{project_id}/repository/archive.zip"
    headers = {
        "PRIVATE-TOKEN":api_token
    }
    try:
        response = requests.get(url, headers=headers,stream=True)
        response.raise_for_status()
        output_file = "./download/" + repo_name + ".zip"
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"    [+] Repo correctly download under name {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"    [-] Can't download repo with http: {e}")
