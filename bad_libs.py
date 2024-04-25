"""
This program is a madlibs game for users to enter random words and receive a story filled with their random words
Author: Luke Demi
"""

#inputs for user to answer for madlibs words
building = input("Type a type of Building: ")
item1 = input("Type a random item (plural): ")
item2 = input("Type another random item (plural): ")
day = input("Type a day of the week: ")
verb = input("Type a verb (present tense): ")
animal = input("Type an animal: ")
restaurant = input("Type a restaurant: ")
food = input("Type a food (plural): ")
activity1 = input("Type an activity: ")
activity2 = input("Type another activity: ")
activity3 = input("Type a third activity: ")
person = input("Type a noun (person): ")

def printStory():
    """
    This function prints out the story with the chosen words after the user has typed their words
    """
    print()
    print("There once was a princess who lived in a", building, "on the top of the tallest hill in all the land.", end=" ")
    print("She lived in total isolation, nothing around her except for ", item1, " and ", item2, ", with not another human to be seen.", sep="", end=" ")
    print("One", day, "Evening, a prince showed up to the foot of her", building, "and offered her the chance to see the city and leave her isolation.", end=" ")
    print("She quickly refused, scared of what the city may bring, but eventually decided she wanted to ", verb, ".", sep="")
    print()
    print("After riding to the city on a ", animal, " they stopped at ", restaurant, " and ate ", food, ".", sep="", end=" ")
    print("She experienced new things such as ", activity1, ", ", activity2, ", and ", activity3, ". She had never had so much fun!", sep="", end=" ")
    print("After a few months of the city, she decided that it was time to move back to her isolation since", person, "would be home to check on her in mere days.", end=" ")
    print("The prince still came by every few weeks and brought her to the city,", end=" ")
    print("but she decided that her home was the", building, "on the hill, not the city.", end=" ")
    print("THE END")

def main(): #main function
    printStory() #Call to the print function

main()