FIRST_PLAYER = '|'
SECOND_PLAYER = '-'

WINNNING_BOARDS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

class State:
    def __init__(self) -> None:
        self.board = [''] * 9
        self.last_move = None

    def __is_cross(self, pos: int) -> True:
        return FIRST_PLAYER in self.board[pos] and SECOND_PLAYER in self.board[pos]
     
    def get_succesors(self, player: str):
        for i, pos in enumerate(self.board):
            if player not in pos and (self.last_move is None or self.last_move != i):    
                succesor = State()
                succesor.board = self.board[:]
                succesor.board[i] += player
                succesor.last_move = i

                yield succesor

    def eval(self) -> int:
        for board in WINNNING_BOARDS:            
            if all(self.__is_cross(pos) for pos in board):
                return 1
        return 0
    
    def has_succesors(self) -> bool:
        return self.eval() != 1