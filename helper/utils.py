import os.path
import tempfile
from hashlib import sha3_512


def cache_tmp(function):
    def wrapper(url, *args, **kwargs):
        filename = sha3_512(url.encode()).hexdigest()
        tmp_dir = tempfile.gettempdir()
        tmp_file_path = os.path.join(tmp_dir, filename)
        if not os.path.isfile(tmp_file_path):
            output = function(url, *args, **kwargs)
            with open(tmp_file_path, 'w') as f:
                f.write(output)
            return output
        with open(tmp_file_path, 'r') as f:
            return f.read()

    return wrapper
