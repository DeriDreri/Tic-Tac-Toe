PLAYER_MARK = 1
AI_MARK = 2

class Board: 
    def __init__(self):
        self.board_list = [ 0 for x in range (0,24)]

    def markSpot(self, player_move, x, y):
        if self.board_list[y*5+x] == 0:
            self.board_list[y*5+x] = PLAYER_MARK if player_move else AI_MARK
            return True 
        return False


def new_board():
    return Board()

def print_board():
    pass 

def is_game_over():
    pass
