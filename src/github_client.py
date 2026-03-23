import requests
import json
import sys
import os

def get_diff(github_token, repo, pr_number):
    print("in github_client.py")

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


def post_comment(github_token, repo, pr_number, review_text):
    print("in post_comment.py")

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
    
    print("delete_previous_comment function complete")
