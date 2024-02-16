# The objective
# Create a turn-taking AI Engine
# This AI engine should be able to play any turn-taking two player game
# Like Chess, Othello, Tic-Tac-Toe, 
# It is a truly open-ended question with hazy requirements at best

# Import classes
# List imports, and variable declarations/initializations alphabetically (ease of lookup and systematic)
from game_state.board import Board
from game_state.cell import Cell
from game_state.game_result import GameResult
from game_state.move import Move
from game_state.player import Player
from games.tic_tac_toe_board import TicTacToeBoard



class Engine:

    def __init__(self) -> None:
        pass

    # Start a new game by creating a new board for the game
    def start(self, game_name: str) -> TicTacToeBoard:
        if game_name == "tic_tac_toe":
            print("TicTacToe board initialization has started.")
            return TicTacToeBoard()
        else:
            raise TypeError("Err 01 ::: V1.0.0 of RSG_AI_Engine only supports TicTacToe")
    
    # Perform a move on the board
    def move(self, board: Board, player: Player, current_move: Move) -> None:
        # before making a move, check that you are making a move on supported boards
        if isinstance(board, TicTacToeBoard):
            curr_tictactoe_board = board
            curr_tictactoe_board.set_cell(player.get_symbol(), current_move.get_cell())
        else:
            raise TypeError("Err 02 ::: Tried making a move on a non TicTacToe Board")

    # Check if the game has been won
    def is_complete(self, board: Board) -> GameResult:
        if isinstance(board, TicTacToeBoard):
            # check for victory through a completed row
            for row in range(0, 3):
                is_row_complete = True
                first_symbol = board.get_cell(row=row, col=0)
                if first_symbol == ".":
                    return GameResult(is_over=False, winner='Incomplete')
                for col in range(1, 3):
                    if board.get_cell(row=row, col=col) != first_symbol:
                        is_row_complete = False
                        break
                if is_row_complete:
                    return GameResult(is_over=True, winner=first_symbol)
            
            # check for victory through a completed col
            for col in range(0, 3):
                is_col_complete = True
                first_symbol = board.get_cell(row=col, col=0)
                if first_symbol == ".":
                    return GameResult(is_over=False, winner='Incomplete')
                for row in range(1, 3):
                    if board.get_cell(row=row, col=col) != first_symbol:
                        is_col_complete = False
                        break
                if is_col_complete:
                    return GameResult(is_over=True, winner=first_symbol)
            
            # check for victory through a completed diagonal
            is_pos_diag_complete = True
            first_symbol = board.get_cell(row=0, col=0)
            if first_symbol == ".":
                    return GameResult(is_over=False, winner='Incomplete')
            for row in range(1, 3):
                if board.get_cell(row=row, col=row) != first_symbol:
                    is_pos_diag_complete = False
            if is_pos_diag_complete:
                return GameResult(is_over=True, winner=first_symbol)
            
            is_neg_diag_complete = True
            first_symbol = board.get_cell(row=0, col=2)
            if first_symbol == ".":
                    return GameResult(is_over=False, winner='Incomplete')
            for row in range(1, 3):
                if board.get_cell(row=row, col=2-row) != first_symbol:
                    is_neg_diag_complete = False
            if is_neg_diag_complete:
                return GameResult(is_over=True, winner=first_symbol)
            
            # If there is no victory so far, check for a tie
            is_tie = True
            moves = 0
            for row in range(3):
                for col in range(3):
                    if board.get_cell(row=row, col=col) != '.':
                        moves += 1
            if moves != 9:
                is_tie = False
            if is_tie:
                return GameResult(is_over=True, winner="Tie")
            
            # if there is no victory, or no tie, then the game is still incomplete
            return GameResult(is_over=False, winner='Incomplete')

        elif isinstance(board, ChessBoard):
            # Mock calculations
            return GameResult(True, "GameResult")
        else:
            raise TypeError("Err 03 ::: Unsupported board type encountered while checking game status (is_complete)")

    # find a game winning move
    def find_move(self, player: Player, board: Board) -> Move:
        # Naive solution, just return the first playable move
        curr_tictactoe_board = board
        for row in range(0, 3):
            for col in range(0, 3):
                if curr_tictactoe_board.get_cell(row=row, col=col) == ".":
                    return Move(Cell(row=row, col=col))
        # if no move exists, raise err
        raise Exception("Err04 ::: Can't find a legal move. [Internal logic error]")



# Lets create game boards for the engine
# TicTacToe is the actual example we will work with
# chess and othello are mock boards
class ChessBoard(Board):
    cells = [["." for _ in range(8)] for _ in range(8)]

class OtheloBoard(Board):
    cells = [["." for _ in range(8)] for _ in range(8)]