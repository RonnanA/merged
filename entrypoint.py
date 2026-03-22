import time
import sys
import os

name = sys.argv[1] if len(sys.argv) > 1 else ""
print(f"Hello {name}")

rn = time.ctime()

github_output = os.getenv('GITHUB_OUTPUT')
if github_output:
    with open(github_output, "a") as f:
        f.write(f"time={rn}\n")
