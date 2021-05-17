import os
import csv

# relative path for getting the .csv file needed to do exercise
csvpath = os.path.join('Resources-PyPoll/election_data.csv')
# BELOW is a file containing a subset used to do tests with 100 records
# csvpath = os.path.join('Resources-PyPoll/election_test.csv')
# # output_path = os.path.join('Resources-PyBank/election_newfile.txt')


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

def sum_votes(): # function to calculate total number of votes
    
    total_votes = 0 # initialize variable total_votes    

    with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)
        
        for row in csvreader: # iteration of rows in cvs file

                total_votes = total_votes + 1 # Add 1 to total votes
           
    return total_votes

def competitor_list(): # function to detect and append name of different politicians
   
    names = [] # create list to append different names
   
    with open(csvpath) as csvfile: # iterate over .csv files

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)

        for row in csvreader: # iteration of rows in cvs file
                # check to see if current name is in list
                if row[2] not in names:
                    # if new name, add to name list
                    names.append(row[2])
                else:
                    pass
    return names

# votepercentage() returns a dictionary: {"name":[percentage, votes]}

def votepercentage():
    
    dictionarynames = {} # create dictionary
    # iterate over list of unique names
    for name in names:
        # add name of previous function as key and 2 values to keep votes and percentages
        dictionarynames[name] = [0,0] 

    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip header row 
        csv_header = next(csvreader)

        for row in csvreader: # iteration of rows in cvs file

                for key, value in dictionarynames.items(): 
                    # when name dictionary key is equal to csv record in current reading
                    if key == row[2]:
                        # increment vote counter in dictionary (2nd field, index 1 after %)
                        value[1] = value[1] + 1
                        # calculate percent votes for name in dict (1st field after name key)
                        # change integer to round and 3 decimals
                        value[0] = round(((value[1] / total_votes) * 100),3)
                    else:
                        pass
    return dictionarynames

             

def election_winner(): # winner() is a function to get the name of most voted candidate 
    
    mostvoted = 0 # declare variable & initialize
    
    # iterate names in dict
    for key, value in dictionarynames.items():
        # if sum of votes contained in field is bigger than current mostvoted variable content
        if value[1] > mostvoted:
            mostvoted = value[1] # then new mostvoted variable is the one on top
            # store corresponding name name
            winner = key # value of winner is the name (key) of dict
        else:
            pass # otherwise go to read next dict entry in the loop
    return winner

# run functions 
total_votes = sum_votes()
names = competitor_list()
dictionarynames = votepercentage()
winner = election_winner()

# PRINTING
print('')
print('')
print('    Election Results')
print('-------------------------')
print('Total Votes:', total_votes)
print('-------------------------')

# print contents of name dictionary 
for key, value in dictionarynames.items():
    print(key + ':', str(value[0]) + '%  (' + str(value[1]) + ')')

print('-------------------------')
print('Winner: ', winner)
print('-------------------------')

# WRITING new txt file in Resources-PyPoll folder

output_path = os.path.join('Resources-PyPoll/election_newfile.txt')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(["Total Votes", str(total_votes)])
    csvwriter.writerow(['-------------------------'])
    for key, value in dictionarynames.items():
        csvwriter.writerow([key, str(value[0]) + '%', '(' + str(value[1]) + ')'])

    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner', winner])
    csvwriter.writerow(['-------------------------'])







