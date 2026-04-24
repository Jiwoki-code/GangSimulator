class Place:

    def __init__(self, name = "Some place", place_type = "General", reputation = 50, current_visitors = 0, max_visitors = 100, boss = "None", current_value = 1000, gains = 0, rent = 100, items = []):
        self.name = name
        self.type = place_type
        self.reputation = reputation
        self.current_visitors = current_visitors
        self.max_visitors = max_visitors
        self.boss = boss
        self.current_value = current_value
        self.gains = gains
        self.rent = rent
        self.items = items
        # Je mets pas howmany items car ça se déduit avec la longueur de l'array

    def get_place_info(self):
        print(self.name, "| Boss:", self.boss, "| Valeur:", self.current_value)