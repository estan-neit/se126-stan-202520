#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
namesList = ["Abby", "Bobby", "Carol"]
print(namesList)       #entire list
print(namesList[0])    #first value  
print(namesList[len(namesList) - 1])       #last value

#creation & population of dictionaries
peopleDictionary ={
    #"key" : value
    fname 
}


#create an empty list for each potential field
#these MUST remain the same lenth in order to parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#gaining data from a text file 
with open("textFiles/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        else:
            color2.append("---")

        #adding data to a dictionary



#processing data from collections
#lists --> standard: for i in range():
print(f"{'NAMES':12} {'RIDERS':30} {'NUMS':3} {'COLOR1':8} {'COLOR2'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 75)

#dictionaries --> for key in collection:
for key in dragons:
    print(f"{key:upper()} : {dragons[key]}") #this will s

#searching & sorting
#BINARY SEARCH --> requires a set of ordered and UNIQUE data
#requires the sorting of data before searching! BUBBLE SORT


for i in range(0, len(names) - 1):
    for j in range(0, len(names) - 1):
        if names[j] > names[j + 1]:
            #swap places!
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)


#binary --> bi means 2 --> we create a high and low half of the list

#SEQUENTial search

search = input("\nPleas enter the DRAGON NAME you wish to find: ")

found = []

for key in dragons:
    if search.lower() in dragons[key][0].lower():
        found.append(key)

if not found:
    print(f"Sorry, we could not dind your search for {search}.")
else:
    print(f"We found your search for {search}; here are the results: ")
    
    for i in range(len[found]):

search = input("\nPleas enter the DRAGON NAME you wish to find: ")

min = 0
max = len(names) - 1
mid = int((min + max) / 2)

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record {mid}: ")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}")
else:
    print(f"Sorry, we could not find your search for {search}.")
    



#2D lists - lists of lists!

letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

print(letters)                         #whole 2D list (you will see multiple[]s)
print(letters[0])                      #first list inside of 2D letters
print(letters[0][0])                   #first value of first list in 2D letters
print(letters[0][len(letters[0]) - 1]) #last value in first list in 2D

letters[]