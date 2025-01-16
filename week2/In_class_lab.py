#Elijah Stan
#1/16/25
#SE 126.04
#W2D2 - Text File Handling Review (In class lab)

#PROGRAM PROMPT:
#The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
#can accommodate, and the number of people currently registered for the event. Write a program that
#displays all rooms that are over the maximum limit of people and the number of people that have to
#be notified that they will have to be put on the wait list. After the file is completely processed the
#program should display the number of records processed and the number of rooms that are over the
#limit.

#VARIABLE DICTIONARY:
#difference: function that subtracts current people in the room fromm max amount of people
#diff: returned value from difference function
#totalRec: total records in file
#roomsOver: amount of rooms that have more than capacity
#maxCap/max: most amount of people in a room at any point in time
#people/ppl: amount of persons in a room
#remaining: the amount of people needed to be removed to meet the capacity of the room
#name: name of the room

#--IMPORTS------------------------------------------------------------
import csv
#FUNCTIONS------------------------------------------------------------
def difference(people,maxCap):
    '''This function is passed 2 values and returns the difference between them'''
    diff = maxCap - people
    return diff #this valu will replace the difference() call in the main code

#MAIN EXECUTING CODE--------------------------------------------------

#initialize needed counting vars
totalRec = 0
roomsOver = 0

#-----connected to file-------------------------
print(f"\n{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER':5}")
print("---------------------------------------------")

with open("textFile/classLab2.csv") as csvfile:
    #we must indent one level while connected to the file

    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (text file -> 2D list)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])   #all text data read as a string, so cast as a num!
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the rooms that are over capacity (remaining is negative)
        if remaining < 0 :
            roomsOver += 1
            print(f"{name:20}   {max:5}   {ppl:5}    {abs(remaining):5}")

        #count ALL rooms!
        totalRec += 1

#-----disconnected from file--------------------
#display final data (countimmg vars)
print(f"\nRooms currently OVER capacity: {roomsOver}")
print(f"Total rooms in the file: {totalRec}")