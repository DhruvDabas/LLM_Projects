import requests
import json

url = "http://127.0.0.1:11434/api/chat"
user_input = input("Enter your prompt: ")

payload = {
        "model": "deepseek-r1:7b",
        "messages": [{"role": "user", "content": user_input}],
        "stream": True
    }

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            try:
                chunk = json.loads(line.decode('utf-8').removeprefix('data: '))
                print(chunk.get('message', {}).get('content', '') or chunk.get('content', ''), end='', flush=True)
            except:
                pass  # Skip any errors silently
else:
    print(f"Error {response.status_code}: {response.text}")