#!/usr/bin/python3

def unique_char_counts(input_string):
    # Convert the string to lowercase for sensitivity
    input_string = input_string.lower()

    # Initialize an empty dictionary to store counts
    char_count = {}

    # Loop through each character in the string
    for char in input_string:
        if char != " ": # Ignore spaces
            # If the character is already in the dictionary, increment its count
            char_count[char] =char_count.get(char, 0) + 1
      

    # Display the unique characters with their counts
    for char, count in char_count.items():
        print(f"{char}: {count}")

# Example usage
input_string = "apple pie"
unique_char_counts(input_string)

    