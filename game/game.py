from . import actions
from game.places import Place
from game.items import Item
import random
import os

class Game:

    def __init__(self):
        self.current_money = 1000
        self.total_rent = 75
        self.gains = 0
        self.posible_actions = []
        self.items = []
        self.day = 0
        self.places = []

    def seed(self): # Pour générer la game et tester des trucs
        
        random_market = actions.generateBlackMarket()
        random_market.get_place_info() # Print les infos sur le market
        self.places.append(random_market)
        self.items.append(Item("Etron", 0))
        self.posible_actions = ["Sortir", "Créer de la drogue", "Dealer"]
        
        # generateRandomItem()
        
    def game_loop(self):
        while not self.isGameOver():
            os.system("clear")
            self.day += 1
            print("Le jours " + str(self.day) + " à commencé.")
            self.calculateMoney()
            self.show_inventory()
            self.inputmanager()
            input("Appuyez sur une touche pour continuer...")

    def show_inventory(self):
        print("\n-- INVENTAIRE --")
        for item in self.items:
            print(item.name + " | q : " + str(item.quantity) + " | prix (u) : " + str(item.price) +  " | prix total : " + str(item.price * item.quantity))

    def isGameOver(self):
        if self.current_money <= 0:
            print("Vous avez fait faillite !")
            print("Game Over !")
            return True

    def calculateMoney(self):
        total_yield = self.gains - self.total_rent
        self.current_money += total_yield

        print("Vos loyers s'élève à " + str(self.total_rent) + "$")
        print("Vos gains s'élève à " + str(self.gains) + "$")
        print("Le rendement total de vos biens est de " + str(total_yield) + "$")
        print("Vous possedez maintenant " + str(self.current_money) + "$")

    def inputmanager(self):
        print("\nChoisissez une action :")
        loop = 0
        for i in self.posible_actions:
            loop += 1
            print(str(loop) + " - " + str(i))
        commande = input("Vous: ")
        # commande = str(2) # pour debut vite
        match commande:
            case "1":
                print("Vous sortez dehors")
            case "2":
                self.addItems(actions.createDrugs())
            case "3":
                print("Vous Dealez")
            case _:
                print("Action non reconnue")

    def addItems(self, item):
        already_exists = False
        for existing_item in self.items:
            if existing_item.name == item.name:
                already_exists = True
                break
        if already_exists:
            existing_item.quantity += item.quantity
            print("Vous ajoutez " + str(item.quantity) + "g de drogue à votre stock.")
        else:
            self.items.append(item)
        print("Vous possédez maintenant " + str(existing_item.quantity) + "g de drogue.")