import random

items = ITEMS_DATA["items"]
black_market_names = NAMES_DATA["black_market_names"]

class black_market:
    def __init__(self, name, boss, reputation, current_value, gains, rent, items, howManyItem):
        self.name = name
        self.boss = boss
        self.reputation = reputation
        self.current_value = current_value
        self.gains = gains
        self.rent = rent
        self.items = items
        self.howManyItem = howManyItem

class item:
    def __init__(self, name = 'Objet non reconnu', price = 0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

def generateRandomItem():
    name = random.choice(items)
    price = random.randint(100, 1000)
    return item(name, price)

generateRandomItem()

def generateBlackMarket():
    name = random.choice(black_market_names)
    boss = 'boss'

    gains = random.randint(5, 20)
    current_value = random.randint(10, 100)
    rent = random.randint(1, 10)
    reputation = random.randint(1, 50)
    howManyItem = random.randint(3, 5)
    items = [generateRandomItem() for i in range(howManyItem)]
    return black_market(name, boss, current_value, reputation, gains, rent, items, howManyItem)

caca = generateBlackMarket()

print(caca.name, caca.boss, caca.current_value, caca.reputation,'gains :', caca.gains, caca.rent, caca.howManyItem)
for a in caca.items:
    print(a.name, a.price)