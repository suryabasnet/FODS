#To read a given CSV file as a list.
import csv
with open('cities.csv', 'r') as file:
    data_file = csv.reader(file)
    for row in data_file:
        print(row)