from game.utils import get_color, find_king
from game.generator.generator_handler import generator_handlers
from game.generator.pawn import generate_pawn_moves
from game.generator.queen import generate_queen_moves
from game.generator.rook import generate_rook_moves
from game.generator.knight import generate_knight_moves
from game.generator.king import generate_king_moves
from game.generator.bishop import generate_bishop_moves


piece_data = {
    "pawn": [1, 11, 1, 11, False],
    "bishop": [4, 14, 5, 15, True],
    "rook": [2, 12, 5, 15, True],
    "knight": [3, 13, 3, 13, False],
    "king": [6, 16, 6, 16, False]
}

# Script for check game rules like check, ilegal moves and more

def check_legality(board, turn, game):

    # Get the king pos (It gets the enemy king of the actual turn to check if the color of the actual turn its atacking the enemy king)
    king_pos = game.black_king_pos if turn == "white" else game.white_king_pos

    is_king_atacked = square_is_atacked_by(board, king_pos, turn)
    return not is_king_atacked



# This function will check if any piece of {atacker_color} color is atacking the {square} position
def square_is_atacked_by(board, square, atacker_color):
    moves_dir = [
        [1, 0, "rook"], # bottom center
        [-1, 0, "rook"], # top center        
        [0, 1, "rook"], # center right
        [0, -1, "rook"], # center left        
        [1, 1, "bishop"], # bottom right
        [-1, 1, "bishop"], # top right
        [-1, -1, "bishop"], # top left
        [1, -1, "bishop"], # bottom left
        [1, 0, "king"], # bottom center
        [-1, 0, "king"], # top center        
        [0, 1, "king"], # center right
        [0, -1, "king"], # center left        
        [1, 1, "king"], # bottom right
        [-1, 1, "king"], # top right
        [-1, -1, "king"], # top left
        [1, -1, "king"], # bottom left
        [2, 1, "knight"], # bottom right
        [2, -1, "knight"], # bottom left
        [-2, 1, "knight"], # top right
        [-2, -1, "knight"], # top left
        [-1, 2, "knight"], # right top
        [1, 2, "knight"], # right bottom
        [-1, -2, "knight"], # left top
        [1, -2, "knight"], # left bottom
        [0, -1, "pawn"], # bottom left
        [0, 1, "pawn"], # bottom right
    ]

    # Checks rook/queen atacks
    if check_atack(board, moves_dir, square, atacker_color):
        return True
    else:
        return False
    
def check_atack(board, directions, square, atacker_color):

    start_row, start_col = square

    for row_move, col_move, piece_type in directions:
        

        # Checks if the piece have infinite movement (slider)
        infinite = piece_data[piece_type][4]

        # If its a pawn it checks if it have to go up or down (1==down, -1==up)
        if piece_type == "pawn":
            row_move = 1 if atacker_color == "white" else -1
            print("ROW POS: " + str(row_move))
            print("BALBALBALBALBFJBL")
        

        # Saves the new position
        new_row = start_row + row_move
        new_col = start_col + col_move
        


        while 0 <= new_row < 8 and 0 <= new_col < 8:
            piece = board[new_row][new_col]

            # [:-1] its for slicing the last element because all elements are int but the last is a bool
            if is_enemy(piece, atacker_color) and piece in piece_data[piece_type][:-1]:
                return True

            # If a piece is hit the while stops
            if piece != 0:
                break
            
            if not infinite:
                break

            new_row += row_move
            new_col += col_move


def is_enemy(piece, atacker_color):
    if 0 < piece < 10 and atacker_color == "white":
        return True
    elif piece > 10 and atacker_color == "black":
        return True
    else:
        return False




# --- PREVIOUS LEGALITY CHECK ---
# def check_legality(board, turn):
#     white_squares_attacked, black_squares_attacked = get_atacked_squares(board)

#     white_king_row, white_king_col = find_king("white", board)
#     black_king_row, black_king_col = find_king("black", board)

#     if (
#         (turn == "white" and white_squares_attacked[black_king_row][black_king_col] == 1)
#         or
#         (turn == "black" and black_squares_attacked[white_king_row][white_king_col] == 1)
#     ):
#         return True
#     else:
#         return False

# def get_atacked_squares(board):
#     # Create an empty 8x8 2D array
#     white_squares_attacked = [[0] * 8 for _ in range(8)]
#     black_squares_attacked = [[0] * 8 for _ in range(8)]

    
#     for row in range(8):
#         for col in range(8):
#             piece = board[row][col]

#             if piece == 0: continue

#             piece_color = get_color(row, col, board)

#             squares_atacked = white_squares_attacked if piece_color == "white" else black_squares_attacked

#             piece_atack = generator_handlers[piece](row, col, board, piece_color)

#             merge_arrays(squares_atacked, piece_atack, 1)

#     return white_squares_attacked, black_squares_attacked



# def merge_arrays(array1, array2, value_to_merge):
#     for row in range(8):
#         for col in range(8):
#             if array2[row][col] == value_to_merge:
#                 array1[row][col] = array2[row][col]