from pprint import pprint

import ollama

from helper.prompt import prompt
from helper.webpage import fetch_html_content

# List available models from Ollama
pprint(list(map(lambda x: x['name'], ollama.list()['models'])))

# Get user input with directory context
# content = prompt('Improve following code.', get_directory_context('.'))
content = prompt('List out all the queens from game of thrones?',
                 fetch_html_content('https://en.wikipedia.org/wiki/Game_of_Thrones'))
print(content)

# Generate chat response using Ollama model
response = ollama.chat(
    # 'qwen2.5-coder:14b',
    'llama3.2:3b-instruct-fp16',
    [{'content': content, 'role': 'user'}],
    options=ollama.Options(num_thread=15)
)['message']['content']
print(response, flush=True)