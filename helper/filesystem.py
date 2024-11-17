import os
import glob
import logging

ignore_files = ['venv', '.pyc']

def get_directory_context(directory_path: str):
    """
    Recursively reads the content of all files in the given directory and subdirectories.

    :param directory_path: Path to the directory whose contents are to be read.
    :return: A string containing the context of all files within the directory.
    """
    context = ""

    # Use glob to find all files recursively
    for file_path in glob.glob(os.path.join(directory_path, '**', '*'), recursive=True):
        if os.path.isfile(file_path):  # Check if it's a file
            if any(ignore_file in file_path for ignore_file in ignore_files):
                continue
            # print(file_path)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    context += f"# File: {file_path}\n{content}\n"
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        context += f"File: {file_path}\n{content}\n"
                except Exception as e:
                    logging.error(f"Error reading {file_path}: {e}")

    return context

if __name__ == "__main__":
    # Specify the directory path you want to read
    path = "."

    # Get the context of all files in the directory
    ollama_context = get_directory_context(path)

    print(ollama_context)