#SE126.04
#Elijah Stan
#W3D2
#Lab 3.1D: Parallel Lists

#Program prompt: Construct a program that will analyze potential voters. The program should generate the following totals:
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.

import csv

# Initialize lists
notEligible = []
#not eligible to vote
notRegistered = []
#eligible but not registered
eligibleNotVoted = []
#eligible but did not vote
voted = []
#voted
totalRecords = []
#total records in file

# Open and read the CSV file
with open("textFile/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        totalRecords.append(rec)
        age = int(rec[1])
        registered = rec[2].lower() == 'y'
        #registered or not
        votedBefore = rec[3].lower() == 'y'
        #has voted before or not
        
        if age < 18:
            notEligible.append(rec)
        elif age >= 18 and not registered:
            notRegistered.append(rec)
        elif age >= 18 and registered and not votedBefore:
            eligibleNotVoted.append(rec)
        elif registered and votedBefore:
            voted.append(rec)

# Print the results
print(f"\nNumber of individuals not eligible to register: {len(notEligible)}")
print(f"\nNumber of individuals who are old enough to vote but have not registered: {len(notRegistered)}")
print(f"\nNumber of individuals who are eligible to vote but did not vote: {len(eligibleNotVoted)}")
print(f"\nNumber of individuals who did vote: {len(voted)}")
print(f"\nNumber of records processed: {len(totalRecords)}")
print("===============================================")
print("Thank you for using this program!")