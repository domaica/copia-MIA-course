import os
import csv

csvpath = os.path.join('Resources-PyPoll/election_test.csv')
# # output_path = os.path.join('Resources-PyBank/budget_new.csv')


with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#     # # # Read the header row first (skip this step if there is now header)
#    csv_header = next(csvreader)
  

# countvotes() returns total number of votes, skipping headers
  
def countvotes():
    # initialize vote counter
    counter = 0    

    with open(csvpath) as csvfile:

    #     # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        
        for row in csvreader:

            if row[0] == 'Voter ID':
                pass
                    # if not a header row, increment single file row counter
            else:
                counter = counter + 1
           
    return counter

# listcand() returns a list of unique candidates

def listcand():
    # create list to hold unique candidates
    candidates = []
    # iterate over .csv files
    with open(csvpath) as csvfile:

    #     # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:
            
            # skip header row
            if row[0] == 'Voter ID':
                pass
            else:
                # check to see if current candidate is in list
                if row[2] not in candidates:
                    # if new candidate, add to candidate list
                    candidates.append(row[2])
                else:
                    pass
    return candidates 

# tallyvotes() returns a dictionary: {"Candidate":[percentage, votes]}

def tallyvotes():
    # initialize dictionary
    candidatedict = {}
    # iterate over list of unique candidates
    for candidate in candidates:
        # initialize list of 2 integers for each candidate key
        candidatedict[candidate] = [0,0]

    with open(csvpath) as csvfile:

    #     # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')    

        # iterate over poll files
        for row in csvreader:
            # skip header row
            if row[0] == 'Voter ID':
                pass
            else:
                # iterate over initialized candidate dictionary
                for key, value in candidatedict.items():
                    # when candidate dictionary key matches voter candidate
                    if key == row[2]:
                        # increment vote value (2nd element in dict value list)
                        value[1] = value[1] + 1
                        # update percent votes for candidate in dict
                        value[0] = round(((value[1] / counter) * 100), 3)
                    else:
                        pass
    return candidatedict

# findwinner() returns key (candidate name string) of highest vote count value               

def findwinner():
    # initialize comparison value
    topdog = 0
    # iterate over each unique candidate in dict
    for key, value in candidatedict.items():
        # if largest vote count so far, store as top vote count
        if value[1] > topdog:
            topdog = value[1]
            # store corresponding candidate name
            winner = key
        else:
            pass
    return winner

# run above functions in sequence
counter = countvotes()
candidates = listcand()
candidatedict = tallyvotes()
winner = findwinner()

# PRINTING
print('')
print('')
print('        Election Results')
print('----------------------------------')
print('Total Votes:', counter)
print('----------------------------------')

# print contents of candidate dictionary with % formatting
for key, value in candidatedict.items():
    print(key + ':', str(value[0]) + '%  (' + str(value[1]) + ')')

print('----------------------------------')
print('Winner: ', winner)
print('----------------------------------')

# WRITING new txt file in Resources-PyPoll folder

# def printtofile():
output_path = os.path.join('Resources-PyPoll/election_newfile.txt')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(["Total Votes", str(counter)])
    csvwriter.writerow(['----------------------------------'])
    for key, value in candidatedict.items():
        csvwriter.writerow([key, str(value[0]) + '%', '(' + str(value[1]) + ')'])

    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(['Winner', winner])
    csvwriter.writerow(['----------------------------------'])







