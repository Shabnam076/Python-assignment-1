#Write a python program that counts the occurences of a specific element in a list.
list2 = [1, 2, 6, 4, 2, 2, 15, 6, 2]


element_to_count = 2
count = 0

for element in list2:
    
    if element == element_to_count:
        count += 1

print(f"The number of occurrences of {element_to_count} in the list is: {count}")
