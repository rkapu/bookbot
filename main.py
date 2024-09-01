def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_count = get_words_count(book_text)
    chars_count_dict = get_chars_count_dict(book_text)
    chars_count_sorted_list = chars_count_dict_to_sorted_list(chars_count_dict)

    print_report(book_path, words_count, chars_count_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    return len(text.split())

def get_chars_count_dict(text):
    chars = {}

    for c in text:
        if not c.isalpha():
            continue

        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def chars_count_dict_to_sorted_list(chars_count_dict):
    dict_list = []
    for char in chars_count_dict:
        dict_list.append({"char": char, "count": chars_count_dict[char]})

    def sort_on(dict):
        return dict["count"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(book_path, words_count, chars_count_sorted_list):
    print(f"---- Begin report on {book_path}")

    print(f"{words_count} words found in the document\n")
    for char in chars_count_sorted_list:
        print(f'The \'{char["char"]}\' character was found {char["count"]} times')

    print("---- End report ----")

main()
