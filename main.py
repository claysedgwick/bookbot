# Imports stat functions from stats.py file
from stats import count_words, count_characters, sort_character_count
from sys import argv

# Takes a relative filepath input and returns file content as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_count = sort_character_count(count_characters(text))

    # Prints final results to console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Prints the char and count for each alphabetical character in the sorted dictionary
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")

main()
