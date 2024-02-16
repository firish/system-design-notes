# This holds the player class

class Player:
    # the Player constructor
    def __init__(self, first: bool) -> None: 
        if first:
            self.symbol = 'X'
        else:
            self.symbol = 'O'
    
    def get_symbol(self) -> str:
        return self.symbol
    
