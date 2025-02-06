#SE126.04
#Elijah Stan
#2/5/25
#PART 1: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.
#PART 2: Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. NOTE: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file).


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

# Track used phone extensions
usedExtensions = set()
#usedExtensions: set of used extensions

# Read the CSV file and store data into records
with open("week4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(rec[2])
        screenName.append(rec[3])
        houseAllegiance.append(rec[4])
        email.append(f"{rec[3]}@westeros.net")
        dept = departmentInfo(rec[4])
        department.append(dept)
        ext = phoneExt(rec[4], usedExtensions)
        phoneExtension.append(ext)
        usedExtensions.add(ext)

print(f"{'FIRST':8}    {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':3}")
print("------------------------------------------------------------------------------------")
for i in range(len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {email[i]:30}  {department[i]:23}  {phoneExtension[i]:3}")

# Write the data to westeros.csv
with open("week4/westeros.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(firstName)):
        if i < len(firstName) - 1:
            writer.writerow([firstName[i], lastName[i], email[i], department[i], phoneExtension[i]])
        else:
            csvfile.write(f"{firstName[i]},{lastName[i]},{email[i]},{department[i]},{phoneExtension[i]}")

# Alert the user
print(f"\nData has been written to westeros.csv")
print(f"Total number of employees: {len(firstName)}")

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