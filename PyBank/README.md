## PyFrat (*<ins>Py</ins>Bank's <ins>F</ins>inancial <ins>R</ins>ecords <ins>A</ins>nalysis <ins>T</ins>ool*)

![Revenue](Images/revenue-per-lead.jpg)

PyFrat ("PyBank's Financial Records Analysis Tool") is a Python script written in the Jupyter Labs notebook environment and exported to an executable file. PyFrat analyses a financial dataset provided by the PyBank institution and performes a number of calculations including the following:

* The <ins>total number of months</ins> included in the dataset

* The <ins>net total amount of Profit and Losses</ins> over the subject period.

* The <ins>average of the changes in Profit and Losses</ins> over the subject period.

* The <ins>date and amount for the greatest increase in profits</ins> month-to-month.

* The <ins>date and amount for the greatest decrease in profits</ins> month-to-month.

<br>

The analysis will print the results to the terminal in the following format:
```
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```
The same results will also be exported as the text file [results.txt](Resources/results.txt).

## Running the program

Change the directory from the root repository folder to the `PyBank` folder. The script can executed by entering the following into the terminal command line:

```python
python main.py
```
A Jupyter Notebook version has been included in same folder and is titled [main.ipynb](main.ipynb).

## Imports

PyFrat imports the `os` module to facilitate the manipulation of files, folders, and paths across operating systems. The `csv` module provides classes that allow for the reading and writing of data in csv format.

The PyBank dataset is imported from the file [budget_data.txt](Resources/budget_data.csv) and read into the variable `csvreader` as shown in the code snippet below:

```python
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
```
This makes the dataset available for analysis and calculations.

## Methods

The analysis was conducted primarily within the context of two `for` loops with variables `change` storing the difference between the current row iteration of `data` and `last_row` and appending to the list `change_m2m` which stores the month-to-month changes. The`net_PL` variable was used to calculate the 




## what achieved
a

## references/sources

The following sources were consulted in the development of this script. 

* [Python.org](https://docs.python.org/3/library/functions.html)
* [stackoverflow](https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python)
* [Codecademy](https://www.codecademy.com/catalog/language/python)
* [Real Python](https://realpython.com/python-sum-function/)
