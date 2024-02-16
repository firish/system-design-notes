# This holds the gameresult

# GameResult object holds the status of a game and the winner of the game
class GameResult:
    def __init__(self, is_over: bool, winner: str) -> None:
        self.is_over = is_over
        self.winner = winner
    
    def get_completed(self):
        return self.is_over