def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_frequency = get_char_frequency(text)
    sorted_char_list = sort_char_frequency(char_frequency)

    print_report(book_path, num_words, sorted_char_list)


def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()


def count_words(text):
    return len(text.split())


def get_char_frequency(text):
    frequency = {}
    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


def sort_char_frequency(frequency_dict):
    return sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)


def print_report(book_path, num_words, sorted_char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char, count in sorted_char_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
