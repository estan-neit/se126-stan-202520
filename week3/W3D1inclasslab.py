#Elijah Stan
#1/20/2025
#Text File Handling

#W2D2 Lab 2

#PROGRAM PROMPT:
#You have been asked to produce a report that lists all the computers in the csv file
#filehandling.csv

#--IMPORTS------------------------------------------------------------
import csv
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
        #count the number of records in the file
        totalRec += 1
        #below code occurs for every record (row) in the file (text file -> 2D list)
        
        #Rec[0] -> computer type
        if rec[0] == "D":
            compType.append("Desktop")
        else:
            compType.append("Laptop")

        #Rec[1] -> brand of computer
        if rec[1] == "DL":
            brand.append("Dell")
        elif rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        else: #Optional if the file is too long to review first
            brand.append("*ERROR*")

        #assign each field data value to a friendly var name
        #Rec[2] -> type of processor
        processor.append(rec[2])
        #Rec[3] -> amount of RAM in GB
        ramGB.append(rec[3])
        #Rec[4] -> size of HDD1
        HDD1Size.append(rec[4])
        #Rec[5] -> how many disks the computer has
        numDisk.append(int(rec[5]))

        if int(rec[5]) == 1:
            HDD2Size.append("---")
            #Rec[6] -> type of OS
            OS.append(rec[6])
            #Rec[7] -> year of manufacture
            year.append(rec[7])
        else:
            #Rec[6] -> size of HDD2
            HDD2Size.append(rec[6])
            #Rec[7] -> type of OS
            OS.append(rec[7])
            #Rec[8] -> year of manufacture
            year.append(int(rec[8]))

#-----disconnected from file--------------------

print(f" {'Type':10}  {'Brand':9} {'Processor':10}     {'RAM':5}   {'HDD1':10} {'Disks':6}    {'HDD2':10}  {'OS':10} {'Year':10}")
print("==============================================================================================")
print()


print("---------------------------------------------------------------------------------------------")
print(f"\nTotal records in file: {len(compType)}\n\nThank you for using this program. Goodbye!")

for i in range(0,  len(compType)):
    print(f"{compType[i]:10}   {brand[i]:10}   {processor[i]:10}   {ramGB[i]:5}  {HDD1Size[i]:8} {numDisk[i]:5}       {HDD2Size[i]:10}  {OS[i]:7}    {year[i]:2}")

