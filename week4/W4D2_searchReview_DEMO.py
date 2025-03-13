#W4D2 - Sequential Search Review + Creating & Writing to Text Files

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#--IMPORTS---------------------------------------------
import csv
#--FUNCTIONS-------------------------------------------

#--MAIN EXECUTING CODE---------------------------------

#create an empty list for each potential field in the file
dragons = []    #field0 - dragon names
riders = []     #field1 - rider names
counts = []     #field2* - 1 or 2, count of colors
color1 = []     #first primary color
color2 = []     #second color, only when count is 2

with open("textFiles/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        counts.append(rec[2])
        color1.append(rec[3])

        if rec[2] ==  "2":
            color2.append(rec[4])
        elif rec[2] == "1":
            color2.append("------")
        else:
            color2.append("ERROR")
#disconnected from file-----------------------------------

#process lists to display data to the console
print(f"{'DRAGONS':15}  {'RIDERS':30}  {'#':3}  {'COLOR1':8}  {'COLOR2':8}")
print("----------------------------------------------------------------------")
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}  {riders[i]:30}  {counts[i]:3}  {color1[i]:8}  {color2[i]:8}")
print("----------------------------------------------------------------------")

#SEARCH FOR A SPECIFIC DRAGON
#step 1: set up and gain of search
found = "x"
search = input("Which dragon are you looking for?: \n")

#step 2: perform search --> for loop w/ if statement
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location (index) of our searched-for value
        found = i

#step 3: filter and display results
if found != "x":
    print(f"Your search for {search} has been FOUND: \n")
    print(f"{dragons[found]:15}  {riders[found]:30}  {counts[found]:3}  {color1[found]:8}  {color2[found]:8}")
else:
    print(f"Your search for {search} was NOT FOUND")

#Search for a color set

found = []
search = input("Enter the color you are looking for: \n")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

print("Here is what the found list contains: ")
for i in range(0, len(found)):
    print(f"\t{found[i]}")

if not found: #"if the found list is empty"
    print(f"Your search for {search} was NOT FOUND")
else:
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15}  {riders[found[i]]:30}  {counts[found[i]]:3}  {color1[found[i]]:8}  {color2[found[i]]:8}")


#WRITE SOME DATA TO A FILE + CREATE SAID FILE
#create and write dragons and riders of the data to a new file:
file = open("week4/targs2.csv", "w")

for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}\n")
file.close()