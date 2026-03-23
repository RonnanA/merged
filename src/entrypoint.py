import time
import sys
import os
from github_client import get_diff


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

get_diff(github_token)
