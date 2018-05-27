# -*- coding: utf-8 -*-
"""

PyBank Python Challenge
Josh Bode
May 26, 2018

"""

## Option 1: PyBank

#0. IMport modules and set paths 
import os
import csv
path = os.path.join("raw_data", "budget_data_1.csv") 

#Variables to track results
months = 0
revenue =  0
delta = 0 
totaldelta = 0 
bigincrease = 0
increase_date = "" 
bigdecrease = 0
decrease_date = ""
 
prior_rev = 0 


#Read in the data - using basic python

with open(path, "r") as csvfile:

	 #CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
    for row in csvreader:
        months = months + 1
        revenue = revenue + int(row[1])
        
        if months > 1:
           delta = int(row[1]) - prior_rev 
   
        if delta > bigincrease:
            bigincrease = delta
            increase_date = row[0]
            
        elif delta <bigdecrease:
            bigdecrease = delta
            decrease_date = row[0]
            
        prior_rev = int(row[1])
        totaldelta = totaldelta + delta
    

print("FINANCIAL ANALYSIS")
print("---------------------------------")
print(f"Total months: {months}")
print(f"Total revenue: {revenue}")    
print(f"Average revenue change: {totaldelta/(months-1)}")        
print(f"Greatest increase in revenue: {increase_date} {bigincrease})") 
print(f"Greatest decrease in revenue: {decrease_date} {bigdecrease}")
