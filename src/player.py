# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room

class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room        
        self.items = items if items is not None else []
    
    def __str__(self):
        return f"This is {self.name}, they are located in {self.current_room}"
    
    def move(self,direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else:
            print("You cannot proceed in that direction!")

    def get_items(self):                  
        choose_item = input(f'Please choose the item you wish: {self.current_room.items}').split(',')
        for itm in choose_item: 
            self.items.append(choose_item)
            print(f'you selected {self.items}')
            
    def drop_items(self):
        select_item = input(f'Please choose the item you wish to remove: {self.items}').split(',')
        for item in select_item:
            self.items.pop(select_item)
            print(f'This is your new list {self.items}')


# instance of class player
player1 = Player('Ronnie', 'outside', ('sword'))



# print(player1.name)
# print(player2.name)