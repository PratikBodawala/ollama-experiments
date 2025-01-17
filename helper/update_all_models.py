# write a code for updating all model of ollama
import ollama

from helper.tools import get_all_models


def update_all_models():
    for model in get_all_models():
        for _ in ollama.pull(model.model, insecure=False, stream=True):
            print(_, end='')


if __name__ == '__main__':
    update_all_models()
