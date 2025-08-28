from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

try:
    with open(path) as f:
        f.read()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(get_num_words(path))

    print("--------- Character Count -------")
    print(formatting(num_characters(path)))


main()