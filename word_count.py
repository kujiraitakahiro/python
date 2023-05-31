#usage
#python3 word_count.py InputFileName OutputFileName
#
import sys
from collections import Counter

def count_words(input_file, output_file):
    with open(input_file, 'r') as f:
        words = [line.strip() for line in f]

    word_counts = Counter(words)

    with open(output_file, 'w') as f:
        for word, count in word_counts.items():
            f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python word_count.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    count_words(input_file, output_file)

