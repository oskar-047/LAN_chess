from .board import Board
import copy
from game.utils import get_color
from game.rules import check_legality
from game.generator.generator_handler import generator_handlers
from game.generator.pawn import generate_pawn_moves
from game.generator.queen import generate_queen_moves
from game.generator.rook import generate_rook_moves
from game.generator.knight import generate_knight_moves
from game.generator.king import generate_king_moves
from game.generator.bishop import generate_bishop_moves

#  the function will only receive the info of the click and will with all the other backend funcstionsmanage what to do, when it have a result will send the new board status and a int var indicating the action to do, like, 1 = only move, 2= ilegal move, 3=pawn promting, 4= checkamte and so on

# Input: clicked coordinates.
# Processing: internal logic decides what happened.
# Output: new board state + integer action code.

game = Board()

def tile_clicked(row: int, col: int):

    # Saves the piece
    piece = game.get_piece(row, col)
    # Saves the color of the piece
    piece_color = get_color(row, col, game.board)

    # If the clicked piece is not same color as the current turn, it will not do anything
    if piece_color and game.turn != piece_color:
        print("AAAAAAAAAAAAAAAAAAAAA")
        return


    # --- MOVEMENT LOGIC ---
    # Checks if the clicked square its a possible move
    if game.possible_moves and game.possible_moves[row][col] == 1:

        capturing = True if game.board[row][col] != 0 else False

        sel_row, sel_col = game.selected_piece

        # Runs the move logic
        move_piece(game, (sel_row, sel_col), (row, col))

        # If is eating it means the var "piece" is not 0, that's why it won't trigger the if below and have to reset now
        if capturing:
            game.reset_selected_piece()
            return

    # If the click is in an empty square it will deselect the piece
    if piece == 0:
        game.reset_selected_piece()
        return
    

    # --- SELECT PIECE LOGIC ---
    

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

        



# Piece movement function
def move_piece(game, from_pos, to_pos):

    # Save the pieces pos
    sel_row, sel_col = from_pos
    row, col = to_pos

    # Saves the board before the move is donde, for later check if the move was ilegal and have to return to the previous position
    game.previous_board = copy.deepcopy(game.board)

    # Updates the piece on the clicked square
    game.board[row][col] = game.board[sel_row][sel_col]

    # Removes the piece from the previous square
    game.board[sel_row][sel_col] = 0

    game.change_turn()

    ilegal_move = check_legality(game.board, game.turn)
    if not ilegal_move:
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        print("THE MOVEMENTE WAS ILEGAL")
        game.reset_move()

# Creates a new game and return the board to the frontend
def create_new_game():
    global game
    game = Board()

def get_game_board():
    return game.board

def get_game_posible_moves():
    return game.possible_moves