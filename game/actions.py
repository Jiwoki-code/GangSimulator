import random
from game.data import Data
from game.items import Item
from game.places import Place

def generateBlackMarket():
    name = random.choice(Data().names()["black_market_names"])
    boss = 'boss'
    gains = random.randint(5, 20)
    current_value = random.randint(10, 100)
    rent = random.randint(1, 10)
    reputation = random.randint(1, 50)
    items = [generateRandomItem() for i in range(random.randint(3, 5))]
    return Place(name=name, place_type="black_market", reputation=reputation, current_visitors=0, max_visitors=0, boss=boss, current_value=current_value, gains=gains, rent=rent, items=items)

def generateRandomItem():
    name = random.choice(Data().items()["items"])
    price = random.randint(100, 1000)
    return Item(name, price)

def createDrugs():
    print("Vous passez la journée à faire de la drogue")
    product_quantity = random.randrange(2, 5)
    print("Vous produisez " + str(product_quantity) + "g de drogue bien dure !")
    print("des vapeurs toxiques s'échappent de votre planque ..")
    item = Item("Drugs", 10, product_quantity)
    return item
