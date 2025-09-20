def get_word_count(book_contents):
    return len(book_contents.split())

def get_all_char_count(book_contents):
    chars = {}
    for char in book_contents:
        char = char.lower()
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

def sort_on(items):
    return items["num"]

def sort_char_dict(dict):
    char_list = []
    for key in dict:
        char_list.append({"char": key, "num": dict.get(key)})
    char_list.sort(reverse=True, key=sort_on)
    return char_list