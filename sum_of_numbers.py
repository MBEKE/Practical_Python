#!/usr/bin/python3

def sum_of_numbers(numbers):
    """
    Calculate the sumof all numeric values in a list.

    Args:
        int or float: The sum of numeric values in the list
    """
    # Check if the list is empty
    if not numbers:
        print("The list is empty")
        return 0
    
    # Filter out non-numeric values and sum of the numeric ones
    numeric_sum = sum(num for num in numbers if isinstance(num, (int, float)))

    return numeric_sum

# Test cases
print(sum_of_numbers([1, 2, 3, 4]))            
print(sum_of_numbers([1, -2, 3.5, -4]))
print(sum_of_numbers([0, 0, 0, 0]))
print(sum_of_numbers(["a", 3, 4, "b"]))
print(sum_of_numbers([]))
print(sum_of_numbers([-5, -15, -10])) 
