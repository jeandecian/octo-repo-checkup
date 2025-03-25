import os
import subprocess
import sys


def get_local_repos(workspace_path):
    repos = []

    for root, dirs, files in os.walk(workspace_path):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")

    return sorted(repos)


def get_remote_url(repo_path):
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError:
        return None


def get_github_api_url(remote_url):
    if remote_url is None:
        return False

    GITHUB_URL = "github.com"

    if GITHUB_URL not in remote_url:
        return False

    owner, repo = (
        remote_url.split(GITHUB_URL)[1].lstrip(":/").removesuffix(".git").split("/")
    )

    return f"https://api.github.com/repos/{owner}/{repo}"


workspace_path = sys.argv[1]
local_repos = get_local_repos(workspace_path)

print("Local repositories found:", len(local_repos))

print("Repositories:")
for repo in local_repos:
    print(" *", repo.removeprefix(workspace_path + "/"))
    print("   * Path:", repo)
    remote_url = get_remote_url(repo)
    print("   * Remote URL:", remote_url)
    print("   * GitHub API URL:", get_github_api_url(remote_url))
