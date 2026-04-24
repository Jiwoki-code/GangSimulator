class Item:

    def __init__(self, name = "unnamed_item", price = 0, quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity


# Classes d'items qui héritent ET qui ont d'autres properties en +

class Weapon(Item):

    def __init__(self):
        self.damage = 0
        self.discretion = 0