# Takes text input and returns total word count
def count_words(book_text):
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

# Counts the number of characters in the input text (all text converted to lowercase)
def count_characters(book_text):
    character_count = {}
    for char in book_text.lower():
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count

# Creates character count dictionary list and sorts descending by count
def sort_character_count(character_count_dict):

    # Defines key to sort dictionary list on
    def sort_on(dict):
        return dict["count"]

    dict_list = []
    for entry in character_count_dict:
        dict_list.append({"char": entry, "count": character_count_dict[entry]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
