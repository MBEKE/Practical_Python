#!/usr/bin/python3

def sum_of_numbers(input_tuple):
    '''Calculate the sum of all numeric elements in a  tuples'''
    total_sum = 0
    for item in input_tuple:
        if isinstance(item, (int, float)): # check if item is a number
            total_sum += item
        else:
            print(f'Skipping non-numeric value:{item}')
    return total_sum

# Example Usage
input_tuple = (5, "apple", 10, 2.5, "banana", 7)
result = sum_of_numbers(input_tuple)
print("Sum of numeric values:", result)
