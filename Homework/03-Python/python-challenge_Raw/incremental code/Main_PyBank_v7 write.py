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

    num_rows = 0
    linetotal = 0
    total = 0
    
    avgchange = 0.00

    initialvalue = 0
    totaldif= 0

    delta = 0
    currdelta = 0
    maxincrease = 0
    maxdecrease = 0
    
    
    for row in csvreader: # Read each row of data after the header

        num_rows += 1 # counter. increment a counter, num_rows, during each iteration.

        currdelta = linetotal - int(row[1]) # antes de cargar el valor de la linea, lo resto porque es el valor anterior menos el de ahora al cambiar la linea
        linetotal = int(row[1]) 
        total = total + linetotal
        
     # comparo el incremento o decremento actual con el valor maximo o minimo previamente guardado en la variable

        if (currdelta > maxincrease):
            maxincrease = currdelta
        elif (currdelta < maxdecrease):
            maxdecrease = currdelta
     
     # en la primera linea cargo el valor inicial para guardarlo y calcular al final la diferencia total
        if num_rows == 1:
            linetotal = int(row[1])
            initialvalue = linetotal
            total = total + linetotal
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


# Begin write new csv
output_path = os.path.join('Resources-PyBank/budget_new.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["Total Months: " + str(num_rows)])
    csvwriter.writerow(["Total: " + " $ " + str(total)])
    csvwriter.writerow(["Average Change: " + " $ " + str(avgchange)])
    csvwriter.writerow(["Greatest Increase in Profits: " + " $ " + str(maxincrease)])
    csvwriter.writerow(["Greatest Decrease in Profits: " + " $ " + str(maxdecrease)])



