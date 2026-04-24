import random
import places
import os 

class game:
    def __init__(self, current_money = 1000, total_rent = 75, gains = 0, posible_actions = [], items = []):
        self.current_money = current_money
        self.total_rent = total_rent
        self.gains = gains
        self.posible_actions = posible_actions
        self.items = items


gameinstance = game()

itemdebase = places.item('caca',0,0)
gameinstance.items.append(itemdebase)
gameinstance.posible_actions = ["Sortir", "Crée de la drogue", "Dealé"]

def isGameOver():
    if gameinstance.current_money <= 0:
        return True

def calculateMoney():
    total_yield = gameinstance.gains - gameinstance.total_rent
    gameinstance.current_money += total_yield

    print('Vos loyers s\'élève à ' + str(gameinstance.total_rent) + '$')
    print('Vos gains s\'élève à ' + str(gameinstance.gains) + '$')
    print('Le rendement total de vos biens est de ' + str(total_yield) + '$')
    print('Vous possedez maintenant ' + str(gameinstance.current_money) + "$")

def inputmanager():
    print('Choisissez une action :')
    loop = 0
    for i in gameinstance.posible_actions:
        loop += 1
        print(str(loop)+ ' - ' + str(i))
    
    commande = input()

    match commande:
        case '1':
            print('Vous sortez dehors')
        case '2':
            creatingDrugs()
        case '3':
            print('Vous Dealez')
        case _:
            print('Action non reconnue')

def addingItems(item):
    print('1')
    print(item)
    for existingitem in gameinstance.items:
        print('2')
        if existingitem.name == item.name:
            print('3')
            existingitem.quantity += item.quantity
            print('Vous ajouter' + str(item.quantity) + 'g de drogue à votre stock ..')
            print('Vous possèdez mtn ' + str(existingitem.quantity) + 'g de drogue')
        else:
            gameinstance.items.append(item)
            print('debug')

def creatingDrugs():
    print('Vous passez la journée à faire de la drogue')
    product = random.randrange(2,5)
    print('Vous produisez ' + str(product) + 'g de drogue bien dure !')
    print('des vapeurs toxiques s\'échappent de votre planque ..')
    item = places.item('Drugs', 10, product)
    print('0')
    addingItems(item)
    print('4')


# game loop
day = 0

while True:
    os.system('clear')
    day += 1
    print('Le jours ' + str(day) + ' à commencer')
    calculateMoney()
    if isGameOver():
        print('Vous avez fait faillite !')
        print("Game Over !")
        break

    inputmanager()

    input("Appuyez sur une touche pour continuer...")