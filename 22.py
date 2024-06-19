#Write a python program that returns the minimum and maximum values in a list of numbers.

list3 = [5, 11, 9, 1, 17, 8, 6]


min_value = list3[0]
max_value = list3[0]


for num in list3:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num


print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
