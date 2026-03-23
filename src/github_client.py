import requests
import json
import sys
import os

def get_diff(github_token):
    print("in github_client.py")
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


    api_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        'Accept': '"application/vnd.github.v3.diff"',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2026-03-10'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        pr_diff = response.text
        print("\nPR DIFF:")
        print(pr_diff)

    except requests.exceptions.RequestException as e:
        print(f"Error getting diff: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

    print("get diff function complete")
    return repo, pr_number, pr_diff


def post_comment(github_token, repo, pr_number, review_text):
    api_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2026-03-10'
    }

    data = {
        'body': f'<!-- merged. -->\n{review_text}'
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        print("Comment posted successfully")

    except requests.exceptions.RequestException as e:
        print(f"Error posting comment: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

    print("post comment function complete")

def delete_previous_comment(github_token, repo, pr_number):
    api_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2026-03-10'
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        comments_data = response.json()
        if isinstance(comments_data, list):
            for comment in comments_data:
                comment_id = comment.get('id')
                comment_body = comment.get('body')

        elif isinstance(comments_data, dict):
            comment_id = comments_data.get('id')
            comment_body = comments_data('body')
        
        print(f"Comment id: {comment_id}")
        print(f"Comment body: {comment_body}")

    except requests.exceptions.RequestException as e:
        print(f"Error deleting comment: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")
