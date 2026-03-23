from ollama import chat

def get_code_review():
    prompt_file = 'prompt.txt'

    with open(prompt_file, 'r') as f:
        prompt_text = f.read()

    print(f"prompt text: {prompt_text}")

    response = chat(model='qwen2.5-coder:1.5b', messages=[
        {
            'role': 'user',
            'content': prompt_text,
        },
    ])
    
    pr_comment = response.message.content
    return pr_comment

