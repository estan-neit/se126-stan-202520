#W3D2 - List Review -1D Lists and Parallel Lists

#Prompt: Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1D lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new piece of data for each student: their current average test score.

#This file uses class_grates.csv

#--IMPORTS-----------------------------------------------------------------------
import csv
#--FUNCTIONS---------------------------------------------------------------------

#--MAIN EXECUTING CODE-----------------------------------------------------------

#initalize a record counting variable
totalRecords = 0

#create an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []


#connecting to the file
with open("textFile/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        totalRecords += 1

        #fname = rec[0]

        #print(fname)

        #store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)
        
        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file

#proccessing lists -- USE A FOR LOOP
for index in range(0, len(firstName)):
    #for every item, indes will start at 0 and run up to (not including) the length (# of items)
    print(f"INDEX {index}:  {firstName[index]:10}   {lastName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}")

#create a new list to hold each student's avg test score
avg = []

for i in range(0 , len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)

print(f"INDEX #:  {'FIRST':10}   {'LAST':10}   {'T1':3}   {'T2':3}   {'T3':3}   {'AVG'}")
print("--------------------------------------------------------------------------------------------")
for index in range(0, len(firstName)):
    #for every item, indes will start at 0 and run up to (not including) the length (# of items)
    print(f"INDEX {index:3}:  {firstName[index]:10}   {lastName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}   {avg[index]:.2f}")
print("--------------------------------------------------------------------------------------------")

#calc the entire class avg using a for loop to add each student's avg to the class total
totalAvg = 0
for i in range(0, len(avg)):
    totalAvg += avg[i]

classAvg = totalAvg / len(avg)

print(f"\nTotal records in file: {totalRecords}\nCURRENT CLASS AVERAGE: {classAvg:.2f}\n\nGoodbye!")