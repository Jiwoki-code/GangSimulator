import random
import places
import os


class game:
    def __init__(
        self, current_money=1000, total_rent=75, gains=0, posible_actions=[], items=[]
    ):
        self.current_money = current_money
        self.total_rent = total_rent
        self.gains = gains
        self.posible_actions = posible_actions
        self.items = items
