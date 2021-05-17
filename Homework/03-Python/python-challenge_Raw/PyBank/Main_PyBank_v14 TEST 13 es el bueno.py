# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyBank/budget_data.csv')
# output_path = os.path.join('Resources-PyBank/budget_new.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # VARIABLES

    delta = 0
    current_line = 0
    prev_line = 0
    maxincrease = 0
    maxdecrease = 0
    max_month = ''
    min_month =''
    month = ''
    
    for row in csvreader: # Read each row of data after the header

       
        # antes de cargar el valor de la linea, lo resto porque es el valor anterior menos el de ahora al cambiar la linea
        if (row == 0):
            current_line = int(row[1])
            prev_line = int(row[1])
            month =  str(row[0])
            delta = current_line

        else:
            current_line = int(row[1])
            month =  str(row[0])
            delta = current_line - prev_line
            prev_line = int(row[1])

            if (delta > maxincrease):
                maxincrease = delta
                max_month = month
            elif (delta < maxdecrease):
                maxdecrease = delta
                min_month = month


              
     # comparo el incremento o decremento actual con el valor maximo o minimo previamente guardado en la variable

    
def sum_months(): # function to calculate total number of votes
    
    total_months = 0 # initialize variable total_months    

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)
        
        for row in csvreader: # iteration of rows in cvs file

                total_months = total_months + 1 # Add 1 to total votes
           
    return total_months

def sum_amount(): # function to calculate total number of votes

    total_amount = 0 # initialize variable total
    linetotal = 0    # initialize variable linetotal 

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)
        
        for row in csvreader: # iteration of rows in cvs file
        #   linetotal = int(row[1]) 
            total_amount = total_amount + int(row[1])
        
    return total_amount

def avg_change(): # function to calculate total number of votes

    mean_delta = 0
    initialvalue = 0
    lastvalue = 0    # initialize variable linetotal 

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)

        for row in csvreader: # Read each row of data after the header
            
            if initialvalue == 0:
                initialvalue = int(row[1])
            else:
                lastvalue = int(row[1])
        
        mean_delta = round(((lastvalue - initialvalue) / (total_months - 1)), 2)

    return mean_delta
     

# run functions 
total_months = sum_months()
total_amount = sum_amount()
mean_delta = avg_change()


print(" ")
print(" ")
print("     Financial Analysis")
# print("__________________________")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + " $ " + str(total_amount))
# print("Average Change: " + " $ " + str(round(avgchange, 2))
print("Average Change: " + " $ " + str(mean_delta))
print("Greatest Increase in Profits: " + str(max_month) + "  (" + "$" + str(maxincrease) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + "  (" + "$" + str(maxdecrease) + ")")


#Begin write new csv
output_path = os.path.join('Resources-PyBank/budget_new.txt')
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis']),
    csvwriter.writerow(["Total Months", str(total_months)])
    csvwriter.writerow(["Total", str(total_amount)])
    csvwriter.writerow(["Average Change" , str(mean_delta)])
    csvwriter.writerow(["Greatest Increase in Profits", str(maxincrease)])
    csvwriter.writerow(["Greatest Decrease in Profits", str(maxdecrease)])
