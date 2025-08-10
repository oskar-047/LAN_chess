import copy

class Board:
    def __init__(self):
        self.board = self._init_board()
        self.previous_board = None # Saves the previous board if a ilegal move is donde
        self.turn = "white"
        self.selected_piece = None # Indicates which piece is selected
        self.possible_moves = [[0] * 8 for _ in range(8)]
        self.full_moves = 1
        self.halfmove_clock = 0 # It increases in each move when there are no captures and none pawn has moved, if a pawn is moved or a capture is made, it resets to 0; if it reaches 100, either player can claim draw
        self.white_kingside_castle = True
        self.white_queenside_castle = True
        self.black_kingside_castle = True
        self.black_queenside_castle = True


    # Inits a defualt chess board
    def _init_board(self):
        return [
            [12, 13, 14, 15, 16, 14, 13, 12],
            [11, 11, 11, 11, 11, 11, 11, 11],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 5, 6, 4, 3, 2],
        ]

        # white: 1=pawn, 2=rook, 3=Knight, 4=bishop, 5=queen, 6=king
        # black: 11=pawn, 12=rook, 13=Knight, 14=bishop, 15=queen, 16=king


    def get_piece(self, row, col):
        return self.board[row][col]


    def set_piece(self, row, col, piece):
        self.board[row][col] = piece


    def move_piece(self, src_row, src_col, dest_row, dest_col):
        self.board[dest_row][dest_col] = self.board[src_row][src_col]
        self.board[src_row][src_col] = 0

    def reset_selected_piece(self):
        self.selected_piece = None
        self.possible_moves = [[0] * 8 for _ in range(8)]

    def change_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

    def reset_move(self):
        self.board = copy.deepcopy(self.previous_board)
        self.change_turn()