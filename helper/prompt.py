def prompt(question: str, context: str) -> str:
    """
    Prompts the user with a question and context and returns the user's response.

    :param question: The question to prompt the user with.
    :param context: The context to provide the user with.
    :return: The user's response to the question.
    """
    # print(f"Context: {context}")
    return f'{question}\n\n{context}\n'

