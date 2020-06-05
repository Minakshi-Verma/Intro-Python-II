# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.connections ={
            "n": n_to,
            "s": s_to,
            "w": w_to,
            "e": e_to
        }
        self.items = items 
      
       
             
    
    # def add_items(self, item):
    #     
    #     self.items.append(avail_item)








