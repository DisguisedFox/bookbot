def get_num_words(book_text):
    num_words = book_text.split()
    return len(num_words)

def get_chars_dict(book_text):
    char_counts = {}
    for char in book_text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def chars_dict_to_sorted_list(char_counts):
    result_list = []
    for char, num in char_counts.items():
        result_list.append({"char": char, "num": num})
    result_list.sort(reverse=True, key=sort_on)
    return result_list

def sort_on(item):
    return item["num"]