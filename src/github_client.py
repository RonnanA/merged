import requests
import json
import sys
import os

def get_diff(github_token):
    github_repository = os.getenv('GITHUB_REPOSITORY')
    if not github_repository:
        print("Error: GITHUB_REPOSITORY env var not set")
        sys.exit(1)
    repo = github_repository.split("/")

    github_event_path = os.getenv('GITHUB_EVENT_PATH')
    if not github_event_path:
        print("Error: GITHUB_EVENT_PATH env var not set")
        sys.exit(1)
    try:
        with open(github_event_path, "r") as f:
            event_payload = json.load(f)
            pr_number = event_payload['pull_request']['number']

            if pr_number:
                print(f"Successfully found the PR number: {pr_number}")

            
    except FileNotFoundError:
        print(f"Error: GitHub event file not found at {github_event_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the GitHub event file at {github_event_path}")
        sys.exit(1)

    print(f"GET https://api.github.com/repos/{repo[0]}/{repo[1]}/pulls/{pr_number}")