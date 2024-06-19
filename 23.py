#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user inpu
temperature = float(input("Enter the temperature value: "))
conversion_type = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").upper()


if conversion_type == 'C':
    converted_temperature = (temperature * 9/5) + 32
    original_unit = "Celsius"
    converted_unit = "Fahrenheit"
    print(f"{temperature} {original_unit} is equal to {converted_temperature:.2f} {converted_unit}.")
elif conversion_type == 'F':
    converted_temperature = (temperature - 32) * 5/9
    original_unit = "Fahrenheit"
    converted_unit = "Celsius"
    print(f"{temperature} {original_unit} is equal to {converted_temperature:.2f} {converted_unit}.")
else:
    print("Invalid input! Please enter 'C' or 'F'.")
