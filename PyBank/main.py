#====================================================================================================
#main.py for PyBank
#This Python script analyzes the records to calculate each of the following values:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period
#====================================================================================================

#importing the necessary Modules
import os
import csv


#This function will be reading from csv file 'budget_data.csv'
csvpath = os.path.join('Resources','budget_data.csv')


#Declaring and initializing values
totalMonth = 0  #row counter to determine number of rows, starting at 0 since the header will be skipped
totalPL = 0
averageChange =0
profit = 0
loss = 0

csvList =[]         #CREATE A LIST TO TRACK THE ROWS OF THE TABLE


with open(csvpath) as budgetcsvfile:
    csvreader = csv.reader(budgetcsvfile, delimiter=',')
    header=next(csvreader, None)  #--> skip the header so that only the data is being analyzed
   
            
    for row in csvreader:
        
        totalMonth += 1         #increasing the row counter
        totalPL += int(row[1])  #incrementing the totalPL with the next row of data
        
        #ADDING A NEW ROW TO THE LIST TO TRACK THE ROWS OF THE TABLE
        csvList.append(row)     #--> adding the next line of the CSV file to the List
        
       
        finalEntryValue = int(row[1]) # this variable will contain the value of the last row at the end of the for loop

#--> calculation of Average Change using 1st and last value from table
averageChange = round((finalEntryValue-int(csvList[0][1]))/(totalMonth-1),2) 


# New varibale to store the months associated the the greatest increase and greatest decrease respectively
profitMth =""
lossMth =""

previousValue = int(csvList[1][1]) - int(csvList[0][1])  # setting previous value to the first item in the list


for entry in range(len(csvList)):       #Traversing through the list compare previous value vs new value
    newvalue= int(csvList[entry][1]) - int(csvList[entry - 1][1])

    
    #CHECK FOR GREATEST INCREASE - PROFIT
    #Checking newvalue, previousValue and profit to ensure that the highest is being captured
    #Also updating to the Month of the highest at the time
    if (newvalue > previousValue) and (newvalue>profit):
        profit = newvalue
        profitMth= csvList[entry][0]
        
    elif (previousValue >newvalue) and (previousValue > profit):
        profit = previousValue
        profitMth= csvList[entry-1][0]
        
    
    #CHECK FOR GREATEST DECREASE - LOSS
    #Checking newvalue, previousValue and loss to ensure that the lowest is being captured
    #Also updating to the Month of the lowest at the time
    if (newvalue < previousValue) and (newvalue< loss):
        loss = newvalue
        lossMth = csvList[entry][0]
    elif (previousValue <newvalue) and (previousValue <loss):
        loss = previousValue
        lossMth = csvList[entry -1][0]

    previousValue = newvalue        #Assigning Previous value to new value for the next iteration

#=======TERMINAL PRINTOUT=============
#Print out of the values calculated
print("Financial Analysis")
print("----------------------------\n")
print(f"Total Months: {totalMonth}\n")
print(f"Total: ${totalPL}\n")
print(f"Average Change: $ {str(averageChange)}\n")  
print(f"Greatest Increase in Profits: {profitMth} (${profit})\n")    
print(f"Greatest Decrease in Profits: {lossMth} (${loss})\n")      


#=======OUTPUT TO FILE PROCESS=========
#Using the print function to write to file - makes for less typing (wink)
pybank_output = os.path.join("analysis","PyBank_Output.txt")

with open(pybank_output, "w", newline="") as output_file:
    #Print out of the values calculated
    print("Financial Analysis", file=output_file)
    print ("----------------------------\n", file=output_file)
    print(f"Total Months: {totalMonth}\n", file=output_file)
    print(f"Total: ${totalPL}\n", file=output_file)
    print(f"Average Change: $ {str(averageChange)}\n", file=output_file)
    print(f"Greatest Increase in Profits: {profitMth} (${profit})\n", file=output_file)    
    print(f"Greatest Decrease in Profits: {lossMth} (${loss})\n", file=output_file)     
