#!/usr/bin/python3
import array as arr

# Creating an array wieh integer type
a = arr.array('i', [1, 2, 3])
print(type(a), a)

# Creating an array wieh char type
a = arr.array('u', 'BAT')
print(type(a), a)

# Creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print(type(a), a)
