from game_state.cell import Cell
from api.engine import Engine
from game_state.move import Move
from game_state.player import Player


# Main, Driver code
class Main:
    # main class constructor
    def __init__(self) -> None:
        # Initialize the game engine
        self.engine = Engine()
        print("RSG_AI_Engine (v1.0.0) initialize successfully.")

        # start the 'TicTacToe' game
        print("TicTacToe is chosen as the game to be played.")
        self.board = self.engine.start(game_name="tic_tac_toe")

        # Initialize the two players
        self.player1 = Player(first=True)
        self.player2 = Player(first=False)
        print("User is player1 and plays with 'X'. RSG_AI_Engine (v1.0.0) is player2 and plays with 'O'")
    
    # Play the game
    def main(self):
        move_number = 1
        while (not self.engine.is_complete(board=self.board).get_completed()):
            
            # user move
            # only play the move if it is valid
            isvalid_curr_player_move = False
            while not isvalid_curr_player_move:
                # validity check 1
                try:
                    user_row = int(input("Select row to place X ::: "))
                    user_col = int(input("Select column to place X ::: "))
                except ValueError as err:
                    print("Err05 ::: " + "Please enter only 1 integer value (0, 1, or 2)")
                    continue
                except Exception as err:
                    print("Err05 ::: " + str(err))
                    continue
                # validity check 2
                if 0 > user_row  or  user_row >= 3 or 0 > user_col or user_col >= 3:
                    print("Err05 ::: Please make sure that the entered row and column values lie between 0 and 2 (Inclusive).")
                    continue
                # validity check 3
                curr_player1_move = Move(Cell(row=user_row, col=user_col))
                isvalid_curr_player_move, msg = self.board.check_valid(potential_move=curr_player1_move)
                if isvalid_curr_player_move:
                    self.engine.move(board=self.board, player=self.player1, current_move=curr_player1_move)
                    self.board.display_board(move_number=move_number, player_numer=1, board=self.board)
                else:
                    print("Err05 ::: " + msg)

            # engine move
            # if player1 hasn't won, player2 can make a move
            if not self.engine.is_complete(board=self.board).get_completed():
                curr_player2_move = self.engine.find_move(player=self.player2, board=self.board)
                # computer move will always be valid
                self.board.check_valid(potential_move=curr_player2_move)
                self.engine.move(self.board, self.player2, current_move=curr_player2_move)
                self.board.display_board(move_number=move_number, player_numer=2, board=self.board)
            
            # keep track of move number
            move_number += 1

        # Display the game result
        result = self.engine.is_complete(board=self.board)
        print(f'Game Completed ::: {result.get_completed()}, Winner ::: {result.winner}')

driver = Main()
driver.main()
