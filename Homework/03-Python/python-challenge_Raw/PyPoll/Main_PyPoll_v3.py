# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyPoll/election_test.csv')
# output_path = os.path.join('Resources-PyBank/budget_new.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

 
   

def total_votes():

    total_votes = 0
    
    for row in csvreader:
    # print(row)
    #    linevotes = linevotes + 1
        total_votes = total_votes + 1
    
    return total_votes
  
  #def total_votes():  

     numvotes = 0
    
    for row in csvreader: # Read each row of data after the header
    
    # def fcandidates():
        
    #     if row[2] not in names:
    #         # if new candidate, add to candidate list
    #         names.append(row[2])
    #     else:
    #         pass
    #     return fcandidates 

    #     #return fcandidates 


    




    #-----------------------------------------------------------------------

    # print("     Election Results")
    # # print("__________________________")
    # print("----------------------------")
    # print("Total Votes: " + str(total_votes))
    # print("----------------------------")
    print(total_votes)
