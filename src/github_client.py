import os

def get_diff():
    github_repository = os.getenv('GITHUB_REPOSITORY')
    github_event_path = os.getenv('GITHUB_EVENT_PATH')
    print(f"repo: {github_repository}")
    print(f"event path: {github_event_path}")