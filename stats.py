def get_book_text(path):
     with open(path) as f:
        return f.read()

def get_num_words(path):
    content = get_book_text(path).split()
    return f"Found {len(content)} total words"

def num_characters(path):
    content = get_book_text(path).lower()
    count = {}
    def sort_on(items):
        return items[1]

    for i in content:
        if i.isalpha():
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        else:
            continue

    count = sorted(
        count.items(),
        key=sort_on,
        reverse=True
    )
    return count

def formatting(sorted_list):
    for char, num in sorted_list:
        print(f"{char}: {num}")
    return "============= END ==============="
