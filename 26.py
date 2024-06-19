#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

input_string = "Hello, Guys!!"
prefix = "Hello"
suffix = "Guys!!"


if input_string[:len(prefix)] == prefix:
    print(f"The string '{input_string}' starts with the prefix '{prefix}'")
else:
    print(f"The string '{input_string}' does not start with the prefix '{prefix}'")


if input_string[-len(suffix):] == suffix:
    print(f"The string '{input_string}' ends with the suffix '{suffix}'")
else:
    print(f"The string '{input_string}' does not end with the suffix '{suffix}'")
