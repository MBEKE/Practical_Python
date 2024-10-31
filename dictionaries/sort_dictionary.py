#!/usr/bin/python3

# List of dictionaries to be sorted
people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 23},
    {"name": "Charlie", "age": 32},
    {"name": "David", "age": 25}
]

# Sorting the list of dictionariew by 'age'
sorted_people = sorted(people, key = lambda person: person['age'])

# Printing the sorted list
print("Sorted list by age:")
for person in sorted_people:
    print(person)