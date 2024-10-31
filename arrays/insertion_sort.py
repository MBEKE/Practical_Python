#!/usr/bin/python3

def insertion_sort(array):
    # Traverse through the array starting from the second element
    for i in range(1, len(array)):
        key = array[i]
        j = i -1
        # Move elements of arr[0..1] that are greater than key to one position
        while j >= 0 and array[j] > key:
            array[j +1] = array[j]
            j -= 1
        array[j + 1] = key

# Example usage
array = [12, 11, 13, 5, 6]
print("Original array:", array)

# Perform insertion sort
insertion_sort(array)

print("Sorted array:", array)