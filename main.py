import os
import subprocess
import sys


def get_local_repos():
    repos = []

    for root, dirs, files in os.walk(sys.argv[1]):
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


local_repos = get_local_repos()

print("Local repositories found:", len(local_repos))

print("Repositories:")
for repo in local_repos:
    print(" *", repo)
    print("   * Remote URL:", get_remote_url(repo))
