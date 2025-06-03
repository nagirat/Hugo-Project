import math
import random

class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter
        
    # we want all player to get their next move given a game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\"s turn. Input move (0-8: )")
            # we are going to check that this is a corret value by trying to cast
            # it to an integer, and if its not, than we say its invalid
            # if that is not avaible on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!!!
            except ValueError:
                print("Invalid Square. Try  again.")

        return val            
