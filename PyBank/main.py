# Import os and csv libraries

import os
import csv

# Set the path to the csv data file

csvpath = os.path.join("Resources", "budget_data.csv")

# Initializing variables for analysis output

greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = 0
greatest_decrease_date = 0

# Open the csv as `csvfile` and read the contents into 'csvreader'

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    next(csvreader) # Function to advance the iterator to remove table header from loops
    rowcount = 0 # Variable to determine total number of rows/months in the dataset
    net_PL = 0 # Variable to store the total of P/L
    change_m2m = [] # List to capture month to month change for average change calculation
    data = list(csvreader) # Creating list 'data' from 'csvreader'
    last_row = int(data[0][1]) # Assign first row P/L amount to 'last_row' for first change calculation

# For loop to iterate through 'data', calculate net P/L, and count rows(months) 

    for row in data:
        net_PL += int(row[1])    
        rowcount += 1

# For loop to calculate month to month P/L changes and append to 'change_m2m' list for average P&L calculation      

    for row in data[1:]:
        change = int(row[1]) - last_row
        change_m2m.append(change)
        last_row = int(row[1])

# Calculate average change in P/L from month to month

avg_change = sum(change_m2m) / len(change_m2m)

# Locate greatest P/L increase and decrease in 'change_m2m' list and assign to analysis variables

greatest_increase = max(change_m2m)
greatest_decrease = min(change_m2m)

# Gather index from 'change_m2m' list for greatest increase and decrease dates

max_index = change_m2m.index(greatest_increase)
min_index = change_m2m.index(greatest_decrease)

# Offset row index by "+1" to correct for greatest increase and decrease dates

greatest_increase_date = data[max_index + 1][0]
greatest_decrease_date = data[min_index + 1][0]

# Print analysis to terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: ${net_PL}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Create the output text file for the results

output_path = os.path.join("Resources", "results.txt")

# Open 'results.txt' file and store the analysis results

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {rowcount}\n")
    file.write(f"Total: ${net_PL}\n")
    file.write(f"Average Change: ${round(avg_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print output text file path and file name to the terminal to notify user    

print(f"The analysis results have been stored as '{output_path}'.")
