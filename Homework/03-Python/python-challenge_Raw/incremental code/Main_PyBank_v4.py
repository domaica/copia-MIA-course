# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyBank/budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # VARIABLES

    num_rows = 0
    
    total = 0
    linetotal = 0
    
    avgchange = 0.00
    linechange = 0
    counterchange = 0
    initialvalue = 0
    totaldif= 0

    delta = 0
    currdelta = 0
    maxincrease = 0
    maxdecrease = 0
    
    
    for row in csvreader: # Read each row of data after the header

        num_rows += 1 # counter. increment a counter, num_rows, during each iteration.

        linetotal = int(row[1])
        total = total + linetotal

        totaldif = linetotal - initialvalue

        if num_rows == 1:
            linetotal = int(row[1])
            initialvalue = linetotal
            total = initialvalue

            continue
       
        
            #---------------------------------------------------------------
        counterchange = num_rows - 1
        totaldif = linetotal - initialvalue
        avgchange =  totaldif / counterchange
        avgchange = str(round(avgchange, 2))

    print("     Financial Analysis")
    # print("__________________________")
    print("----------------------------")
    print("Total Months: " + str(num_rows))
    print("Total: " + " $ " + str(total))
    # print("Average Change: " + " $ " + str(round(avgchange, 2))
    print("Average Change: " + " $ " + str(avgchange))
    print("Greatest Increase in Profits: " + " $ " + str(maxincrease))
    print("Greatest Decrease in Profits: " + " $ " + str(maxdecrease))



