#====================================================================================================
#main.py for PyBank
#Your task is to create a Python script that analyzes the records to calculate each of the following
#values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#====================================================================================================


import os
import csv


#This function will be reading from a csv file
csvpath = os.path.join('Resources','budget_data.csv')


#Declaring the values with initial values
totalMonth = 0  #row counter to determine number of rows
totalPL = 0
averageChange =0
profit = 0
loss = 0


with open(csvpath) as budgetcsvfile:
    csvreader = csv.reader(budgetcsvfile, delimiter=',')
    next(csvreader, None)  # skip the header so that only the data is being analyzed
   
            
    for row in csvreader:
        
        totalMonth = totalMonth + 1     #increasing the row counter
        totalPL = totalPL + int(row[1])
        
       
        if int(row[1]) < 0:
            loss = loss + int(row[1])
        elif int(row[1]) >= 0:
            profit = profit + int(row[1])

    

averageChange = round(totalPL/totalMonth,3)

#Print out of the values calculated
print ("_____________________")
print("Financial Analysis")
print ("---------------------")
print(f"Total Months: {totalMonth}")
print(f"Total: $ {totalPL}")
print("Average Change: " + str(averageChange))      # CURRENT CALCULATION IS INCORRECT, should be the average of the difference btw 2
print(f"Greatest Increase in Profits: {profit}")    # CURRENT CALCULATION IS INCORRECT, should be the highest value in the diference btw 2
print(f"Greatest Decrease in Profits: {loss}")      # CURRENT CALCULATION IS INCORRECT, should be the lowest value in the diference btw 2