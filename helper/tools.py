from pprint import pprint

import ollama
from ollama._types import ListResponse
from typing_extensions import Sequence

from helper.utils import cache_tmp


def get_all_models(filter_out=None) -> Sequence[ListResponse.Model]:
    for model in ollama.list().models:
        if filter_out and filter_out in model.model:
            continue
        yield model


@cache_tmp
def get_models_capability(model_obj):
    return ollama.chat(
        model_obj.model,
        [{'content': "What can you do? describe in only keywords", 'role': 'user'}],
        options=ollama.Options(num_thread=15)
    )['message']['content']


def choose_best_model_from_prompt(prompt: str) -> str:
    ask_to_ollama = '''which model is best for this prompt? following are the models and their capabilities
    '''

    for model in get_all_models(filter_out='embed'):
        ask_to_ollama += f"{model.model} : {get_models_capability(model)}\n"

    ask_to_ollama += '''Please choose the best model for this prompt, and provide the model name as the response.
    '''

    ask_to_ollama += prompt

    output = ollama.chat(
        'phi4',
        [ollama.Message(role='user', content=ask_to_ollama)],
        options=ollama.Options(num_thread=15)
    )

    pprint(output)

    for _ in get_all_models():
        if _.model.lower() in output.message.content.lower():
            return _.model


if __name__ == "__main__":
    for i, model in enumerate(get_all_models(filter_out='embed')):
        print(i, model.model)

