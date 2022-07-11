# main.py for PyPoll


import os
import csv


#This function will be reading from a csv file
csvPyPoll = os.path.join('Resources','election_data.csv')


#Declaring the values with initial values
totalVotes = 0
winnerName =""
candidate_1_count = 0
candidate_2_count = 0
candidate_3_count = 0

with open(csvPyPoll) as PyPollcsvfile:
    PyPollcsvreader = csv.reader(PyPollcsvfile, delimiter=',')
    header = next(PyPollcsvfile, None)  # skip the header so that only the data is being analyzed
   
            
    for row in PyPollcsvreader:
        totalVotes+=1
        if row[2] =="Charles Casper Stockham":      #CONDITION TO CHECK IF CHARLES' NAME IS IN THAT ROW
            candidate_1_count += 1
        elif row[2] =="Diana DeGette":              #CONDITION TO CHECK IF DIANA'S NAME IS IN THAT ROW
            candidate_2_count += 1
        elif row[2] =="Raymon Anthony Doane":       #CONDITION TO CHECK IF RAYMON'S NAME IS IN THAT ROW
            candidate_3_count += 1
        
# WHO IS THE WINNER?? ==> COMPARING THE TOTAL NUMBER OF VOTES PER CANDIDATE
if (candidate_1_count > candidate_2_count) and (candidate_1_count > candidate_3_count):
    winnerName = "Charles Casper Stockham"
elif (candidate_2_count > candidate_1_count) and (candidate_2_count > candidate_3_count):
    winnerName = "Diana DeGette"
else:
    winnerName = "Raymon Anthony Doane"



#OUTPUT FILE INFO
pypoll_output = os.path.join("Resources","PyPoll_Output.txt")

with open(pypoll_output, "w", newline ="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])

# PRINT OUT OF RESULTS TO TERMINAL

print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {totalVotes}")
print("----------------------------")
print(f"Charles Casper Stockham: {round((candidate_1_count/totalVotes),5)*100}% ({candidate_1_count})")
print(f"Diana DeGette: {round((candidate_2_count/totalVotes),5)*100}% ({candidate_2_count})")
print(f"Raymon Anthony Doane: {round((candidate_3_count/totalVotes),3)*100}% ({candidate_3_count})")
print("----------------------------")
print(f"Winner: {winnerName}")
print("----------------------------")