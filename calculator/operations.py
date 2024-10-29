#!/usr/bin/python3
'''
operations.py

This module contains functions for  basic arithmetic operations:
addition, substraction, multiplication and division
'''
def add(a, b):
    '''
    Args:
    a (float): the first number
    b (float): the second number.

    Returns:
    float: The sum of a and b
    '''
    return a + b

def subtract(a, b):
    '''
    Args:
    a (float): the first number
    b (float): the second number.

    Returns:
    float: The difference of a and b
    '''
    return a - b

def multiply(a, b):
    '''
    Args:
    a (float): the first number
    b (float): the second number.

    Returns:
    float: The product of a and b
    '''
    return a * b

def divide(a, b):
    '''
    Args:
    a (float): the first number
    b (float): the second number.

    Returns:
    float: The quotient of a and b
    Raises:
    ValueError: If b is zero, to prevent division by zero
    '''
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b