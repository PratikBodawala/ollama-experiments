import  ollama
from pprint import pprint
from helper.filesystem import get_directory_context
from helper.prompt import prompt

pprint(list(map(lambda x: x['name'], ollama.list()['models'])))

content = prompt('Improve following code.', get_directory_context('.'))
print(content)
print(ollama.chat(
    'qwen2.5-coder:14b',
    [{'content': content, 'role': 'user'}],
    options=ollama.Options(num_thread=15)
)['message']['content'], flush=True)

