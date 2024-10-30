#!/usr/bin/python3

def find_vowel(mystr):
    vowels = "aeiou"
    count = 0
    for x in mystr:
        if x.lower() in vowels: count += 1
    
    print(f"Number of Vowels: {count}")
find_vowel("I am a Python Backend Engineer")