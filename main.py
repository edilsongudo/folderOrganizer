from utils import *

def main(path):
    extensions_categorized = load_extensions_list('all_filetypes.json')

    os.chdir(path)

    filenames = os.listdir()

    for filename in filenames:
        file_extension = get_filename_extension_and_remove_dot(filename)

        extension_match = extensions_categorized.get(file_extension)

        if extension_match:
            extensions_category = extension_match[-1]
            move_file(filename, extensions_category)


# Replace with your download folder path
main('c:/Users/DELL/Downloads')