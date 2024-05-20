PLAYER_MARK = 1
AI_MARK = 2
# [y*5+x]

def get_index(x, y):
    return y*5+x

def new_board():
    board = [0 for x in range (0, 25)]
    return board


def print_board(board):
    for y in range(0, 5):
        for x in range(0, 5):
            to_print = "[ ]"
            value = board[get_index(x,y)]
            to_print = "[X]" if value == 1 else to_print
            to_print = "[O]" if value == 2 else to_print
            print(to_print, end='')
        print("")

def is_game_over(board): 
    #1. Check horizontal 
    for y in range(0, 5):
        for x in range(0,3):
            init_value = board[get_index(x,y)]
            if board[get_index(x+1, y)] == init_value and \
            board[get_index(x+2, y)] == init_value:
                return True
    #2. Check vertical
    for x in range(0, 5):
        for y in range(0, 3):
            init_value = board[get_index(x,y)]
            if board[get_index(x, y+1)] == init_value and \
            board[get_index(x, y+2)] == init_value:
                return True
    #3. Check \ axis
    for y in range(0, 3):
        for x in range(0,3):
            init_value = board[get_index(x,y)]
            if board[get_index(x+1, y+1)] == init_value and \
            board[get_index(x+2, y+2)] == init_value:
                return True
    #4. Check / axis
    for y in range(3, 5):
        for x in range(3,5):
            init_value = board[get_index(x,y)]
            if board[get_index(x-1, y-1)] == init_value and \
            board[get_index(x-2, y-2)] == init_value:
                return True
    return True

def announce_outcome(board, player_move):
    if player_move:
        print("AI is victorious")
    else:
        print("Humanity triumphs once again")

# [][][][][]
# [][][][][]
# [][][][][]
# [][][][][]
# [][][][][]
