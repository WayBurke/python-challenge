#====================================================================================================
#main.py for PyPoll
#This Python script analyzes the records to calculate each of the following values:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote
#====================================================================================================

#importing the necessary Modules
import os
import csv


#This function will be reading from csv file 'election_data.csv'
csvPyPoll = os.path.join('Resources','election_data.csv')


#Declaring the values with initial values
totalVotes = 0          #counter for total number of votes overall
winnerName =""          #variable to capture the person with the highest votes
candidate_1_count = 0   #vote counter for Charles
candidate_2_count = 0   #vote counter for Diana
candidate_3_count = 0   #vote counter for Raymon

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



#=======TERMINAL PRINTOUT=============
# PRINT OUT OF RESULTS TO TERMINAL
print(f"Election Results")
print("----------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("----------------------------\n")
print(f"Charles Casper Stockham: {round((candidate_1_count/totalVotes),5)*100}% ({candidate_1_count})\n")
print(f"Diana DeGette: {round((candidate_2_count/totalVotes),5)*100}% ({candidate_2_count})\n")
print(f"Raymon Anthony Doane: {round((candidate_3_count/totalVotes),3)*100}% ({candidate_3_count})\n")
print("----------------------------\n")
print(f"Winner: {winnerName}\n")
print("----------------------------\n")


#=======OUTPUT TO FILE PROCESS=========
#Using the print function to write to file - makes for less typing (wink, wink)

pypoll_output = os.path.join("analysis","PyPoll_Output.txt")

with open(pypoll_output, "w",newline="") as output_file:
    print(f"Election Results", file=output_file)
    print("----------------------------\n", file=output_file)
    print(f"Total Votes: {totalVotes}\n", file=output_file)
    print("----------------------------\n", file=output_file)
    print(f"Charles Casper Stockham: {round((candidate_1_count/totalVotes),5)*100}% ({candidate_1_count})\n", file=output_file)
    print(f"Diana DeGette: {round((candidate_2_count/totalVotes),5)*100}% ({candidate_2_count})\n", file=output_file)
    print(f"Raymon Anthony Doane: {round((candidate_3_count/totalVotes),3)*100}% ({candidate_3_count})\n", file=output_file)
    print("----------------------------\n", file=output_file)
    print(f"Winner: {winnerName}\n", file=output_file)
    print("----------------------------\n", file=output_file)