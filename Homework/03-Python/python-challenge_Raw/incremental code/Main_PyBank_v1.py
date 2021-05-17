# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyBank/budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    num_rows = 0
    
    total = 0
    linetotal = 0
    
    avgchange = 0
    linechange = 0
    counterchange = 0
    currentline = 0
    nextline= 0
    # # Read each row of data after the header

    for row in csvreader:
        # counter. increment a counter, num_rows, during each iteration.
        num_rows += 1
        # increment a Total profit or loss, during each iteration.
        linetotal = int(row[1])
        total = total + linetotal
    
    print("     Financial Analysis")
    # print("__________________________")
    print("----------------------------")
    print("Total Months: " + str(num_rows))
    print("Total: " + " $ " + str(total))
    print("Average Change: " + " $ " + str(total))
  




