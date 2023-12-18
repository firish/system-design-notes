# The objective
# Create a turn-taking AI Engine
# This AI engine should be able to play any turn-taking two player game
# Like Chess, Othello, Tic-Tac-Toe, 
# It is a truly open-ended question with hazy requirements at best

class Engine:

    # Start a new game by creating a new board for the game
    def start():
        return Board()
    
    # Perform a move on the board
    def move(board, player, current_move):
        pass

    # Check if the game has been won
    def is_complete(board):
        if board.isinstance(TicTacToeBoard):
            # check for victory through a completed row
            for row in range(0, 3):
                is_row_complete = True
                first_symbol = board.cells[row][0]
                for col in range(1, 3):
                    if board.cells[row][col] != first_symbol:
                        is_row_complete = False
                        break
                if is_row_complete:
                    return GameResult(True, first_symbol)
            
            # check for victory through a completed col
            for col in range(0, 3):
                is_col_complete = True
                first_symbol = board.cells[col][0]
                for row in range(1, 3):
                    if board.cells[row][col] != first_symbol:
                        is_col_complete = False
                        break
                if is_col_complete:
                    return GameResult(True, first_symbol)
            
            # check for victory through a completed diagonal
            is_pos_diag_complete = True
            first_symbol = board.cells[0][0]
            for row in range(1, 3):
                if board.cells[row][row] != first_symbol:
                    is_pos_diag_complete = False
            if is_pos_diag_complete:
                return GameResult(True, first_symbol)
            
            is_neg_diag_complete = True
            first_symbol = board.cells[0][2]
            for row in range(1, 3):
                if board.cells[row][2 - row] != first_symbol:
                    is_neg_diag_complete = False
            if is_neg_diag_complete:
                return GameResult(True, first_symbol)
            
            # If there is no victory so far, check for a tie
            is_tie = True
            moves = 0
            for row in range(3):
                for col in range(3):
                    if board.cell[row][col] != '.':
                        moves += 1
            if moves == 9:
                is_tie = False
            if is_tie:
                return GameResult(False, "Tie")
            
            # if there is no victory, or no tie, then the game is still incomplete
            return GameResult(False, "Incomplete")

        elif board.isinstance(ChessBoard):
            # Mock calculations
            return GameResult(True, "GameResult")
        else:
            # Othello Board
            # Mock Calculations
            return GameResult(True, "GameResult")


class Board:
    pass

class Player:
    pass

class Move:
    pass


# GameResult object holds the status of a game and the winner of the game
class GameResult:
    def __init__(self, is_over, winner):
        self.is_over = is_over
        self.winner = winner


# Lets create game boards for the engine
# TicTacToe is the actual example we will work with
# chess and othello are mock boards
class TicTacToeBoard(Board):
    cells = [["." for _ in range(3)] for _ in range(3)]

class ChessBoard(Board):
    cells = [["." for _ in range(8)] for _ in range(8)]

class OtheloBoard(Board):
    cells = [["." for _ in range(8)] for _ in range(8)]