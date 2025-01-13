#Variable dictionary
#people: amount of attentees
#maxCap: maximum capacity the room can hold
#difference/diff: function that finds the difference of amount of attendees and maximum capacity the room can hold
#decision: function that finds the decision of whether or not the meeting with all the attendees follows fire regulations or not
#response: logs user's answer, 'y' or 'n'
#meetingName: is the meeting's title
#anotherCheck: goes to ask the user if they want to check the legality of another meeting


print("Welcome to the fire marshal compliance meeting simulator")
#Welcome statement

def difference(people, maxCap):
    #difference/diff: function that finds the difference of amount of attendees and maximum capacity the room can hold
    return maxCap - people


def decision(response):
    #decision: function that finds the decision of whether or not the meeting with all the attendees follows fire regulations or not
    response = response.lower()
    while response != 'y' and response != 'n':
        response = input("Invalid input. Please enter y or n: ").lower()
    return response

response = 'y'

while response == 'y':
    #this loop asks the user various questions like meeting name, room capacity, and attendees
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
#Goodbye statement