#Import libraries to use
import csv
import pathlib
import os

#Set path for finding csv file

csv_path = pathlib.Path('Resources/budget_data.csv')

#Create lists to store the data
profit_loss = []
date_combined = []
month = []
year = []

#Open csv file and read
with open(csv_path) as csv_file:
    csv_data = csv.reader(csv_file)
    
    #Read Header row and id
    csv_header=next(csv_data)
    # print(csv_header)
    
    for x in csv_data:
        print(x=2)
