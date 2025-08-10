from game.generator.pawn import generate_pawn_moves
from game.generator.queen import generate_queen_moves
from game.generator.rook import generate_rook_moves
from game.generator.knight import generate_knight_moves
from game.generator.king import generate_king_moves
from game.generator.bishop import generate_bishop_moves


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