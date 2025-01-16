#W2D2 Lab 2

#PROGRAM PROMPT:


#VARIABLE DICTIONARY:


#--IMPORTS------------------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------------------

#--MAIN EXECUTING CODE------------------------------------------------

#-----connected to file-------------------------

totalRec = 0

with open("textFile/filehandling.csv") as csvfile:
    #indent one level while connected to the file

    file = csv.reader(csvfile)

    for rec in file:
        totalRec += 1
        #below code occurs for every record (row) in the file (text file -> 2D list)

        #assign each field data value to a friendly var name
        compType = rec[0]
        brand = rec[1]
        processor = rec[2]
        ramGB = rec[3]
        HDD1Size = rec[4]
        numDisk = rec[5]
        OS = rec[6]
        year = rec[7]

        if 
        HDD2Size = rec[6]
        






