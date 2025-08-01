from .board import Board
from game.utils import get_color
from game.generator.pawn import generate_pawn_moves

#  the function will only receive the info of the clic and will with all the other backend funcstionsmanage what to do, when it have a result will send the new board status and a int var indicating the action to do, like, 1 = only move, 2= ilegal move, 3=pawn promting, 4= checkamte and so on

# Input: clicked coordinates.
# Processing: internal logic decides what happened.
# Output: new board state + integer action code.

game = Board()

generator_handlers = {
    1: generate_pawn_moves,    # white pawn
    # 2: generate_rook_moves,    # white rook
    # 3: generate_knight_moves,  # white knight
    # 4: generate_bishop_moves,  # white bishop
    # 5: generate_queen_moves,   # white queen
    # 6: generate_king_moves,    # white king

    11: generate_pawn_moves,    # black pawn
    # 12: generate_black_rook_moves,    # black rook
    # 13: generate_black_knight_moves,  # black knight
    # 14: generate_black_bishop_moves,  # black bishop
    # 15: generate_black_queen_moves,   # black queen
    # 16: generate_black_king_moves,    # black king
}

def tile_clicked(row: int, col: int):

    piece = game.get_piece(row, col)
    if piece == 0:
        game.reset_move()
        return
    

    piece_color = get_color(row, col, game.board)

    if game.selected_piece is None:
        game.selected_piece = (row, col)

    else:
        
        sel_row, sel_col = game.selected_piece
        sel_color = get_color(sel_row, sel_col, game.board)

        # In case the clicked piece is a different color from the actual selected piece, it won't do anything
        if piece_color != sel_color:
            return
        
        # But in case the clicked piece is the same color, the clicked piece will be the new selected piece
        game.selected_piece = (row, col)      

    game.possible_moves = generator_handlers[piece](row, col, game.board, piece_color)

        





# Creates a new game and return the board to the frontend
def create_new_game():
    global game
    game = Board()

def get_game_board():
    return game.board

def get_game_posible_moves():
    return game.possible_moves