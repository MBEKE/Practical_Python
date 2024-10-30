#!/usr/bin/python3

def remove_non_alphabetic(input_string):
    # Filter only alphabtic characters and join them into a new string
    cleaned_string = ''.join(char for char in input_string if char.isalpha())
    return cleaned_string

    # Example usage
input_string = "Hello, World! Welcome to Python 3.9"
print("Original String:", input_string)
print("Alphabetic-only string:", remove_non_alphabetic(input_string))

