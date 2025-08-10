from game.utils import get_color, find_king
from game.generator.generator_handler import generator_handlers
from game.generator.pawn import generate_pawn_moves
from game.generator.queen import generate_queen_moves
from game.generator.rook import generate_rook_moves
from game.generator.knight import generate_knight_moves
from game.generator.king import generate_king_moves
from game.generator.bishop import generate_bishop_moves

# Script for check game rules like check, ilegal moves and more

def check_legality(board, turn):
    white_squares_attacked, black_squares_attacked = get_atacked_squares(board)

    white_king_row, white_king_col = find_king("white", board)
    black_king_row, black_king_col = find_king("black", board)

    if (
        (turn == "white" and white_squares_attacked[black_king_row][black_king_col] == 1)
        or
        (turn == "black" and black_squares_attacked[white_king_row][white_king_col] == 1)
    ):
        return False
    else:
        return True

def get_atacked_squares(board):
    # Create an empty 8x8 2D array
    white_squares_attacked = [[0] * 8 for _ in range(8)]
    black_squares_attacked = [[0] * 8 for _ in range(8)]

    
    for row in range(8):
        for col in range(8):
            piece = board[row][col]

            if piece == 0: continue

            piece_color = get_color(row, col, board)

            squares_atacked = white_squares_attacked if piece_color == "white" else black_squares_attacked

            piece_atack = generator_handlers[piece](row, col, board, piece_color)

            merge_arrays(squares_atacked, piece_atack, 1)

    return white_squares_attacked, black_squares_attacked



def merge_arrays(array1, array2, value_to_merge):
    for row in range(8):
        for col in range(8):
            if array2[row][col] == value_to_merge:
                array1[row][col] = array2[row][col]