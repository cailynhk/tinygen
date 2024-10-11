import requests
import logging
import dotenv
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

dotenv.load_dotenv('.env.local')
github_token = os.getenv("GITHUB_TOKEN")

def extract_owner_repo(url, headers):
    # Remove the protocol part (https://)
    if url.startswith("https://"):
        url = url[len("https://"):]
    
    # Split the URL by '/'
    parts = url.split('/')
    
    # Ensure the URL has at least three parts (domain, owner, and repo)
    if len(parts) >= 3:
        owner = parts[1]
        repo = parts[2]
        base_url = f"https://api.github.com/repos/{owner}/{repo}"
        print(headers)
        logging.info(f"Fetching repo in github.py: {base_url}")
        response = requests.get(base_url, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Invalid URL: {response.status_code}")
        response = response.json()
        default_branch = response["default_branch"]
        return owner, repo, default_branch
    else:
        raise ValueError("Invalid URL")

def fetch_files_in_repo(url="", token=""):
    headers = {
        "Authorization": f"token {token}"
    }

    if url == "":
        raise ValueError("URL is empty")
    owner, repo, default_branch = extract_owner_repo(url,headers)
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"

    repo_context_str = "{"
    response = requests.get(url, headers=headers) 
    if response.status_code != 200:
        raise ValueError(f"Invalid URL: {response.status_code}")
    response_json = response.json()
    for file in response_json["tree"]:
        if file["type"] == "blob":
            raw_download_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/{file['path']}"
            file_response = requests.get(raw_download_url,headers=headers)
            if file_response.status_code == 200:
                try:
                    file_content = file_response.content.decode('utf-8')
                    repo_context_str += f"{file['path']}: {{CONTENT:{file_content}, SHA:{file['sha']}, MODE:{file['mode']}}},"
                except UnicodeDecodeError:
                    logging.warning(f"Skipping file {file['path']} due to decoding error")
    repo_context_str += "}"

    return repo_context_str

if __name__ == "__main__":
    print(fetch_files_in_repo("https://github.com/rtyley/small-test-repo", github_token))