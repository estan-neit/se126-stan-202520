# Elijah Stan
# 3/5/2025
# SE126.04
# Lab 7 - Dictionaries and Files

# PROGRAM PROMPT: Build a mini programming dictionary a user can search through and ad to using the words.csv file: 
# words.csv fields
# --------------------------------
# Field num       | File Data
# 0 Word (unique) | 1 Definition
# Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu:
# My Programming Dictionary Menu
# 1. Show all words – Show all words and their definitions stored to the dictionary
# 2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
# 3. Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
# 4. EXIT

#--IMPORTS----------------------------------------------------------------
import csv

#--FUNCTIONS--------------------------------------------------------------    
def swap(index, listName):
    # this function swaps the values of two elements in a list
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#--MAIN EXECUTING CODE-----------------------------------------------------
library = {}
# dictionary to store the words and their definitions

names = []
# list to store the words
defs = []
# list to store the definitions

with open("week8/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        # use the below for every record in the file
        # file is a 2D list
        # rec is 1st record's data
        library.update({rec[0] : rec[1]})
        names.append(rec[0])
        defs.append(rec[1])
         
        # libraryNum: rec[0], a string
        # title: rec[1], also a string

#--DISCONNECTED FROM FILE-------------------------------------------------
ans = "y"
# user's choice
menu = ['1', '2', '3', '4']
# choices for menu

while ans == "y": # all optyions are in the while loop
    print("Dictionary Menu")
    print("1. Show All Words")
    # words defined in the dictionary
    print("2. Search For A Word")
    # user can enter word and program will show its definition if it is in the dictionary
    print("3. Add A Word")
    # user can add a word and its definition to the dictionary
    print("4. EXIT")
    # exit the program

    choice = input("What Option Would You Like To Choose? Choose Option From 1 To 4: ") # user's choice

    if choice not in menu:
        print("\n***Invalid Entry***\n***Try Again***")

    elif choice == "1":
        print("\nShow All Words\n")

        print(f"{'WORD':25} : {'DEFINITION'}")
        print("-" * 200)


        for key in library:
        # for every key found in dictionary
            print(f"{key.upper():25} : {library[key]}")
            print("-" * 200)

    elif choice == "2":
        print("\nSearch For A Word")

        search = input("Enter The Word You Are Searching For In The Dictionary?: ").lower()

        found = 0

        for key in library:
            if search.lower() == key.lower():
                found = key

        if found != 0:
            print(f"\nHere Is Your Search For {search}:\n")
            print("-" * 200)
            print(f"{found.upper():4} : {library[found]}")
            print("-" * 200)
        else:
            print(f"\nYour Search For {search} Was Not Found. Please Try Again.\n")

    elif choice == "3":
        print("\n~Add A Word~")

        word = input("Enter The Word You Want To Add: ")
        meaning = input("Enter The Definition Of The Word You Want To Add: ")

        if word not in library:
            library.update({word : meaning})
            print("-" * 200)
            print(f"{'WORD':25} : {'DEFINITION'}")
            print("-" * 200)
       
            for key in library:
                print(f"{key.upper():25} : {library[key]}")
                print("-" * 200)
                 
    elif choice == "4":
        print(f"\n~EXIT~")
        ans = "n"
   
    else:
        print("\n***Invalid Entry***\n***Try Again***")

print("\nThank You For Using The Dictionary Program. Goodbye")
print("-" * 200)

