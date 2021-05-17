
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources-PyPoll/election_test.csv')
# output_path = os.path.join('Resources-PyBank/budget_new.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # VARIABLES

    # name = 'name'
    total_votes = 0
    
    names = []
    

    for row in csvreader:
    
    def fcandidates():
        
        if row[2] not in names:
            # if new candidate, add to candidate list
            names.append(row[2])
        else:
            pass
        return fcandidates 


    




    #-----------------------------------------------------------------------

    # print("     Election Results")
    # # print("__________________________")
    # print("----------------------------")
    # print("Total Votes: " + str(total_votes))
    # print("----------------------------")
            print(names)
