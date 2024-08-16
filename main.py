def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n")
    sorted_dict = sort_dict(num_char)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    char_dict = {}
    for c in text:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_dict(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    for i in sorted_items:
        if i[0].isalpha():
            print(f"The '{i[0]}' character was found '{i[1]}' times")

main()