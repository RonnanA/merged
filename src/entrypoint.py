import time
import sys
import os
import json
from github_client import get_diff, post_comment, delete_previous_comment


github_token = sys.argv[1]
ollama_url = sys.argv[2]
ollama_model = sys.argv[3]

print("in entrypoint.py")
print(f"the github token is: {github_token}")
print(f"the ollama url is: {ollama_url}")
print(f"the ollama model is: {ollama_model}")

rn = time.ctime()

github_output = os.getenv('GITHUB_OUTPUT')
if github_output:
    with open(github_output, "a") as f:
        f.write(f"time={rn}\n")

# Get the owner and repo value from GITHUB_REPOSITORY ENV var
    repo = os.getenv('GITHUB_REPOSITORY')
    if not repo:
        print("Error: GITHUB_REPOSITORY env var not set")
        sys.exit(1)

# Get the PR number from the GITHUB_EVENT_PATH ENV var
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

sample_text = "sample comment for PR"

get_diff(github_token, repo, pr_number)
delete_previous_comment(github_token, repo, pr_number)
#post_comment(github_token, repo, pr_number, sample_text)
