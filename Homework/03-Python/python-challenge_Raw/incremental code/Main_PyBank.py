# First we'll import the os module. This will allow us to create file paths across operating systems
import os
import csv # Module for reading CSV files

csvpath = os.path.join('Resources-PyBank/budget_data.csv') # Path of working csv file

with open(csvpath) as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')  # CSV reader specifies delimiter and variable that holds contents

    csv_header = next(csvreader) # Read the header row first (skip this step if there is now header)
   # lines= len(list(csvreader)) # Total  number of rows.

    # VARIABLES
    total = 0
    linetotal = 0
    
    avgchange = 0
    linechange = 0
    initialvalue = 0
    
    for row in csvreader:  # Read each row of data after the header
                     
        # if row == 1:
        initialvalue = int(row[1])  # to calculate average change, store value 1st record 
        linetotal = int(row[1])     # increment a Total profit or loss, during each iteration.
        total = total + linetotal  
            
        # else:
        #     linetotal = int(row[1])     # increment a Total profit or loss, during each iteration.
        #     total = total + linetotal
        #     avgchange = initialvalue - linetotal
            
    
print("     Financial Analysis")
# print("__________________________")
print("----------------------------")
print("Total Months: " + str(lines))
print("Total: " + " $ " + str(total))
print("Average Change: " + " $ " + str(lines - 1))
  




