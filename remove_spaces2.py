#this program's usage
#python remove_spaces2.py <your_input_file_path> <your_output_file_path>

import sys

def remove_spaces_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content_without_spaces = content.replace(' ', '').replace('　', '')
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content_without_spaces)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide an input file path and an output file path as command line arguments.")
        sys.exit(1)
    
    remove_spaces_from_file(sys.argv[1], sys.argv[2])

