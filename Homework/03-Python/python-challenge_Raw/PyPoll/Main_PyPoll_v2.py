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

    # VARIABLES

    name = 'name'
    total_votes = 0
    
    # candidates = []
    
    
    candidate_percent = 0
    

    for row in csvreader:
        # print(row)
    #    linevotes = linevotes + 1
        total_votes = total_votes + 1

    for row in csvreader:
        # candidates = []
                # skip header row
                # if row[0] == 'Voter ID':
                #     pass
                # else:
                    # check to see if current candidate is in list
        if row[2] not in candidates:
            # if new candidate, add to candidate list
            candidates.append(row[2])
        else:
            pass
    # return candidates 


    




    #-----------------------------------------------------------------------

    print("     Election Results")
    # print("__________________________")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
    print(candidates)
