#W2D2 Lab 2

#PROGRAM PROMPT:


#VARIABLE DICTIONARY:


#--IMPORTS------------------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------------------

#--MAIN EXECUTING CODE------------------------------------------------
compType = []
brand = []
processor = []
ramGB = []
HDD1Size = []
HDD2Size = []
numDisk = []
OS = []
year = []


#-----connected to file-------------------------

totalRec = 0

with open("textFile/filehandling.csv") as csvfile:
    #indent one level while connected to the file

    file = csv.reader(csvfile)

    for rec in file:
        totalRec += 1
        #below code occurs for every record (row) in the file (text file -> 2D list)
        
        #Rec[0] -> computer type
        if rec[0] == "D":
            compType = "Desktop"
        else:
            compType = "Laptop"

        #Rec[1] -> 
        if rec[1] == "DL":
            brand = "Dell"
        if rec[1] == "GW":
            brand = "Gateway"

        #assign each field data value to a friendly var name
        compType = rec[0]
        brand = rec[1]
        processor = rec[2]
        ramGB = rec[3]
        HDD1Size = rec[4]
        numDisk = (rec[5])

        if numDisk == 1:
            HDD1Size = "---"
            os = rec[6]
            year = rec[7]
        else:
            HDD2Size = rec[6]
            os = rec[7]
            year = int(rec[8])



totalRec += 1