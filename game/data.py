import json

class Data:

    def names(self):
        NAMES_DATA = [] # En majuscule car variable globale
        with open("data/names.JSON") as json_file:
            NAMES_DATA = json.load(json_file)
        return NAMES_DATA

    def items(self):
        ITEMS_DATA = [] # En majuscule car variable globale
        with open("data/items.JSON") as json_file:
            ITEMS_DATA = json.load(json_file)
        return ITEMS_DATA