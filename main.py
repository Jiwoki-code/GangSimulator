import os
from game.game import Game
from game.places import Place
from game.items import Item

# Main

def main():
    os.system("clear")
    game = Game() # Init nouvelle instance de Game
    game.seed() # Crée les instances et trucs randoms nécessaires pour faire jouer ou débug
    game.game_loop() # Lance la loop dans l'instance

if __name__ == "__main__":
    main()