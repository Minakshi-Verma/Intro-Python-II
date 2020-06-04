from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}

print(room['outside'].name)
print(room['foyer'].description)


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Ronnie', 'outside')
# print(player1.name)
# print(player1)

# Write a loop that:#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print("Player current location:,", {player1.current_room})
    #  '\n' "Player's current room description: ", {room['outside'].description})
  
    direction = input("enter direction: ") 
     
    if player1.current_room =="outside" and direction == "north":        
        print("you reached the 'Foyer'!")
        player1.current_room ="foyer"
        
        if player1.current_room =="foyer" and direction == "south":
            print("You are back to 'Outside'!")
            # player1.current_room ="outside"

        elif player1.current_room =="foyer" and direction == "north":
            print("You reached 'Overlook!")
            player1.current_room ="overlook"

            if player1.current_room =="overlook" and direction == "south":
                print("You reached 'Foyer!")
                # player1.current_room ="foyer"

            elif player1.current_room =="overlook" and direction == "north":
                print("Wrong move!")
            elif player1.current_room =="overlook" and direction == "east":
                print("Wrong move!")
            elif player1.current_room =="overlook" and direction == "west":
                print("Wrong move!")
        elif player1.current_room =="foyer" and direction == "east":
            print("You are now in room 'Narrow'!")
            player1.current_room ="narrow"

            if player1.current_room =="narrow" and direction == "west":
                print("You reached 'Foyer!")
                # player1.current_room ="foyer"

            elif player1.current_room =="narrow" and direction == "east":
                print("Wrong move!")
            elif player1.current_room =="narrow" and direction == "north":
                print("You reached 'Treasure'!")
                # player1.current_room ="tresure"

                if player1.current_room =="treasure" and direction == "south":
                    print("You are back to 'Narrow'!")
                    # player1.current_room ="narrow"

                elif player1.current_room =="treasure" and direction == "north":
                    print("Wrong move!")
                elif player1.current_room =="treasure" and direction == "west":
                    print("Wrong move!")
                elif player1.current_room =="treasure" and direction == "east":
                    print("Wrong move!")
            elif player1.current_room =="narrow" and direction == "south":
                print("Wrong move!")
        elif player1.current_room =="foyer" and direction == "west":
            print("invalid move!")
    elif player1.current_room =="outside" and direction == "south":
        print("Wrong move!")
    elif player1.current_room =="outside" and direction == "east":
        print("Wrong move!")
    elif player1.current_room =="outside" and direction == "west":
        print("Wrong move!")
    if direction == "q":
        print("You quit the game")
        exit()  


       
