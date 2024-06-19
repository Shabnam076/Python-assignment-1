"""Write a program that reads data from a CSV file and prints it to the 
console. """
import csv

# Function to read and print CSV file
def read_and_print_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the CSV file
csv_file_path = 'data.csv'

# Call the function to read and print the CSV file
read_and_print_csv(csv_file_path)