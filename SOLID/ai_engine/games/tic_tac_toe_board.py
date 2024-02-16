from game_state.board import Board
from game_state.cell import Cell
from game_state.move import Move
from game_state.player import Player


class TicTacToeBoard(Board):
    # class constructor
    def __init__(self):
        # defining the board
        self.cells = [["." for _ in range(3)] for _ in range(3)]
        print("TicTacToe board has been successfully initialized.")

        # storing all the moves associated with the board
        self.used_cells = [[False for _ in range(3)] for _ in range(3)]

    # getter-setter for board cell
    def get_cell(self, row: int, col: int) -> str:
        return self.cells[row][col]
    
    def set_cell(self, symbol: str, cell: Cell) -> None:
        self.cells[cell.get_row()][cell.get_col()] = symbol

    # check if a move being made is valid
    def check_valid(self, potential_move: Move)-> tuple: # (bool, str)
        cell = potential_move.get_cell()
        # check if the move is not trying to overwrite an existing move
        if not self.used_cells[cell.get_row()][cell.get_col()]:
            self.used_cells[cell.get_row()][cell.get_col()] = True
            return (True, '')
        else:
            return (False, "The row and column entered have already been used.")
        
    
    # func to display the current board
    def display_board(self, move_number: int, player_numer: int, board: Board) -> None:
        print(f'After move_numer {move_number}, by player {player_numer}, the board looks as follow ::: ')
        for row in range(0, 3):
            for col in range(0, 3):
                curr_cell = self.get_cell(row=row, col=col)
                print(curr_cell, end='')
            print("")
        print("")


