# In this assignment, you will create a Python script that analyzes the financial records of your company.  Inside your starter code, you will find a financial dataset in the budget_data.csv file. This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:


import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Open the csv
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = 0
greatest_decrease_date = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    next(csvreader)
    rowcount = 0 # total number of rows/months in the dataset
    net_PL = 0 # 
    change_m2m = []
    currentrow = 0
    
    data = list(csvreader)
    lastrow = int(data[0][1])
    for row in data:
        # rowcount += 1
        net_PL += int(row[1])
        
        
        # if rowcount != 0:
        #     change_m2m.append(int(lastrow) + int(row[1]))
        #     print(f"{int(lastrow)} + {int(row[1])} = ")
        #     print(int(lastrow) + int(row[1]))
        #     lastrow = row[1]        
        rowcount += 1
        
       
    for row in data[1:]:
       
        change = int(row[1]) - lastrow
        change_m2m.append(change)
        lastrow = int(row[1])
        
avg_change = sum(change_m2m) / len(change_m2m)
print(change_m2m)
print(max(change_m2m))

greatest_increase = max(change_m2m)
greatest_decrease = min(change_m2m)
max_index = change_m2m.index(greatest_increase)
min_index = change_m2m.index(greatest_decrease)
print(max_index)
greatest_increase_date = data[max_index + 1][0]
greatest_decrease_date = data[min_index + 1][0]
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: ${net_PL}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})")

# print(change_m2m)
# change_m2m_len = len(change_m2m)
# print(change_m2m_len)

# The net total amount of Profit/Losses over the entire period

# The average of the changes in Profit/Losses over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# Your resulting analysis should look similar to the following:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Your final script should print the analysis to the terminal and export a text file with the results.