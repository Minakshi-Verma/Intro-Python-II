# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, avail_items=None):
        self.name = name
        self.description = description
        self.connections ={
            "n": n_to,
            "s": s_to,
            "w": w_to,
            "e": e_to
        }
        self.avail_items = []
       
             
    
    # def add_items(self, item):
    #     avail_item = add_item(self, item)
    #     self.avail_items.append(avail_item)

#create instances of Room

# outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
# foyer = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")
# overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
# narrow = Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.")
# treasure = Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")


# print(overlook.name)







#  def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
#         self.name = name
#         self.description = description
#         self.n_to = n_to
#         self.s_to = s_to
#         self.e_to = e_to
#         self.w_to = w_to
#         self.avail_items = []


