#!/usr/bin/python3

def difference_from_average(numbers):
    """
    Calculates the difference beween each number in the list and the average of all numbers

    Args:
       numbers (list): List of numerical values
    Returns:
        list: List of differences between each number and the average
    """
    if not numbers:
        return []
    
    # Calculate the average of all numbers
    average = sum(numbers) / len(numbers)

    # Calculate the differences between each number and the average
    differences = [round(num - average, 2) for num in numbers]
    return differences

# Example usage
numbers = [10, 15, 20, 25, 30]
result = difference_from_average(numbers)

print("Original numbers:", numbers)
print("Difference from average:", result)
