from game.utils import get_color
from game.generator.piece_generator import generate_piece_moves

def generate_bishop_moves(row, col, board, color):

    bishop_dir = [
        [1, 1], # bottom right
        [-1, 1], # top right
        [-1, -1], # top left
        [1, -1] # bottom left
    ]

    return generate_piece_moves(row, col, board, color, bishop_dir, True)