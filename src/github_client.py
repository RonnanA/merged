import requests

def get_diff(github_token, repo, pr_number):
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
        print("PR DIFF:")
        print(pr_diff)

    except requests.exceptions.RequestException as e:
        print(f"Error getting diff: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

    print("get diff function complete")
    return pr_diff


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


def delete_previous_comments(github_token, repo, pr_number):
    get_api_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
        'X-GitHub-Api-Version': '2026-03-10'
    }

    try:
        get_response = requests.get(get_api_url, headers=headers)
        get_response.raise_for_status()
        comments_data = get_response.json()

        for comment in comments_data:
            comment_id = comment.get('id')
            comment_body = comment.get('body')
            comment_author = comment.get('user', {}).get('login')

            if '<!-- merged. -->' in comment_body and comment_author == 'github-actions[bot]':
                delete_api_url = f"https://api.github.com/repos/{repo}/issues/comments/{comment_id}"
                delete_response = requests.delete(delete_api_url, headers=headers)
                delete_response.raise_for_status()
                print(f"Comment {comment_id} deleted successfully")

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving comment: {e}")
        print(f"Response status code: {e.response.status_code}")
        print(f"Response body: {e.response.text}")

    print("delete_previous_comment function complete")
