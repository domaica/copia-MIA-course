import os
import csv

cereal_csv = os.path.join('Resources/cereal.csv')

with open(cereal_csv) as csvfile:
       # next(csvreader, None)
        csvreader = csv.reader(csvfile, delimiter = ',')
        print(csvreader)
