from .board import Board
from utils import get_color

#  the function will only receive the info of the clic and will with all the other backend funcstionsmanage what to do, when it have a result will send the new board status and a int var indicating the action to do, like, 1 = only move, 2= ilegal move, 3=pawn promting, 4= checkamte and so on

# Input: clicked coordinates.
# Processing: internal logic decides what happened.
# Output: new board state + integer action code.

game = Board()

generator_handlers = {
    1: generate_pawn_moves,    # white pawn
    2: generate_rook_moves,    # white rook
    3: generate_knight_moves,  # white knight
    4: generate_bishop_moves,  # white bishop
    5: generate_queen_moves,   # white queen
    6: generate_king_moves,    # white king

    11: generate_pawn_moves,    # black pawn
    12: generate_rook_moves,    # black rook
    13: generate_knight_moves,  # black knight
    14: generate_bishop_moves,  # black bishop
    15: generate_queen_moves,   # black queen
    16: generate_king_moves,    # black king
}

def tile_clicked(row: int, col: int):

    # If there is no selected piece
    if(game.selected_piece is None):
        # Select a piece
        game.selected_piece = (row, col)

        piece = board.get_piece(row, col)
        if(piece != 0):
            color = get_color(row, col, game.board)
            game.possible_moves = generator_handlers[piece](row, col, board, color)
        





# Creates a new game and return the board to the frontend
def create_new_game():
    global game
    game = Board()

def get_game_board():
    return game.board

def get_game_posible_moves():
    return game.possible_moves