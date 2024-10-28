#!/usr/bin/python3
'''
This module replaces the occurences of the 1st character of an input string
to '$' throught the string exept the 1st occurence
'''
def change_char(str1):
    '''
    This function takes one argument, 'str1', finds and replaces the occcurences
    of the 1st char throughout the string
    '''
    first_char = str1[0]

    # Replace all occurences of the 'first_char' with '$' in the 'str1'
    replaced = str1[1:].replace(first_char, '$')
    # Return modified 'str1' string.
    str1 = first_char + replaced
    return str1

# Call the change_char() function with the argument 'restart'
# and print the resulting new string
print(change_char('restart'))
