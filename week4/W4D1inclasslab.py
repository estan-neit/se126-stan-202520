#W4D1 - Sequential Search

#Elijah Stan
#1/27/2025
#SE126.04

#PROGRAM PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#--IMPORTS------------------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"
    return let #the 'let' value will literally replace the letter () call in main code
#--MAIN EXECUTING CODE------------------------------------------------

#create some empty lists - one list for every potential field in the file
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#-----connected to file-------------------------
with open("textFile/class_grades.csv") as csvfile:
    #indent one level while connected to the file
    file = csv.reader(csvfile)

    for rec in file:
        #store data from current record to corrosponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connect by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from file--------------------------------------------

#process the lists to create and store each student's numeric average as well as letter grade average, the display all data back to the user
numAvg = []          #holds student's numeric avg: (test1 + test2 + test3) / 3
letAvg = []          #holds student's letter avg: letter(numAvg) return

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    numAvg.append(a)
    letAvg.append(letter(a))

#print field headers for display below
print(f"{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
print("---------------------------------------------------------------------------------------------------------------")
#processing through lists for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {numAvg[i]:6.1f}  {letAvg[i]}")
print("---------------------------------------------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")

#Sequential Search - search for a student by their LAST name
print("Welcome to the stuident search system")
answer = input("Would you like to start your search? (y/n): ")
while answer == "y":
    print("\t~Search Menu~")
    print("1. Search by last name")
    print("2. Search by first name")
    print("3. Search by letter grade")
    print("4. Exit search system")
    searchType = input("Enter your search type [1-4]: ")

    if searchType == "1":
        found = -1 #flag var, will be replaced with index position if name is found
        searchLast = input("Enter the last name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(lastName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if searchLast.lower() == lastName[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {searchLast} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {numAvg[found]:6.1f}  {letAvg[found]}")
        else:
            #NOT found
            print(f"Your search for {searchLast} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif searchType == "2":
        found = -1 #flag var, will be replaced with index position if name is found
        searchFirst = input("Enter the first name you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(firstName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if searchFirst.lower() == firstName[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!
            print(f"Your search for {searchFirst} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {numAvg[found]:6.1f}  {letAvg[found]}")
        else:
            #NOT found
            print(f"Your search for {searchFirst} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif searchType == "3":
        
        #step 1: set-up and gain search query
        found = [] #empty list, found locations (index) will be stored here
        searchLet = input("Enter the letter grade you wish to find: ") #grade we are looking for all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(letAvg)):
            #for loop performs the SEQUENCE - from start through end of list items

            if searchLet.upper() == letAvg[i]:
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list
                print(f"Found a {searchLet} grade in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an empty list
            #NOT found
            print(f"Your search for {searchLet} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            #last name FOUND!
            print(f"Your search for {searchLet} was FOUND! Here is their data: ")
            for i in range(0, len(found)):
                print(f"{firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {numAvg[found[i]]:6.1f}  {letAvg[found[i]]}")

    elif searchType == "4":
        answer = "n"

    else:
        print("ERROR: Invalid search type. Please try again.")
        

print("Thank you for using the student search system. Goodbye!")