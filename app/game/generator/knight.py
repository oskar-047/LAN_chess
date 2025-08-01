from game.utils import get_color
from game.generator.piece_generator import generate_piece_moves

def generate_knight_moves(row, col, board, color):

    knight_dir = [
        [2, 1], # bottom right
        [2, -1], # bottom left
        [-2, 1], # top right
        [-2, -1], # top left
        [-1, 2], # right top
        [1, 2], # right bottom
        [-1, -2], # left top
        [1, -2], # left bottom
    ]

    return generate_piece_moves(row, col, board, color, knight_dir, False)