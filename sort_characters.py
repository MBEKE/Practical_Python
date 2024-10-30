#!/usr/bin/python3
def sort_string_characters(input_string):
    """
    Sorts the characters in the input string alphabetically and return the sorted string

    Args:
        input_string (str): The string to be sorted
    Returns:
         str: the sorted string
    """
    # convert everything to lowecase
    lowered = input_string.lower()
    # Convert string to a list of characters
    char_list = list(lowered)

    # Sort the list of characters
    char_list.sort()
    sorted = ''.join(char_list)
    return sorted
print(sort_string_characters("I am Pythonic Brian"))