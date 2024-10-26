#!/usr/bin/python3
'''
This module containes a function to calculate the length of a string
'''


def string_length(str1):
    '''
    The function returns the number of characters in a given string
    '''
    count = 0

    for _ in str1:
        count += 1

    return count
print(string_length('I am Pythonic Brian'))
