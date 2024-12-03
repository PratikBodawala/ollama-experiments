from pprint import pprint

import ollama

from helper.utils import cache_tmp


def get_all_models():
    for model in ollama.list()['models']:
        yield model


@cache_tmp
def get_models_capability(model_obj: dict):
    return ollama.chat(
        model_obj['name'],
        [{'content': "What can you do? describe in only keywords", 'role': 'user'}],
        options=ollama.Options(num_thread=15)
    )['message']['content']


def choose_best_model_from_prompt(prompt: str) -> str:
    ask_to_ollama = '''which model is best for this prompt? following are the models and their capabilities
    '''

    for model in get_all_models():
        ask_to_ollama += f"{model['name']} : {get_models_capability(model)}\n"

    ask_to_ollama += '''Please choose the best model for this prompt, and provide the model name as the response.
    '''

    ask_to_ollama += prompt

    output = ollama.chat(
        'llama3.2',
        [{'content': ask_to_ollama, 'role': 'user'}],
        options=ollama.Options(num_thread=15)
    )
    message = output.pop('message')['content']

    pprint(output)

    for model in get_all_models():
        if model['name'] in message:
            return model['name']


if __name__ == "__main__":
    print(choose_best_model_from_prompt('Write a code to find the sum of all numbers in a list.'))
