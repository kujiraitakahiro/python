#this program's usage
#python remove_spaces.py <your_input_file_path>
#
#NOTICE
#Please backup original text file, because this program doesn't have file backup fanction.#
#
import sys

def remove_spaces_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content_without_spaces = content.replace(' ', '').replace('　', '')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content_without_spaces)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a file path as a command line argument.")
        sys.exit(1)
    
    remove_spaces_from_file(sys.argv[1])
