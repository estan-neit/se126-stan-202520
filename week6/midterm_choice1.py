#SE126.09
#Elijah Stan
#2/10/2025
#Program Prompt: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees.Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu:
#Westeros Services Directory Search
#1. Search by EMAIL
#2. Search by DEPARTMENT
#3. EXIT
#For option 1: When a searched-for item is found, print all data* in the program on the specific employeef from the lists. If they are not found, alert the user. For option 2: When a searched for item is found, print all data* in the program on all employees that match the criteria. If no one matches the searched-for criteria, alert the user. The user should not be able to quit the search program unless they choose option 3, to exit

import csv
import random

def departmentInfo(houseAllegiance):
    #houseAllegiance: House Stark, House Targaryen, House Tully, House Lannister, House Baratheon, The Night's Watch
    if houseAllegiance == "House Stark":
        return "Research & Development"
    elif houseAllegiance == "House Targaryen":
        return "Marketing"
    elif houseAllegiance == "House Tully":
        return "Human Resources"
    elif houseAllegiance == "House Lannister":
        return "Accounting"
    elif houseAllegiance == "House Baratheon":
        return "Sales"
    elif houseAllegiance == "The Night's Watch":
        return "Auditing"
    else:
        return "ERROR"

def phoneExt(houseAllegiance, usedExts):
    #usedExts: set of used extensions
    if houseAllegiance == "House Stark":
        extRange = range(100, 199)
        #extRange: range of extensions for each house
    elif houseAllegiance == "House Targaryen":
        extRange = range(200, 299)
    elif houseAllegiance == "House Tully":
        extRange = range(300, 399)
    elif houseAllegiance == "House Lannister":
        extRange = range(400, 499)
    elif houseAllegiance == "House Baratheon":
        extRange = range(500, 599)
    elif houseAllegiance == "The Night's Watch":
        extRange = range(600, 699)
    else:
        return "ERROR"
    
    availableExts = [ext for ext in extRange if ext not in usedExts]
        #availableExts: list of available extensions
        #If the extension is not in usedExts, add it to availableExts
    if availableExts:
        return random.choice(availableExts)
    else:
        return "ERROR"

def officeNum(firstName):
    #officeNum: employee's office number
    if firstName == "Eddard":
        return 100
    elif firstName == "Benjen":
        return 101
    elif firstName == "Catelyn":
        return 102
    elif firstName == "Arya":
        return 103
    elif firstName == "Robb":
        return 104
    elif firstName == "Sansa":
        return 105
    elif firstName == "Bran":
        return 106
    elif firstName == "Rickon":
        return 107
    elif firstName =="Jon":
        return 108
    elif firstName == "Tyrion":
        return 109
    elif firstName == "Jaime":
        return 110
    elif firstName == "Cersei":
        return 111
    elif firstName == "Robert":
        return 112
    elif firstName == "Stannis":
        return 113
    elif firstName == "Renly":
        return 114
    elif firstName == "Daenerys":
        return 115
    elif firstName == "Viserys":
        return 116
    else:
        return officeNumber
    
# Initialize lists to store records
firstName = []
#firstName: list of first names
lastName = []
#lastName: list of last names
age = []
#age: list of ages
screenName = []
#screenName: list of screen names
houseAllegiance = []
#houseAllegiance: list of house allegiances
email = []
#email: emails used by characters
department = []
#department: list of departments
phoneExtension = []
#phoneExtension: phone extensions used by characters
officeNumber = []
#officeNumber: office number of employee

# Track used phone extensions
usedExtensions = set()
#usedExtensions: set of used extensions

# Read the CSV file and store data into records
with open("week4/westeros.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        firstName.append(rec[0])
        lastName.append(rec[1])
        email.append(rec[2])
        department.append(rec[3])
        phoneExtension.append(rec[4])

print(f"{'FIRST':8}    {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':3}")
print("------------------------------------------------------------------------------------")
for i in range(len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {email[i]:30}  {department[i]:23}  {phoneExtension[i]:3}")

for i in range(0, len(firstName)):
    officeNumber.append(officeNum(firstName[i]))

# Write the data to midterm_choice1.csv
with open("week6/midterm_choice1.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(firstName)):
        if i < len(firstName) - 1:
            writer.writerow([firstName[i], lastName[i], email[i], department[i], phoneExtension[i], officeNumber[i]])
        else:
            csvfile.write(f"{firstName[i]},{lastName[i]},{email[i]},{department[i]},{phoneExtension[i]},{officeNumber[i]}")

# Alert the user
print(f"\nData has been written to westeros.csv")
print(f"Total number of employees: {len(firstName)}")
print(f"\nTotal number of records: {len(firstName)}")

# Count employees in each department
deptCount = {}
#deptCount: dictionary to count employees in each department
for dept in department:
    if dept in deptCount:
        deptCount[dept] += 1
    else:
        deptCount[dept] = 1

print("\nEmployee count by department:")
print("-----------------------------")
for dept, count in deptCount.items():
    print(f"{dept:23} {count:1}")

# Remove the final additional line in the text file
with open("week4/westeros.csv", "r") as file:
    lines = file.readlines()

with open("week4/westeros.csv", "w", newline='') as file:
    for line in lines:
        if line.strip():
            file.write(line)

#Sequential Search - search for an employee by their email address
print("Welcome to the employee search system")
answer = input("Would you like to start your search? (y/n): ")
while answer == "y":
    #answer: user's choice to start search system
    print("\t~Search Menu~")
    print("1. Search by email")
    print("2. Search by department")
    print("3. Exit search system")
    searchType = input("Enter your search type [1-3]: ")
    #searchType: user's choice of search type

    if searchType == "1":
        found = -1 #flag var, will be replaced with index position if name is found
        searchEmail = input("Enter the email you wish to find: ") #email we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(email)):
            #for loop performs the SEQUENCE - from start through end of list items

            if searchEmail.lower() == email[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #email FOUND!
            print(f"Your search for {searchEmail} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {email[found]:3}  {department[found]:3}  {phoneExtension[found]:3}")
        else:
            #NOT found
            print(f"Your search for {searchEmail} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif searchType == "2":
        found = -1 #flag var, will be replaced with index position if name is found
        searchDept = input("Enter the department you wish to find: ") #dept we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(department)):
            #for loop performs the SEQUENCE - from start through end of list items

            if searchDept.lower() == department[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #dept FOUND!
            print(f"Your search for {searchDept} was FOUND! Here is their data: ")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {email[found]:3}  {department[found]:3}  {phoneExtension[found]:3}")
        else:
            #NOT found
            print(f"Your search for {searchDept} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif searchType == "3":
        answer = "n"

    else:
        print("ERROR: Invalid search type. Please try again.")
        
print("Thank you for using the employee search system. Goodbye!")