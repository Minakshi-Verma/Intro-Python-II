# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room

class Player:
    def __init__(self, name, current_room, avail_items=None):
        self.name = name
        self.current_room = current_room        
        self.avail_items = []
    
    def move(self,direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else:
            print("You cannot proceed in that direction!")

    def add_items(self, item):
        avail_item = add_item(self, item)
        self.avail_items.append(avail_item)
            

    # def add_items(self, item):
    #     addon = add_items(item)
    #     self.addons.append(addon)

# instance of class player
player1 = Player('Ronnie', 'outside')
player2 = Player('Ben', 'outside')


# print(player1.name)
# print(player2.name)