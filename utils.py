import json
import os
import shutil

def create_folder_if_does_not_exist(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def load_extensions_list(path):
    with open(path, 'r') as file:
        extension_categorized = json.load(file)
    return extension_categorized


def get_filename_extension_and_remove_dot(filename):
    return os.path.splitext(filename)[-1].replace('.', '')


def move_file(filename, destination_folder):
    create_folder_if_does_not_exist(destination_folder)
    shutil.move(filename, f'{destination_folder}/{filename}')
    print(f'"{filename}" moved to "{destination_folder}"')