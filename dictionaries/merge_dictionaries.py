#!/usr/bin/python3

def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries using the unpacking opeerator

    Args:
       dict1 (dict): First dictionary to merge.
       dict2 (dict): Second dictionary to merge

    Returns:
      dict: A new dictionary containing items from both dict1 and dict3
    """
    # Merge dictionaries using the unpacking operator
    merged_dict = (**dict1, **dict2)

# Example dictionaries
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}

# Merging the dictionaries
result_dict = merge_dictionaries(dict1, dict2)

# Printing the merged dictionary
print("Merged dictionary:", result_dict)
