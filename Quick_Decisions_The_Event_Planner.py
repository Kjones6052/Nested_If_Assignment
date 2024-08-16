# Task 1: Code Correction
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = input("Enter number of attendees: ")
venue = "large hall" if (int(attendees) > 100) else "conference room"
print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" 
# or "projector" based on the number of attendees.

attendees = input("Enter number of attendees: ")
venue = "large hall" if (int(attendees) > 100) else "conference room"
accomodations = "get a speaker system and projector" if (int(attendees) > 100) else "no accomodations required"
print(venue, accomodations)

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = input("Enter number of attendees: ")
venue = "large hall" if (int(attendees) > 100) else "conference room"
accomodations = "get a speaker system and projector" if (int(attendees) > 100) else "no accomodations required"
food_choice = input("are the guests vegetarian? ")
catering = "vegatarian delight caterers" if food_choice == "yes" else "gourmet meals caterers"
print(venue, accomodations, catering)