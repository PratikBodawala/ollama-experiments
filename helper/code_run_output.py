def run_python_and_provide_output_context(filepath: str) -> str:
    """
    Runs the Python script at the given file path and returns the output context.

    :param filepath: The path to the Python script to run.
    :return: The output context of the script.
    """
    import subprocess

    try:
        # Run the Python script and capture the output
        result = subprocess.run(['python', filepath], capture_output=True, text=True)
        output = result.stdout

        # Provide the output context to the user
        return f"Output:\n{output}\n"
    except Exception as e:
        import traceback
        return (
            f"An error occurred: {e}\n\n"
            f'{traceback.format_exc()}\n'
        )


def code_run_output(filepath: str) -> str:
    """
    # Specify the path to the Python script you want to run
    filepath = "experiment.py"
    """
    # Run the Python script and provide the output context
    output_context = run_python_and_provide_output_context(filepath)

    return f"File content:\n\n{open(filepath).read()}\n {output_context}"
