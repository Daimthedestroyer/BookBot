from stats import (
    get_book_text,
    get_num_words,
    get_num_chars,
    get_report,
    sort_chars
)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Path variable
    path = sys.argv[1]

    # Analysing
    book = get_book_text(path)
    book_lenght = get_num_words(book)
    char_count = get_report(sort_chars(get_num_chars(book)))

    # Printing to console
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(book_lenght)

    print("--------- Character Count -------")
    print(char_count[:-1]) # :-1 to get rid of newline at the end

    print("============= END ===============")

if __name__ == "__main__":
    main()