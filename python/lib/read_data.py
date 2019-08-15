import os.path
import json

class Base(Exception):
    pass

class FileNotFoundError(Base):
    '''Raise FileNotFound'''
    def __init__(self, message, *args):
        self.message = message # without this you may get DeprecationWarning
        super(FileNotFoundError, self).__init__(message, *args)

def read_json_file(json_file):
    if __file_exists(json_file):
        with open(json_file) as input_file:
            data = json.load(input_file)
        return data
    else:
        raise FileNotFoundError(f"File {json_file} not found.")

def __file_exists(json_file):
    return os.path.isfile(json_file)
