#!/usr/bin/python3
"""
This module finds character frequency in a given string.
"""


def char_frequency(str1):
    """
    The function returns a frequency_dictionary of character frequencies in a string
    """
    frequency_dict = {}

    for n in str1:
        # Retrieve the keys (unique charcters) in the 'frequency_dict' dictionary.
        keys = frequency_dict.keys()

        # Check if the character 'n' is already a key in the frequency_dictionary.
        if n in keys:
            frequency_dict[n] += 1
        else:
            # If 'n' is not a key, add it to the frequency_dictionary with a frequency
            frequency_dict[n] = 1

    return frequency_dict


# Call the function with an argument and print the result
print(char_frequency("Pythonic Brian"))
