from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Key", "Sword"],

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}

print(room['outside'].name)
print(room['outside'].avail_items)


# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Ronnie', room["outside"])
print(player1.current_room.name)


# Write a loop that:#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
 #  '\n' "Player's current room description: ", {room['outside'].description})


user_is_playing = True
while user_is_playing:
    print(player1.current_room.name)
    # print(player1.avail_items)
    # print(player1.current_room.description)
    for line in textwrap.wrap(player1.current_room.description, width = 30):
        print(line)
    direction_input = input("What direction do you want to go?: ")
    add_item_input = input("Choose the item you like?Key/Sword?Flashlight/Backpack/Lightsaber/Hat/Nail/Hammer: ")
    if direction_input in ["n", "s", "e", "w"]:
        player1.move(direction_input).add_items(add_item_input)
    else:
        print("This is not the valid command")
        user_is_playing = False





# while True:
#     print("Player current location:", {player1.current_room}, '\n', "Player's current room description: ", {room['outside'].description})
  
#     direction = input("Enter move command('n', 's' , 'e' , 'w'): ") 
     
#     if player1.current_room =="outside" and direction == "n":        
#         print("you reached the 'Foyer'!")
#         player1.current_room ="foyer"          
#     if player1.current_room =="foyer" and direction == "s":
#             print("You are back to 'Outside'!")
#             player1.current_room ="outside"
#     elif player1.current_room =="foyer" and direction == "n":
#             print("You reached 'Overlook!")
#             player1.current_room ="overlook"
#             if player1.current_room =="overlook" and direction == "s":
#                 print("You reached 'Foyer!")
#                 player1.current_room ="foyer"
#             elif player1.current_room =="overlook" and direction == "n":
#                 print("Wrong move!")
#             elif player1.current_room =="overlook" and direction == "e":
#                 print("Wrong move!")
#             elif player1.current_room =="overlook" and direction == "w":
#                 print("Wrong move!")
#         elif player1.current_room =="foyer" and direction == "e":
#             print("You are now in room 'Narrow'!")
#             player1.current_room ="narrow"
#             if player1.current_room =="narrow" and direction == "w":
#                 print("You reached 'Foyer!")
#                 player1.current_room ="foyer"
#             elif player1.current_room =="narrow" and direction == "e":
#                 print("Wrong move!")
#             elif player1.current_room =="narrow" and direction == "n":
#                 print("You reached 'Treasure'!")
#                 player1.current_room ="tresure"
#                 if player1.current_room =="treasure" and direction == "s":
#                     print("You are back to 'Narrow'!")
#                     player1.current_room ="narrow"
#                 elif player1.current_room =="treasure" and direction == "n":
#                     print("Wrong move!")
#                 elif player1.current_room =="treasure" and direction == "w":
#                     print("Wrong move!")
#                 elif player1.current_room =="treasure" and direction == "e":
#                     print("Wrong move!")
#             elif player1.current_room =="narrow" and direction == "s":
#                 print("Wrong move!")
#         elif player1.current_room =="foyer" and direction == "w":
#             print("invalid move!")
#     elif player1.current_room =="outside" and direction == "s":
#         print("Wrong move!")
#     elif player1.current_room =="outside" and direction == "e":
#         print("Wrong move!")
#     elif player1.current_room =="outside" and direction == "w":
#         print("Wrong move!")
#     if direction == "q":
#         print("Not a valid direction!")
#         exit()  


       
# if parent is "mother":
#     print("She is beautiful")
#     if hair is "brown":
#         print()
# elif parent is "stepmother":
#     print("something")
# else:
