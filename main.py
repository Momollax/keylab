import os
import argparse
from dotenv import load_dotenv
from api_endpoint.list_project_id import list_project_id
from api_endpoint.list_project_issue_board import list_project_issue_board
from api_endpoint.download_project import download_project_http
from api_endpoint.get_scope_list import get_scope_list
from api_endpoint.get_repo_branches import get_repo_branches
from api_endpoint.enum_members import enum_members
from api_endpoint.get_access_request import get_groups_access_request, get_project_access_request
from api_endpoint.get_project import get_project
from api_endpoint.get_user_info import get_user_info
from api_endpoint.get_ip_whitelist import get_ip_whitelist
from api_endpoint.upload_file import upload_file_to_repo
from utils.unzip import unzip_file
from utils.find_entry_point import find_entry_point
from utils.pwn import pwn
load_dotenv()

api_token = os.getenv("API_TOKEN")
gitlab_url = os.getenv("GITLAB_URL")
group_id = os.getenv("GROUPE_ID")

def main(args):
    if args.get_user_info:
        get_user_info(api_token, gitlab_url)

    project_ids, repo_name = list_project_id(api_token, gitlab_url)
    i = 0
    for project in project_ids:
        if args.get_project_info:
            get_project(api_token, gitlab_url, project)
        
        if args.get_access_request:
            get_groups_access_request(api_token, gitlab_url, project)
            get_project_access_request(api_token, gitlab_url, project)
        
        if args.list_issues:
            list_project_issue_board(api_token, gitlab_url, project)
        
        if args.get_branches:
            get_repo_branches(api_token, gitlab_url, project)
        
        if args.download:
            download_project_http(api_token, gitlab_url, project, repo_name[i])
        
        if args.enum_members:
            enum_members(api_token, gitlab_url, project)
        
        if args.get_ip_whitelist:
            get_ip_whitelist(api_token, gitlab_url, group_id)
        
        if args.get_scope:
            get_scope_list(api_token, gitlab_url, project)
        
        if args.upload:
            if args.file_path:
                
                upload_file_to_repo(api_token, gitlab_url, project, file_path=args.file_path)
            else:
                print("Error: For uploading, you must specify --file_path, --branch, and --commit_message.")
        if args.pwn:
            download_project_http(api_token, gitlab_url, project, repo_name[i])
            name = unzip_file(repo_name[i], "pwn")
            entry_point_path, entry_point_type = find_entry_point(name)
            pwn(entry_point_path, entry_point_type)

        i = i + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for interacting with GitLab API")

    parser.add_argument("--get_user_info", action="store_true", help="Get user info")
    parser.add_argument("--get_project_info", action="store_true", help="Get project info")
    parser.add_argument("--get_access_request", action="store_true", help="Get access request info")
    parser.add_argument("--list_issues", action="store_true", help="List project issue boards")
    parser.add_argument("--get_branches", action="store_true", help="Get repository branches")
    parser.add_argument("--download", action="store_true", help="Download the project via HTTP")
    parser.add_argument("--enum_members", action="store_true", help="Enumerate project members")
    parser.add_argument("--get_ip_whitelist", action="store_true", help="Get IP whitelist")
    parser.add_argument("--get_scope", action="store_true", help="Get project scope list")
    parser.add_argument("--upload", action="store_true", help="Upload file to the repository")
    parser.add_argument("--file_path", type=str, help="Path of the file to upload")
    parser.add_argument("--pwn", type=str, help="pwn testing, modify and add a discord webhook")
    args = parser.parse_args()
    main(args)
