import os
import sys


def get_local_repos():
    repos = []

    for root, dirs, files in os.walk(sys.argv[1]):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")

    return sorted(repos)


local_repos = get_local_repos()

print("Local repositories found:", len(local_repos))

print("Repositories:")
for repo in local_repos:
    print(" *", repo)
