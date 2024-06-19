"""Write a program that reads data from a CSV file and prints it to the 
console. """
import csv

#specify the file name
filename = 'myfile.csv'

#open the csv file
with open(filename, mode='r') as file:
    #create a csv reader object
    csv_reader = csv.reader(file)

    #iterate through the rows and print each row
    for row in csv_reader:
        print(row)