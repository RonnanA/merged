import requests

def get_code_review(ollama_url, ollama_model, pr_diff):
    prompt_file = '/src/prompt.txt'

    with open(prompt_file, 'r') as f:
        prompt_text = f.read()

    prompt = prompt_text.replace('{diff}', pr_diff)
    print(f"Prompt being sent to Ollama: {prompt[:500]}")

    response = requests.post(
        f"{ollama_url}/api/generate",
        json={
            "model": ollama_model,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    
    return response.json()['response']

