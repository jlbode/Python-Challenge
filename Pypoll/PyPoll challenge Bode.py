# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:11:24 2018
@author: bodej
Python Challenge - PyPoll

"""


#0. Import modules and set paths 
import os
import csv
path = os.path.join("raw_data", "election_data_2.csv") 
resultspath = os.path.join("raw_data", "election_results_1.csv")

#Variables to track results
totalvotes  = 0
candidates = []
votes = []


#1. Read in the data and tally votes - using basic python

with open(path, "r") as csvfile:

	 #CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
    for row in csvreader:
        totalvotes = totalvotes + 1
        
        #If candidate is not in our list add them in
        if row[2] not in candidates:
             candidates.append(row[2]) 
             votes.append(0)
        
        #Add to the tally if the candidate matches
        index = 0
        for candidate in candidates:
            if row[2] == candidate:
                votes[index] = votes[index] + 1 
            index = index +1

#2. Calculate % of total for each candidates
pct_votes = []
index = 0
for candidate in candidates:  
    pct_votes.append(round(votes[index]/totalvotes*100,2))       
    index = index + 1    
            
#3. Combine lists of candidates, percentages, and votes
voting_data = zip(candidates, pct_votes, votes)         

#4. Identify the winner
index = 0
for candidate in candidates:
    if votes[index] == max(votes) :
       winner = candidate
       
    index = index + 1


#5. Export the results to a CSV file
with open(resultspath, "w", newline = "") as csvfile:    
    #initialize the csv.writer
    csvwriter = csv.writer(csvfile)

    #Write the first row headers 
    csvwriter.writerow(["Candidate", "% of Votes", "Votes"])
    
    #Write the data (not working)
    csvwriter.writerows(voting_data)
    
      
#5. PRINT RESULTS
voting_data = zip(candidates, pct_votes, votes)      
print("ELECTION RESULTS")
print("---------------------------------")
print(f"Total Votes: {totalvotes}")
print("---------------------------------")
for candidates, pct_votes, votes in voting_data:
    print(f"{candidates}: {pct_votes}% ({votes})")
print("---------------------------------")
print(f"The winner is {winner}")
print("---------------------------------")