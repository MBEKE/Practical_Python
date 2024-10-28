#!/usr/bin/python3
'''
This module defines a function to swap the first two charaters of two given strings
and return a single string with the modified versions of each input string separated by space
'''
def chars_mix_up(a, b):
    '''
    Swaps the first two characters of each string and returns them as a single string

    Args:
         a (str): The first input string.
         b (str): The second input string.
    
    Returns:
         str: A single string combining the modified versions of 'a' an 'b' separated by space
    '''
    # Swap the firs two characters of each string
    new_a = b[:2] + a[2:]

    new_b = a[:2] + b[2:]

    # Return the modified strings separated by a space
    return new_a + ' ' + new_b

# Test the function with simple input
print(chars_mix_up('abc','xyz'))
