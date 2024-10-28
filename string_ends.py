#!/usr/bin/python3
"""
This module defines a function that finds and concatenates 2 characters at the end of a string
"""


def string_ends(str1):
    """
    the function takes one argument, 'str1' and retrieves
    the first2 and last 2 characters if the string length is 2 or more
    """
    # Check if the leghth of the 'str' is less than 2 characters
    if len(str1) < 2:
        return ""
    # If the string has at least 2 characters, concatenate the first 2 and the last 2
    # Return the result
    result = str1[0:2] + str1[-2:]
    return result


# Call string_ends() with different input strings and print the result
print(string_ends("The Muse"))
print(string_ends("Pas"))
print(string_ends("B"))
