# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyBank/budget_data.csv') # Relative path to read .csv file

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # VARIABLES

    delta = 0           # Var to calculate difference btw 2 amounts in consecutive rows
    current_line = 0    # Var containing current line amount
    prev_line = 0       # Var containing previous line amount
    maxincrease = 0     # Var to store greatest increase
    maxdecrease = 0     # Var to store greatest decrease
    max_month = ''      # Var to store month of greatest increase
    min_month =''       # Var to store month of greatest decrease
    month = ''          # Var to current row month
    
    for row in csvreader: # Read each row of data after the header
    
        # initial row values
        if (row == 0):
            current_line = int(row[1])  # Value of current row amount
            prev_line = int(row[1])     # store current row amount to operate in next row
            month =  str(row[0])        # store month of current line
            delta = current_line        # delta is = current row amount,
                                        # because there is not previous amount

        # Comparing current increase or decrease with 
        # the maximum or minimum values previously saved in variables
        else:
            current_line = int(row[1])          # Value of current row amount
            month =  str(row[0])                # store month of current line
            delta = current_line - prev_line    # delta is = current row amount - previous one
            prev_line = int(row[1])             # store current row amount to operate in next row

            if (delta > maxincrease):           # if current delta greater than stored previously
                maxincrease = delta             # Greatest increase is now the current delta
                max_month = month               # store greatest increase month 

            elif (delta < maxdecrease):         # if current delta smaller than stored previously
                maxdecrease = delta             # Greatest decrease is now the current delta
                min_month = month               # store greatest decrease month 


# function to calculate total number of months
def sum_months(): 
    
    total_months = 0 # initialize variable total_months    

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)
        
        for row in csvreader: # iteration of rows in cvs file

                total_months = total_months + 1 # Add 1 to total months
           
    return total_months

def sum_amount(): # function to calculate total net amount of profit/losses
    total_amount = 0 # initialize variable total
   
    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)
        
        for row in csvreader: # iteration of rows in cvs file
      
            total_amount = total_amount + int(row[1])
        
    return total_amount

def avg_change(): # function to average change

    mean_delta = 0      # average of changes, of deltas 
    initialvalue = 0    # 1st amount of the serie
    lastvalue = 0       # last amount of the serie

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)

        for row in csvreader: # Read each row of data after the header
            # initial row values
            if (initialvalue == 0):
                initialvalue = int(row[1])  # store initial amount in variable
            else:
                lastvalue = int(row[1])     # store final amount in variable
        # average = last amount - initial amount divided by number of months except 1st line
        # change format to number rounded to 2 decimals
        mean_delta = round(((lastvalue - initialvalue) / (total_months - 1)), 2)

    return mean_delta
     

# run functions 
total_months = sum_months()
total_amount = sum_amount()
mean_delta = avg_change()


#--------------------------
# PRINT results
#--------------------------
# Skip 2 lines just cosmetic, 1st line was too close in terminal to top
print(" ")
print(" ")

print("     Financial Analysis")
# print("__________________________")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + " $ " + str(total_amount))
print("Average Change: " + " $ " + str(mean_delta))
print("Greatest Increase in Profits: " + str(max_month) + "  (" + "$" + str(maxincrease) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + "  (" + "$" + str(maxdecrease) + ")")

#--------------------------
# WRITE results to new .txt
#--------------------------
# Path to write new file, Analisis folder
output_path = os.path.join('Analysis-PyBank/budget_new.txt')
# newline parameter important to avoid skip lines in csv or txt
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------'])
    csvwriter.writerow(["Total Months", str(total_months)])
    csvwriter.writerow(["Total", str(total_amount)])
    csvwriter.writerow(["Average Change" , str(mean_delta)])
    csvwriter.writerow(["Greatest Increase in Profits", str(maxincrease)])
    csvwriter.writerow(["Greatest Decrease in Profits", str(maxdecrease)])
