import csv

#--FUNCTIONS-----------------------------------------------------------------------------
def display(x, records):

    print(f"{'CLASS':8}  {'NAME':10}  {'MEANING':25}  {'CULTURE'}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{classType[x]:8}  {name[x]:10}  {meaning[x]:25}  {culture[x]}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{classType[found[i]]:8}  {name[found[i]]:10}  {meaning[found[i]]:25}  {culture[found[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{classType[i]:8}  {name[i]:10}  {meaning[i]:25}  {culture[i]}")

    print("----------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
    

def seqSearch(search,listName):
    for i in range(0, len(listName)):
        if search.lower() in listName[i].lower():
            found.append(i)
#--MAIN EXECUTING CODE-------------------------------------------------------------------
row = []
lW = []
lA = []
rA = []
rW = []

planeSeatingChart = [
    ["1", "A", "B", "C", "D"],
    ["2", "A", "B", "C", "D"],
    ["3", "A", "B", "C", "D"],
    ["4", "A", "B", "C", "D"],
    ["5", "A", "B", "C", "D"],
    ["6", "A", "B", "C", "D"],
    ["7", "A", "B", "C", "D"]
]

with open("collectionsAndLogic.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(planeSeatingChart)
    for i in range(len(row)):
        if i < len(row) - 1:
            writer.writerow([row[i], lW[i], lA[i], rA[i], rW[i]])
        else:
            csvfile.write(f"{row[i]},{lW[i]},{lA[i]},{rA[i]},{rW[i]}")

#disconnected from file------------------------------------

#display whole list data to user
#display("x",len(classType)) #practice with function

#display one row data to user
#display(0, len(classType)) #practice with function

#display one row of data from the file
#display(16, len(name))

ans = input("Would you like to enter the search program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()

#main searching loop
while ans == "y":
    found = [] #reset found list so each new menu/search it is empty

    print("\tSEARCHING MENU")
    print("1. Search by TYPE") #shows all of either elf or dragon
    print("2. Search by NAME") #binary search review
    print("3. Search by MEANING") #find part of a whole
    print("4. EXIT")

    searchType = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if searchType not in ["1", "2", "3", "4"]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    elif searchType == "1":
        print(f"\nYou have chosen to search by TYPE")
        
        
        #allow the user to search for a certain TYPE and then display ALL records (multi) with that type
        search = input("Which type: 'dragon' or 'elf':")

        #show all values in classType of either dragon or elf --> sequential search!
        if search.lower() not in ["dragon", "elf"]:
            print("Sorry, only 'dragon' or 'elf' are accepted. Please try again.")

        else:
            #SEQUENTIAL SEARCH for MULTIPLE VALUES MATCHING SEARCH TERM
            
            for i in range(0, len(classType)):
                if search.lower() == classType[i].lower():
                    found.append(i) #add current index (location) of found item to 'found' list
            #display results
            if not found: #if the found list is still empty
                print(f"Sorry your search for {search} came up empty.")
            else:
                #call display() to show the values
                display("x", len(found))

    elif searchType == "2":
        print(f"\nYou have chosen to search by NAME")


        #allow the user to search for ONE specific and unique name value (binary search!)
        search = input("Enter the NAME you are looking for: ")
        #BINARY SEARCH: 
        #               * requires a collection of UNIQUE values to search through
        #               * requires the collection to be SORTED (ORDERED)
        #                       ascending or descending ; alpha or numeric



        #BUBBLE SORT--> higher values 'bubble' to the bottom of the collection
        for i in range(0, len (name) - 1):
            for j in range(0, len(name) - 1):
                if name[j] > name[j + 1]:
                    #they must swap places because the higher value must come afterwards
                    temp = name[j]
                    name[j] = name[j + 1]
                    name[j + 1] = temp

                    #use the function to cut down on coding and potential errors!
                    swap(j, classType)
                    swap(j, meaning)
                    swap(j, culture)


        #check our bubble sort -- sorting in ascending order by name
        display("x", len(name))

        #BINARY SEARCH: must be performed on ordered/sorted lists populated with unique values - can only find ONE item or value

        min = 0                         #lowest possiblen index
        max = len(name) - 1             #highest index
        mid = int((min + max) / 2)      #middle index in sorted list

        while min < max and search.lower() != name[mid].lower():
            #while above is true, list is not yet exhausted and we haven't found what we are looking for so, must go through another searching iteration!
            if search.lower() < name[mid].lower():
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
            mid = int((min + max) / 2) 

        if search.lower() == name[mid].lower():
            print(f"Huzzah! We have found your search for {search}, see details below:")
            display(mid, len(name))
        else:
            print(f"Sorry, we could not find your seach for {search}. Please try again.")

        
    elif searchType == "3":
        print(f"\nYou have chosen to search by MEANING")

        search = input("Enter the meaning seach term you are looking for: ").lower()


        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, we could not find your seach for {search}. Please try again.")
        else:
            print(f"Huzzah! We have found your search for {search}, see details below:")
            display("x", len(found))

        
    elif searchType == "4":

        print(f"\nYou have chosen to EXIT")
        ans = "N"

#alert user that program is about to end
print("Thank you for using my program, goodbye!\n")