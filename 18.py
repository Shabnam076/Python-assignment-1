""" Write a python program that converts a given string to uppercase"""
def to_uppercase(input_string):
    uppercase_string = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            # Convert to uppercase by adjusting the ASCII value
            uppercase_char = chr(ord(char) - 32)
        else:
            # If it's not a lowercase letter, keep it as is
            uppercase_char = char
        uppercase_string += uppercase_char
    return uppercase_string

input_str = "Hello! This is a test."
result = to_uppercase(input_str)
print("Original String:", input_str)
print("Uppercase String:", result)
