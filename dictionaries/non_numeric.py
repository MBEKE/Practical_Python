#!/usr/bin/python3

def extract_non_numeric_values(input_dict):
    """
    Extracts and returns a new dictionary containing only key-value pairs
    where the value is non-numeric (no an integer or float)

    Args:
       input_dict (dict): The original dictionary

    Returns:
        dict: A dictionary with non-numeric values
    """
    # Create a new dictionay to store non-numeric key-value pairs
    non_numeric_dict = {key: value for key, value in input_dict.items() if not isinstance(value, (int, float))}
    return non_numeric_dict

# Example usage
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "height": 5.6,
    "occupation": "Engineer",
    "salary": 50000
}

non_numeric_dict = extract_non_numeric_values(sample_dict)
print("Dictionary with non-numeric values:", non_numeric_dict)