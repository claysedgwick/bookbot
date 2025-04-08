# Imports stat functions from stats.py file
from stats import count_words, count_characters, sort_character_count
import sys
from sys import argv

# Takes a relative filepath input and returns file content as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    # Checks if sys.argv passes at least two arguments
    # Otherwise, prints program usage statment and exits with error code 1   
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Initializes required variables for print statements
    # filepath set to second argument passed from CLI
    filepath = argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_char_count = sort_character_count(char_count)

    # Prints final results to console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Prints the char and count for each alphabetical character in the sorted dictionary
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")

main()
