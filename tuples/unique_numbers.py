#!/usr/bin/python3

def get_unique_elements(input_tuple):
    """
    Takes a tuple as input and returns a new tuple with unique elements.
    
    Parameters:
        input_tuple (tuple): The tuple from which unique elements are to be extracted.
    
    Returns:
        tuple: A new tuple containing only the unique elements of the input tuple.
    """
    unique_tuple = ()
    for x in input_tuple:
        if x not in unique_tuple:
            unique_tuple += (x,)
    return unique_tuple

# Example usage
tuple1 = (1, 9, 1, 6, 3, 4, 5, 3, 3, 4, 2, 8)
unique_tuple = get_unique_elements(tuple1)

print("Original tuple:", tuple1)
print("Unique numbers:", unique_tuple)
