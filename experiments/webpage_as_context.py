import ollama

from helper.prompt import prompt
from helper.webpage import fetch_html_content

content = prompt('List out all the queens from game of thrones',
                 fetch_html_content('https://en.wikipedia.org/wiki/Game_of_Thrones'))
print(content)

# Generate chat response using Ollama model
response = ollama.chat(
    'llama3.2:latest',
    [{'content': content, 'role': 'user'}],
    options=ollama.Options(num_thread=15)
)['message']['content']
print(response, flush=True)
