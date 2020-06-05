from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance","North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.",["key","sword", "flashlight"]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", ["hammer","flashlight"]),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", ["nail","key"]),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", ["sword","flashlight", "hammer"]),
}

# print(room['outside'].name)
# print(room['outside'].items)
# print(room['foyer'].items)


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
# print(player1.current_room.name)


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
    print(f'You are at: {player1.current_room.name}')
    # print(player1.current_room.items)
    # print(player1.current_room.description)
    for line in textwrap.wrap(player1.current_room.description, width = 30):
        print(line)
    direction_input = input("Enter direction(s/n/e/w) first AND then type 'myGear: ")  
    # print(f'You are in {player1.current_room.name}')     
    if direction_input in "myGear":
        player1.get_items()
    if direction_input in "dropItem":
        player1.drop_items()
    if direction_input in ["n", "s", "e", "w"]:
        player1.move(direction_input)
    if direction_input in "quit":
        print("Thanks for playing. Goodbye!")
        user_is_playing = False    
else:
    print("Thanks for playing. Goodbye!")
    user_is_playing = False






