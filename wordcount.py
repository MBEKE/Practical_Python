#!/usr/bin/python3

def wordcount(input_string):
    # Split the string by whitespace to get individual words
    words = input_string.split()
    #Count the number of words in the list
    word_count = len(words)
    return word_count
# Example usage
input_string = "Hello, welcome  to the world of Python programming!"
print("Number of words:", wordcount(input_string))