def get_book_text(path):
    import sys
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    
def get_num_words(doc):
    return f"Found {len(doc.split())} total words"

def get_num_chars(doc):
    char_count = {}
    for words in doc.split():
        for char in words.lower():
            if char_count.get(char):
                char_count[char] += 1
            elif char.isalpha():
                char_count[char] = 1
    return char_count

def sort_chars(chars):
    return sorted(
        chars.items(),
        reverse = True,
        key = lambda item: item[1]
    )

def get_report(lst):
    report = ""
    for char, count in lst:
        report += char + ":" + str(count) + "\n"

    return report