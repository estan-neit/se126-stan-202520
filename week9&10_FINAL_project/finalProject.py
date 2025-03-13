#W7D1 - Introduction to 2D Lists

#2D lists are just lists of lists! 

#--IMPORTS------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------
def show():
    # This function displays the seating chart
    for i in range(len(course)):
        print(f"{i + 1} {course[i]} {name[i]} {description[i]} {price[i]}")

def answer(ans):
    # This function checks the answer for validity and returns the answer to the main code
    while ans != "y" and ans != "n":
        print("Sorry I couldn't hear what you said. It's too loud in here. Would you speak up please?")
        ans = input("Welcome to Jewel of Himalaya! Are you ready to place your order?").lower()
    
    
    return ans #this value will replace the function call in the main code
#--MAIN EXECUTING CODE------------------------------------
course = []
#type of item on the menu (appetizer, entree, dessert, etc.)
name = []
#name of the food item
description = []
#description of the food item
price = []
#price of the food item

'''
two_d_list = [
    ['1','2','3','4'],
    ['5','6','7','8'],
    ['9','0','A','B'],
    ]

for i in range(len(two_d_list)):
    for x in range(len(two_d_list[i])):
        print(two_d_list[i][x], end='')
    print()

    
file = []'''

with open("week9&10_FINAL_project/jewelOfHimalayaMenu.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        course.append(rec[0])
        name.append(rec[1])
        description.append(rec[2])
        price.append(rec[3])
#--DISCONNECTED FROM FILE--------------------------------





#search_title = input("Enter the author to search for: ")

'''
for i in range(len(fileData)):
    for x in range(len(fileData[i])):
        #print(fileData[i][x])
        if search_title.lower() in fileData[i][x].lower():
            print(f"{fileData[i][0]:5}  {fileData[i][1]:35}  {fileData[i][2]:25}  {fileData[i][3]:17}  {fileData[i][4]:3}  {fileData[i][5]}")
'''

def menu():
    print(f"{'ITEM #':2}|{'COURSE':6}   {'NAME':32}   {'DESCRIPTION':65}  {'PRICE':2}")
    print("-" * 150)
    for i in range(len(course)):
        print(f" {i + 1:2}    {course[i]:10}  {name[i]:32}   {description[i]:65}  {price[i]:2}")
    print("-" * 150)

course = ['Appetizers', 'Appetizers', 'Appetizers', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Tandoori', 'Tandoori', 'Tandoori', 'Tandoori', 'Rice', 'Rice', 'Noodles', 'Noodles', 'Dessert', 'Dessert']
name = ['Vegetable Pakoda', 'Lasooni Govi', 'Beef Sekuwa', 'Dal Makhini', 'Chana Massala', 'Himalayan Aloo', 'Murgh Makhini', 'Lamb Vindaloo', 'Saag Paneer', 'Tandoori Chicken (Bones)', 'Tandoori Chicken Tika (Boneless)', 'Seafood Tandoori', 'Paneer Tandoori', 'Lamb Biryani', 'Mix Fried Rice', 'Shrimp Fried Noodle', 'Egg Fried Noodle', 'Gulab Jamun', 'Himalayan Kulfi']
description = ['Mix vegetable and mashed potatoes deep in tempura batter and deep fried.', 'Cauliflower battered in chickpea flour and marinated in ginger & garlic & and Himalayan spices.', 'Beef cubes grilled in clay oven.', 'Combination of lentils cooked in tomato and onion and cashew nut sauce. Served with Basmati rice.', 'Chickpeas cooked in onion and tomato & Masala sauce.', 'Spicy potatoes and cauliflower mix in curry sauce. Served with Basmati rice.', 'Chicken marinated in ginger and garlic and tomato onion sauce and Himalayan spices. Served with Basmati rice.', 'Lamb and potato mix curry with spicy sauce. Served with Basmati rice. *Cannot make mild*.', 'Glazed spinach blend with Himalayan cheese (paneer). Served with Basmati rice.', 'Chicken marinated in yogurt and spices and roasted in a tandoor.', 'Chicken marinated in yogurt and spices and roasted in a tandoor.', 'Shrimp and scallops and lobster.', 'Marinated paneer cheese baked in a traditional tandoor oven.', 'Indian style Mutton fried rice served with Raita (yogurt) Sauce.', 'Vegetable & egg & beef & chicken.', 'Stir fried noodles with shrimp and vegetables.', 'Stir fried noodles with egg and vegetables.', 'Deep fried milk balls soaked in sugar syrup.', 'Mango & Pistachio & Cashew & Almond.']
price = ['8', '12', '13', '20', '18', '19', '23', '24', '22', '20', '22', '36', '23', '24', '20', '24', '17', '5', '5']

menu()

# Seat booking section
while ans == "y":
    show()
    row = int(input("Enter row [1-7]: "))
    seat = input("Enter seat type A, B, C or D: ").upper()

    if seat.upper() == "A":
        if course[row - 1] != "X":
            course[row - 1] = "X"
        else:
            sA[row -1] = "X"
            print(f"Seat {row}{seat.upper()} is taken. Please choose another seat.")

    elif seat.upper() == "B":
        if sB[row - 1] != "X":
            sB[row - 1] = "X"
        else:
            sB[row -1] = "X"
            print(f"Seat {row}{seat.upper()} is taken. Please choose another seat.")

    elif seat.upper() == "C":
        if sC[row - 1] != "X":
            sC[row - 1] = "X"
        else:
            sC[row -1] = "X"
            print(f"Seat {row}{seat.upper()} is taken. Please choose another seat.")

    elif seat.upper() == "D":
        if sD[row - 1] != "X":
            sD[row - 1] = "X"
        else:
            sD[row -1] = "X"
            print(f"Seat {row}{seat.upper()} is taken. Please choose another seat.")

    else:
        print(f"This seat either does not exist or was not entered correctly. Please try again.")

    ans = input("Is there another seat you wish to book? [ y / n ]: ").lower()

    answer(ans)