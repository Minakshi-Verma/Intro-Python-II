class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description 

#create instances of class Item

item_1 = Item('Key', 'You can open the treasure box!')
item_2 = Item("Sword", "You can kill the monsters!")
item_3 = Item("Flashlight", "You can see in the dark")
item_4 = Item("Backpack", "You might need this to carry your newly found treasure!")
item_5 = Item("Lightsaber", "You got special powers!")
item_6 = Item("Hat", "You got a swag, keep it safe!")
item_7 = Item("Nail", "You can hang your swag here!")
item_8 = Item("Hammer", "You will need this to put your nail on the wall!")


print(item_1.name)