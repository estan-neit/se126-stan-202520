#W2D1 - text file handling intro demo

#step 1: import the csv (comma separated value) library
import csv

totalRecords = 0 #holds total num of recs in file

#--connected to file-------------------------------------
#include relative file path in open()
#make sure \ switches to /
with open("textFile/simple.csv") as csvfile:
    #make sure to indent inside of code block

    #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list / matrix / table]
    file = csv.reader(csvfile)
    #print for headers
    print(f"{'NAME':10}  {'NUM':3}  {'COLOR'.title()}")
    print("----------------------------------------------")
    #step 3: process through every record (row) in the file
    for record in file:
        #add +1 to totalRecords to keep accurate count of recs
        totalRecords += 1

        #print(record) #entire record/row data as a list

        name = record[0]    #name field
        number = record[1]  #number field
        color = record[2]   #color field

        print(f"{name:10}  {number:3}  {color.title()}")
#--disconnected from file--------------------------------
print(f"\nTOTAL RECORDS: {totalRecords}\n")