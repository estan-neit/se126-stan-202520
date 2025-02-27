# Elijah Stan
# 2/26/2025
# SE126.04
# Lab 6 - Collections and Logic
# PROGRAM PROMPT: For Lab #6, you must use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#--FUNCTIONS---------------------------------------------------------------------------
def show():
    # This function displays the seating chart
    for i in range(len(sA)):
        print(f"{i + 1} {sA[i]} {sB[i]} {sC[i]} {sD[i]}")

def answer(ans):
    # This function checks the answer for validity and returns the answer to the main code
    while ans != "y" and ans != "n":
        print("***INVALID ENTRY!***")
        ans = input("Would you like to enter the search program? [y/n]").lower()
    
    
    return ans #this value will replace the function call in the main code

#--MAIN EXECUTING CODE-----------------------------------------------------------------

sA = ["A", "A", "A", "A", "A", "A", "A"]
# sA = seat a in each row
sB = ["B", "B", "B", "B", "B", "B", "B"]
# sB = seat b in each row
sC = ["C", "C", "C", "C", "C", "C", "C"]
# sC = seat c in each row
sD = ["D", "D", "D", "D", "D", "D", "D"]
# sD = seat d in each row

# Disconnected from file

ans = input("Would you like to enter the search program? [ y / n ]").lower()

print(f"\tBook your plane seat here.")
print("==========================================")

ans = "y"

# Seat booking section
while ans == "y":
    show()
    row = int(input("Enter row [1-7]: "))
    seat = input("Enter seat type A, B, C or D: ").upper()

    if seat.upper() == "A":
        if sA[row - 1] != "X":
            sA[row - 1] = "X"
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

print("Thank you for booking your flight with us.")

show()