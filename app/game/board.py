class Board {
    def __init__(self):
        self.board = init_board()
        self.is_white_turn = True
        self.selected_piece = None # Indicates which piece is selected
        self.full_moves = 1
        self.halfmove_clock = 0 # It increases in each move when there are no captures and none pawn has moved, if a pawn is moved or a capture is made, it resets to 0; if it reaches 100, either player can claim draw
        self.white_kingside_castle = True
        self.white_queenside_castle = True
        self.black_kingside_castle = True
        self.black_queenside_castle = True


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


    def piece_at(self, row, col):
        return self.board[row][col]


    def set_piece(self, row, col, piece):
        self.board[row][col] = piece


    def move_piece(self, src_row, src_col, dest_row, dest_col):
        self.board[dest_row][dest_col] = self.board[src_row][src_col]
        self.board[src_row][src_col] = 0

}