from game_state.cell import Cell

# This holds the move class
class Move:
    # The move constructor
    def __init__(self, cell: Cell) -> None:
        #Associate a move with a cell
        self.cell = cell
    
    def get_cell(self) -> Cell:
        return self.cell
    

