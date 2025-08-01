from game.utils import get_color
from game.generator.piece_generator import generate_piece_moves

def generate_rook_moves(row, col, board, color):

    rook_dir = [
        [1, 0], # bottom center
        [0, 1], # center right
        [-1, 0], # top center
        [0, -1], # center left
    ]

    return generate_piece_moves(row, col, board, color, rook_dir, True)