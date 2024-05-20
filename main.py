from studentA import print_board, is_game_over, new_board, announce_outcome
from studentB import ai_move, get_user_move, is_player_starting

board = new_board()
player_move = is_player_starting()
while not is_game_over(board):
    print_board(board)
    board = player_move and get_user_move(board) or ai_move(board)
    player_move = not player_move 

announce_outcome(board, player_move)
