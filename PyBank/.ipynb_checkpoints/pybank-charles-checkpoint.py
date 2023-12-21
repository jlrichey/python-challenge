# 
# opening csv files in python
# basic algo - sum, count, min, max
# do not use sum, len, min, max functions for this assignment
# for loops
# if statements
from pathlib import Path
import csv # csv.reader and csv.writer

# list1 = [10,20,304,50]
# how do you find the size of htis list
# algorithm a list of instructions to help me solve this problem
list1 = [1,2,3,4,5,6]
# print(sum(list1))

# reading and writing csv files
# WHERE THE FILE IS?
# file path, full path, relative path
# full path
# . <= this folder
# .. <= parent folder
#full_path = "/Users/jrichey/Desktop/1_BOOTCAMP/bootcamp_homework/PyBank/Resources/budget_data.csv"
relative_path = Path("./PyBank/Resources/budget_data.csv")

# read or write the file,m "r", "w"

#with context manager
# with open(relative_path, "r") as file:
#     file_reader = csv.reader(file)
#     for row in file_reader:
#         print(row)
# print('hello')
# for loops
# iterabnle: list, dict, str
# var: represents the value at the curernt execution of the for lop
# format:
# for var in iterable:
#     statmeent1
#     statmeent2
#     statmeent3
#     statmeent4

#rules
# looks at every element inside the list AND execiutes ALL STATEMENTS INSIDE THE FOR LOOP
# for every element in the list
# when it finishes all the statements THEN it geos to the next element
# when does it stop? stops when all elements in the list have executed all statements
# list1 = [1,2,3,4,5,6]
for charles in list1: # num =3
    print("ststatmetn1")
    print(charles)
    print('merry christmas')
    print("one more")
    
print("outside of the for loop")
print('continue regular execution')