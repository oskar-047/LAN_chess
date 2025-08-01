from game.utils import get_color
from game.generator.piece_generator import generate_piece_moves

def generate_king_moves(row, col, board, color):

    king_dir = [
        [1, 0], # bottom center
        [1, 1], # bottom right
        [0, 1], # center right
        [-1, 1], # top right
        [-1, 0], # top center
        [-1, -1], # top left
        [0, -1], # center left
        [1, -1] # bottom left
    ]

    return generate_piece_moves(row, col, board, color, king_dir, False)