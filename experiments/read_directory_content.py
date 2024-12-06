from pprint import pprint

import ollama

from helper.filesystem import get_directory_context
from helper.prompt import prompt

# List available models from Ollama
pprint(list(map(lambda x: x.model, ollama.list().models)))

# Get user input with directory context
content = prompt('Improve following code.', get_directory_context('/tmp/ollama'))

print(content)

# Generate chat response using Ollama model
response = ollama.chat(
    'qwen2.5-coder:14b',
    [{'content': content, 'role': 'user'}],
    options=ollama.Options(num_thread=15)
)['message']['content']
print(response, flush=True)
