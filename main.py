import sys
from stats import get_word_count, get_all_char_count, sort_char_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as f:
        book_contents = f.read()
        return book_contents

def main():
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    char_list = sort_char_dict(get_all_char_count(text))
    for item in char_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()