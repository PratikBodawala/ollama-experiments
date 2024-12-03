import os.path
import tempfile
from hashlib import sha3_512


def cache_tmp(function):
    def wrapper(*args, **kwargs):
        filename = sha3_512(('|'.join(map(str, args)) + '#' + '|'.join(kwargs.keys()) + '#' + '|'.join(
            kwargs.values())).encode()).hexdigest()
        tmp_dir = tempfile.gettempdir()
        tmp_file_path = os.path.join(tmp_dir, filename)
        if not os.path.isfile(tmp_file_path):
            output = function(*args, **kwargs)
            with open(tmp_file_path, 'w') as f:
                f.write(output)
            return output
        with open(tmp_file_path, 'r') as f:
            return f.read()

    return wrapper
