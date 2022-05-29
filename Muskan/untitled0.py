


import csv
import pandas as pd
import random
New=[]
with open('movieR.csv','r') as csvfile:
    readCSV = csv.reader(csvfile)
    New.append(random.choice(list(readCSV)))
print(New[0][0])
        
        