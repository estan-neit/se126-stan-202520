# W7D1 - Introduction to 2D Lists

# 2D lists are just lists of lists! 

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
        print("***INVALID ENTRY!***")
        ans = input("Welcome to Jewel of Himalaya! Are you ready to place your order?").lower()
    
    return ans # This value will replace the function call in the main code

#--MAIN EXECUTING CODE------------------------------------
course = []
# Type of item on the menu (appetizer, entree, dessert, etc.)
name = []
# Name of the food item
description = []
# Description of the food item
price = []
# Price of the food item

#--DISCONNECTED FROM FILE--------------------------------

def menu():
    print(f"{'ITEM #':2}|{'COURSE':6}   {'NAME':32}   {'DESCRIPTION':65}  {'PRICE':2}")
    print("-" * 150)
    for i in range(len(course)):
        print(f" {i + 1:2}    {course[i]:10}  {name[i]:32}   {description[i]:65}  {price[i]:2}")
    print("-" * 150)


course = ['Appetizers', 'Appetizers', 'Appetizers', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Entrees', 'Tandoori', 'Tandoori', 'Tandoori', 'Tandoori', 'Rice', 'Rice', 'Noodles', 'Noodles', 'Desserts', 'Desserts']
name = ['Vegetable Pakoda', 'Lasooni Govi', 'Beef Sekuwa', 'Dal Makhini', 'Chana Massala', 'Himalayan Aloo', 'Murgh Makhini', 'Lamb Vindaloo', 'Saag Paneer', 'Tandoori Chicken (Bones)', 'Tandoori Chicken Tika (Boneless)', 'Seafood Tandoori', 'Paneer Tandoori', 'Lamb Biryani', 'Mix Fried Rice', 'Shrimp Fried Noodle', 'Egg Fried Noodle', 'Gulab Jamun', 'Himalayan Kulfi']
description = ['Mix vegetable and mashed potatoes dipped in tempura batter and deep fried.', 'Cauliflower battered in chickpea flour and marinated in ginger & garlic & and Himalayan spices.', 'Beef cubes grilled in clay oven.', 'Combination of lentils cooked in tomato and onion and cashew nut sauce. Served with Basmati rice.', 'Chickpeas cooked in onion and tomato & Masala sauce.', 'Spicy potatoes and cauliflower mix in curry sauce. Served with Basmati rice.', 'Chicken marinated in ginger and garlic and tomato onion sauce and Himalayan spices. Served with Basmati rice.', 'Lamb and potato mix curry with spicy sauce. Served with Basmati rice. *Cannot make mild*.', 'Glazed spinach blend with Himalayan cheese (paneer). Served with Basmati rice.', 'Chicken marinated in yogurt and spices and roasted in a tandoor.', 'Chicken marinated in yogurt and spices and roasted in a tandoor.', 'Shrimp and scallops and lobster.', 'Marinated paneer cheese baked in a traditional tandoor oven.', 'Indian style Mutton fried rice served with Raita (yogurt) Sauce.', 'Vegetable & egg & beef & chicken.', 'Stir fried noodles with shrimp and vegetables.', 'Stir fried noodles with egg and vegetables.', 'Deep fried milk balls soaked in sugar syrup.', 'Mango & Pistachio & Cashew & Almond.']
price = ['8', '12', '13', '20', '18', '19', '23', '24', '22', '20', '22', '36', '23', '24', '20', '24', '17', '5', '5']


apps = ['Vegetable Pakoda: Mix vegetable and mashed potatoes dipped in tempura batter and deep fried.  $8', 'Lasooni Govi: Cauliflower battered in chickpea flour and marinated in ginger & garlic & and Himalayan spices  $12', 'Beef Sekuwa: Beef cubes grilled in clay oven  $13']
entrees = ['Dal Makhini: Combination of lentils cooked in tomato and onion and cashew nut sauce. Served with Basmati rice  $20', 'Chana Massala: Chickpeas cooked in onion and tomato & Masala sauce  $18', 'Himalayan Aloo: Spicy potatoes and cauliflower mix in curry sauce. Served with Basmati rice  $19', 'Murgh Makhini: Chicken marinated in ginger and garlic and tomato onion sauce and Himalayan spices. Served with Basmati rice  $23', 'Lamb Vindaloo: amb and potato mix curry with spicy sauce. Served with Basmati rice. *Cannot make mild*  $24', 'Saag Paneer: Glazed spinach blend with Himalayan cheese (paneer)  $22']
tandoori = ['Tandoori Chicken (Bones): Chicken marinated in yogurt and spices and roasted in a tandoor  $20', 'Tandoori Chicken Tika (Boneless): Chicken marinated in yogurt and spices and roasted in a tandoor  $22', 'Seafood Tandoori: Shrimp and scallops and lobster  $36', 'Paneer Tandoori: Marinated paneer cheese baked in a traditional tandoor oven  $23']
rice = ['Lamb Biryani: Indian style Mutton fried rice served with Raita (yogurt) Sauce  $24', 'Mix Fried Rice: Vegetable & egg & beef & chicken  $20']
noodles = ['Shrimp Fried Noodle: Stir fried noodles with shrimp and vegetables  $20', 'Egg Fried Noodle: Stir fried noodles with egg and vegetables  $24']
desserts = ['Gulab Jamun: Deep fried milk balls soaked in sugar syrup  $5', 'Himalayan Kulfi: Mango & Pistachio & Cashew & Almond  $5']

menu()

ans = input("Would you like to enter the search program? [ y / n ]").lower()

while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [ y / n ]").lower()

# Online menu
while ans == "y":
    # ans: user's choice to start search system
    print(f"\tHere is our menu:")
    print("==========================================")
    print("\t~Jewel of Himalaya Online Menu~")
    print("1. Search by appetizers")
    print("2. Search by entrees")
    print("3. Search by tandoori")
    print("4. Search by rice")
    print("5. Search by noodles")
    print("6. Search by desserts")
    print("7. Show full menu")
    print("8. Exit search system")
    searchType = input("Enter your search type [1-8]: ")
    # searchType: user's choice of search type

    if searchType == "1":
        found = [] # Flag var, will be replaced with index position if name is found

        searchApp = input("Enter the appetizer you wish to find: ") # Appetizer we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(apps)):
            if searchApp.lower() in apps[i].lower():
                found.append(i)
            # For loop performs the SEQUENCE - from start through end of list items

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchApp} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Appetizer FOUND!
            print(f"Your search for {searchApp} was FOUND! Here is their data: ")
            for index in found:
                print(f"{apps[index]:3}")

                input("Would you like to order this item? [y/n]: ").lower()
                if ans == "y":
                    print("Your order has been placed!")
                if ans == "n":
                    print("Returning you back to the menu.")

    elif searchType == "2":
        found = [] # Flag var, will be replaced with index position if name is found
        searchEntree = input("Enter the entree you wish to find: ") # Entree we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(entrees)):
            if searchEntree.lower() in entrees[i].lower():
                found.append(i)
            # For loop performs the SEQUENCE - from start through end of list items

            if searchEntree.lower() == entrees[i].lower():
                # If performs the SEARCH - is what we're looking for here in the list?
                found = i  # Stores found item's INDEX LOCATION

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchEntree} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Entree FOUND!
            print(f"Your search for {searchEntree} was FOUND! Here is their data: ")
            for index in found:
                print(f"{entrees[index]:3}")

    elif searchType == "3":
        found = [] # Flag var, will be replaced with index position if name is found
        searchTandoori = input("Enter the tandoori you wish to find: ") # Tandoori we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(tandoori)):
            if searchTandoori.lower() in tandoori[i].lower():
                found.append(i)
            # For loop performs the SEQUENCE - from start through end of list items

            if searchTandoori.lower() == tandoori[i].lower():
                # If performs the SEARCH - is what we're looking for here in the list?
                found = i  # Stores found item's INDEX LOCATION

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchTandoori} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Tandoori FOUND!
            print(f"Your search for {searchTandoori} was FOUND! Here is their data: ")
            for index in found:
                print(f"{tandoori[index]:3}")
        
    elif searchType == "4":
        found = [] # Flag var, will be replaced with index position if name is found
        searchRice = input("Enter the rice you wish to find: ") # Rice we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(rice)):
            if searchRice.lower() in rice[i].lower():
                found.append(i)
            # For loop performs the SEQUENCE - from start through end of list items

            if searchRice.lower() == rice[i].lower():
                # If performs the SEARCH - is what we're looking for here in the list?
                found = i  # Stores found item's INDEX LOCATION

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchRice} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Rice FOUND!
            print(f"Your search for {searchRice} was FOUND! Here is their data: ")
            for index in found:
                print(f"{rice[index]:3}")
    
    elif searchType == "5":
        found = [] # Flag var, will be replaced with index position if name is found
        searchNoodles = input("Enter the noodles you wish to find: ") # Noodles we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(noodles)):
            if searchNoodles.lower() in noodles[i].lower():
                found.append(i)

            # For loop performs the SEQUENCE - from start through end of list items

            if searchNoodles.lower() == noodles[i].lower():
                # If performs the SEARCH - is what we're looking for here in the list?
                found = i  # Stores found item's INDEX LOCATION

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchNoodles} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Noodles FOUND!
            print(f"Your search for {searchNoodles} was FOUND! Here is their data: ")
            for index in found:
                print(f"{noodles[index]:3}")
            
    elif searchType == "6":
        found = [] # Flag var, will be replaced with index position if name is found
        searchDessert = input("Enter the dessert you wish to find: ") # Dessert we are looking for

        # Step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(desserts)):
            if searchDessert.lower() in desserts[i].lower():
                found.append(i)
            # For loop performs the SEQUENCE - from start through end of list items

            if searchDessert.lower() == desserts[i].lower():
                # If performs the SEARCH - is what we're looking for here in the list?
                found = i  # Stores found item's INDEX LOCATION

        # Step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            # NOT found
            print(f"Your search for {searchDessert} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else:
            # Dessert FOUND!
            print(f"Your search for {searchDessert} was FOUND! Here is their data: ")
            for index in found:
                print(f"{desserts[index]:3}")

    elif searchType == "7":
        menu()
        
    elif searchType == "8":
        ans = "n"

    else:
        print("ERROR: Invalid search type. Please try again.")

    answer(ans)


