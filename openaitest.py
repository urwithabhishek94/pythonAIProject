from ollama import chat

response = chat(
    model='qwen2.5:1.5b',  # Change model name if needed
    messages=[
        {
            'role': 'user',
            'content': 'Hello, who are you?'
        }
    ]
)

print(response['message']['content'])