def difference(people, maxCap):

    return maxCap - people


def decision(response):

    response = response.lower()
    while response != 'y' and response != 'n':
        response = input("Invalid input. Please enter y or n: ").lower()
    return response

response = 'y'

while response == 'y':

    meetingName = input("What is the meeting's name? ")
    print(f"The meeting's name is: {meetingName}")

    maxCap = int(input("What is the room capacity? "))
    people = int(input("How many people are attending the meeting? "))

    diff = difference(people, maxCap)

    if diff >= 0:
        print(f"{meetingName} is legal. {diff} more person(s) can be added to {meetingName} and still meet fire regulations.")
    else:
        print(f"{meetingName} is illegal. {-diff} person(s) must be removed from {meetingName} to meet fire regulations.")

    anotherCheck = input("Do you have another meeting to check? (y/n): ")
    response = decision(anotherCheck)

print("Goodbye!")