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


from operator import ne
import os
import csv


#This function will be reading from a csv file
csvpath = os.path.join('Resources','budget_data.csv')


#Declaring the values with initial values
totalMonth = 0  #row counter to determine number of rows, starting at 1 since first line is
totalPL = 0
StartValue = 0
EndValue = 0
averageChange =0
profit = 0
loss = 0

csvList =[]         #CREATE A LIST TO TRACK THE ROWS OF THE TABLE


with open(csvpath) as budgetcsvfile:
    csvreader = csv.reader(budgetcsvfile, delimiter=',')
    next(csvreader, None)  # skip the header so that only the data is being analyzed
   
            
    for row in csvreader:
        
        totalMonth = totalMonth + 1     #increasing the row counter
        totalPL = totalPL + int(row[1])
        
        #ADDING A NEW ROW TO THE LIST TO TRACK THE ROWS OF THE TABLE
        csvList.append(row)     # adding the next line of the CSV file to the List
        
       
        averageTotal = int(row[1])

   
averageChange = round((averageTotal-int(csvList[0][1]))/(totalMonth-1),2) #-->UNDER CONSTRUCTION


#create new list
# use this new list to store the difference
profitMth =""
lossMth =""
previousValue = int(csvList[1][1]) - int(csvList[0][1])  # setting previous value to the first item in the list


for entry in range(len(csvList)):
    newvalue= int(csvList[entry][1]) - int(csvList[entry - 1][1])

    
    #CHECK FOR GREATEST INCREASE - PROFIT
    if (newvalue > previousValue) and (newvalue>profit):
        profit = newvalue
        profitMth= csvList[entry][0]
        #loss = previousValue
    elif (previousValue >newvalue) and (previousValue > profit):
        profit = previousValue
        profitMth= csvList[entry-1][0]
        #loss = newvalue

    
    #CHECK FOR GREATEST DECREASE - LOSS
    if (newvalue < previousValue) and (newvalue< loss):
        loss = newvalue
        lossMth = csvList[entry][0]
    elif (previousValue <newvalue) and (previousValue <loss):
        loss = previousValue
        lossMth = csvList[entry -1][0]

    previousValue = newvalue


#Print out of the values calculated
print ("_____________________")
print("Financial Analysis")
print ("---------------------")
print(f"Total Months: {totalMonth}")
print(f"Total: ${totalPL}")
print(f"Average Change: $ {str(averageChange)}")  
print(f"Greatest Increase in Profits: {profitMth} (${profit})")    
print(f"Greatest Decrease in Profits: {lossMth} (${loss})")      
