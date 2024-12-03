# write a code for updating all model of ollama
import ollama

from helper.tools import get_all_models


def update_all_models():
    for model in get_all_models():
        print(ollama.pull(model['name'], insecure=False, stream=True), flush=True)


if __name__ == '__main__':
    update_all_models()
