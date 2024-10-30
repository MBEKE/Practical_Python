#!/usr/bin/python3

def remove_duplicate(input_string):
    # Track characters that have already appeared
    seen = set()
    result = []

    for char in input_string:
        # Only add the character if it has not been seen before
        if char not in seen:
            seen.add(char)
            result.append(char)

    # Join the list into a single string
    unique = ''.join(result)
    return unique

# Example usage
input_string = (" We are 5 Great Engineers")
print(remove_duplicate(input_string))