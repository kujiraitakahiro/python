#This program is text data sort program
#
#usage
#python3 sort_file.py OriginalFileName OutputFileName (False)
#3rd argument is option. Default(if you Unspecified) is True.
#
import sys

def sort_file(input_file, output_file, case_insensitive=True):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    if case_insensitive:
        lines.sort(key=str.lower)
    else:
        lines.sort()

    with open(output_file, 'w') as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) > 3 and sys.argv[3] == 'False':
        case_insensitive = False
    else:
        case_insensitive = True

    sort_file(input_file, output_file, case_insensitive)

