#!/usr/bin/python3

def convert_to_data_type(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
           result = func(*args, **kwargs)
           return data_type(result)
        return wrapper
    return decorator

@convert_to_data_type(int)
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 20)
print("Result:", type(result))

@convert_to_data_type(str)
def concatenate_strings(x, y):
    return x + y

result = concatenate_strings("Python", "Decorator")
print("Result:", result, type(result))
