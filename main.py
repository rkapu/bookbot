def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_count = get_words_count(book_text)
    chars_count = get_chars_count(book_text)
    print(chars_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    return len(text.split())

def get_chars_count(text):
    chars = {}

    for c in text:
        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

main()
