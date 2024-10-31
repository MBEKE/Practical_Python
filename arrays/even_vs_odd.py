#!/usr/bin/python3
import array as arr

def separate_even_odd(numbers):
    # Initialize empty arrays for even and odd numbers
    even_numbers = arr.array('i', [])
    odd_numbers = arr.array('i', [])
    
    # Loop through each number and separate based on even or odd
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers

# Initialize 'numbers' array
numbers = arr.array('i', [4, 77, 94, 21, 63, 88, 13, 4, 95, 6])

# Call the function
even_numbers, odd_numbers = separate_even_odd(numbers)

# Print results
print("Original numbers:", numbers)
print("Even numbers are:", even_numbers)
print("Odd numbers are:", odd_numbers)
