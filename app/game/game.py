from .board import Board
from game.utils import get_color
from game.generator.pawn import generate_pawn_moves
from game.generator.queen import generate_queen_moves
from game.generator.rook import generate_rook_moves
from game.generator.knight import generate_knight_moves
from game.generator.king import generate_king_moves
from game.generator.bishop import generate_bishop_moves

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

    piece = game.get_piece(row, col)


    # MOVEMENT LOGIC
    if game.possible_moves and game.possible_moves[row][col] == 1:

        is_eating = True if game.board[row][col] != 0 else False

        sel_row, sel_col = game.selected_piece

        game.board[row][col] = game.board[sel_row][sel_col]
        game.board[sel_row][sel_col] = 0

        # If is eating it means the var "piece" is not 0, that's why it won't trigger the if below and have to reset now
        if is_eating:
            game.reset_move()
            return

    # If the clic is in an empty square it will deselect the piece
    if piece == 0:
        game.reset_move()
        return
    
    # Saves the color of the piece
    piece_color = get_color(row, col, game.board)

    # If there isn't a piece selected, its marks the actual square piece as selected
    if game.selected_piece is None:
        game.selected_piece = (row, col)

    else:
        # If a piece is already selected it saves the selected piece color and position(not the actual)
        sel_row, sel_col = game.selected_piece
        sel_color = get_color(sel_row, sel_col, game.board)

        # In case the clicked piece is a different color from the actual selected piece, it won't do anything
        if piece_color != sel_color:
            return
        
        # But in case the clicked piece is the same color, the clicked piece will be the new selected piece
        game.selected_piece = (row, col)      

    # Generats the posible moves
    game.possible_moves = generator_handlers[piece](row, col, game.board, piece_color)

        





# Creates a new game and return the board to the frontend
def create_new_game():
    global game
    game = Board()

def get_game_board():
    return game.board

def get_game_posible_moves():
    return game.possible_moves