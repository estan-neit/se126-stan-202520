# Elijah Stan
# SE126.02
# Lab 5: Searching & Sorting
# 2/21/25

# Program Prompt: Build a personal library search system using the file book_list.csv. Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

# Imports

import csv

# Functions
def showAllTitles():
    # Print all titles in the library
    for i in range(len(title)):
        print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")

def searchBooks(searchType, keyword):
    # Search for books based on searchType and keyword
    for i in range(len(title)):
        if searchType == 'libNum' and keyword == libNum[i]:
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")
        elif searchType == 'title' and keyword.lower() in title[i].lower():
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")
        elif searchType == 'author' and keyword.lower() in author[i].lower():
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")
        elif searchType == 'genre' and keyword.lower() in genre[i].lower():
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")
        elif searchType == 'pgCount' and int(keyword) == int(pgCount[i]):
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")

def booksStatus(status):
    # Print all books with the specified status
    for i in range(len(status)):
        if status[i].lower() == status:
            print(f"{libNum[i]}, {title[i]}, {author[i]}, {genre[i]}, {pgCount[i]}, {status[i]}")

# Initialize lists to store book data
libNum = []
# libNum: Library Number
title = []
# title: Title of book
author = []
# author: Author of book
genre = []
# genre: Genre of book
pgCount = []
# pgCount: Page Count of book
status = []
# status: Status of book (available/on loan)

# Read data from CSV file and store in lists
with open('week7/book_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        libNum.append(row[0])
        title.append(row[1])
        author.append(row[2])
        genre.append(row[3])
        pgCount.append(row[4])
        status.append(row[5])
# Disconnected from file

choice = ''
while choice != '8':
    print("\nLibrary Lookup Menu")
    print("1. Show All title")
    print("2. Search for a Title")
    print("3. Search for an Author")
    print("4. Search for a Genre")
    print("5. Search for Page Count")
    print("6. Show All Available")
    print("7. Show All On Loan")
    print("8. EXIT")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        showAllTitles()
    elif choice == '2':
        keyword = input("Enter title or keyword: ").lower()
        if not searchBooks('title', keyword):
            print("No matching titles found.")
    elif choice == '3':
        authorName = input("Enter author name: ").lower()
        if not searchBooks('author', authorName):
            print("No matching authors found.")
    elif choice == '4':
        genreName = input("Enter genre: ").lower()
        if not searchBooks('genre', genreName):
            print("No matching genres found.")
    elif choice == '5':
        pageCount = input("Enter page count: ")
        searchBooks('pgCount', pageCount)
    elif choice == '6':
        booksStatus('available')
    elif choice == '7':
        booksStatus('on loan')
    elif choice == '8':
        print("Thank you for using the program.")
    else:
        print("Invalid choice. Please try again.")
