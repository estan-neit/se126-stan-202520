import csv

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

library = {}
word = {}
define = {}

with open("week8/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        library.update({rec[0] : rec[1]})
        word.update({rec[0]})
        define.update({rec[1]})

# disconnected from file-------------------------------

print(f"{'KEY':4} : {'TITLE'}")
print("-" * 50)
for key in library:
    # for every key found in the library dictionary
    print(f"{key.upper():4} : {library[key]}")
print("-" * 50)

#--SEQUENTIAL SEARCH WITH DICTIONARIES------------------
search = input("\nEnter the TITLE you are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-" * 50)
    '''
    for i in range(0, len(found)):
        print(f"{found[i].upper():4} : {library[found[i]]}")
    print(f"{found.upper():4} : {library[found]}")
    '''
    print(f"{found.upper():4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search}")
