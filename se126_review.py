#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------



#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
namesList = ["Abby", "Bobby", "Carol"]
print(namesList)       #entire list
print(namesList[0])    #first value  
print(namesList[len(namesList) - 1])       #last value

#creation & population of dictionaries
peopleDictionary ={
    #"key" : value
}


#gaining data from a text file 
with open("textFiles/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 


        #adding data to a dictionary



#processing data from collections



#searching & sorting




#2D lists - lists of lists! 