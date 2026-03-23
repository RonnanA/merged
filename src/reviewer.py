import requests

def get_code_review(ollama_url, ollama_model):
    prompt_file = '/src/prompt.txt'

    with open(prompt_file, 'r') as f:
        prompt = f.read()

    print(f"prompt text: {prompt}")

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

