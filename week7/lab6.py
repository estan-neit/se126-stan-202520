def display_seating(seats):
    print("Seating Chart:")
    print("  A B C D")
    for row in range(len(seats)):
        print(f"{row + 1} ", end="")
        for seat in seats[row]:
            print(seat, end=" ")
        print()
    print()

def get_seat_choice():
    seat = input("Enter the seat you want to reserve (e.g., 1A): ").upper()
    seat = seat.replace(" ", "")
    if len(seat) < 2 or not seat[0].isdigit() or not seat[1].isalpha():
        print("Invalid seat format. Please try again.")
        return get_seat_choice()
    else:
        row = int(seat[0]) - 1
        col = ord(seat[1]) - ord('A')
        if row < 0 or row >= 7 or col < 0 or col >= 4:
            print("Seat out of range. Please try again.")
            return get_seat_choice()
        else:
            return row, col

def continue_reserving():
    choice = input("Do you want to continue reserving seats? (y/n): ").lower()
    if choice == 'y' or choice == 'n':
        return choice == 'y'
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return continue_reserving()

def all_seats_filled(seats):
    for row in seats:
        if 'A' in row or 'B' in row or 'C' in row or 'D' in row:
            return False
    return True

def search_seat(seats):
    seat = input("Enter the seat you want to search for (e.g., 1A): ").upper()
    seat = seat.replace(" ", "")
    if len(seat) < 2 or not seat[0].isdigit() or not seat[1].isalpha():
        print("Invalid seat format. Please try again.")
        return search_seat(seats)
    else:
        row = int(seat[0]) - 1
        col = ord(seat[1]) - ord('A')
        if row < 0 or row >= 7 or col < 0 or col >= 4:
            print("Seat out of range. Please try again.")
            return search_seat(seats)
        else:
            if seats[row][col] == 'X':
                print(f"Seat {seat} is already occupied.")
            else:
                print(f"Seat {seat} is available.")
            return

def main():
    seats = [['A', 'B', 'C', 'D'] for _ in range(7)]
    continue_reserve = True
    while continue_reserve:
        display_seating(seats)
        if all_seats_filled(seats):
            print("All seats are filled.")
            break
        action = input("Do you want to (r)eserve a seat or (s)earch for a seat? (r/s): ").lower()
        if action == 'r':
            row, col = get_seat_choice()
            if seats[row][col] == 'X':
                print("Seat is already occupied. Please choose another seat.")
            else:
                seats[row][col] = 'X'
        elif action == 's':
            search_seat(seats)
        else:
            print("Invalid input. Please enter 'r' or 's'.")
        continue_reserve = continue_reserving()

if __name__ == "__main__":
    main()