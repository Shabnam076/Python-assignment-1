"""Write a python program that removes all punctuation from a given string. """
import string

input_string = "Hello, world! This is a test."

punctuation_chars = string.punctuation


result_string = ""

for char in input_string:
    
    if char not in punctuation_chars:
        result_string += char

print("Original String:", input_string)
print("String without punctuation:", result_string)
