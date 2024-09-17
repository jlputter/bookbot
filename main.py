def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_len = get_num_words(text)
    words_by_letter = get_letter_count(text.lower())
    print_report(words_by_letter, words_len, book_path)

def print_report(word_dict, words_len, book_file_path):
    print(f"--- Begin report of {book_file_path} ---")
    print(f"{words_len} words found in document")
    print()

    dict_list = [{"char": k, "num": v} for k, v in word_dict.items() if k.isalpha()]
    dict_list.sort(reverse=True,key=sort_on)

    for item in dict_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times.")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def get_book_text(file_path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()