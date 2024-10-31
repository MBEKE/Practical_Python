#!/usr/bin/python3

def build_dict_from_tuples(tuple_list):
    '''
    Builds and returns a dictionary from a list of two-item tuples

    Args:
       tuple_list (list): List of tuples, where each tuple contains a key and a value
    Returns:
        dict: Dictionary created from the list of tuples
    '''
    # Convert list of tuples to dictionary
    result_dict = dict(tuple_list)
    return result_dict

# Example usage
tuple_list = [("name", "Alice"), ("age", 25), ("city", "New York")]
result_dict = build_dict_from_tuples(tuple_list)

print("Dictionary from list of tuples:", result_dict)