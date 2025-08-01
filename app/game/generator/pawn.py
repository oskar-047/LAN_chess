from game.utils import get_color

def generate_pawn_moves(row, col, board, color):

    moves = [[0 for _ in range(8)] for _ in range(8)]


    # Assignating basic vars like the move direction, the inital row and else

    direction = -1 if color == "white" else 1
    initial_row = 6 if color == "white" else 1

    one_step = row + direction 
    two_step = row + direction * 2 

    right_step = col + 1
    left_step = col - 1


    # --- ONE STEP ---
    if 0 <= one_step < 8 and board[one_step][col] == 0:
        moves[one_step][col] = 1


        # --- DOUBLE STEP ---
        if row == initial_row and 0 <= two_step < 8 and board[two_step][col] == 0:
            moves[two_step][col] = 1
    
    # --- PAWN DIAGONAL MOVEMENT ---
    diagonal_move(color, one_step, right_step, moves, board)
    diagonal_move(color, one_step, left_step, moves, board)

    

    return moves


def diagonal_move(color, row, col, moves, board):

    # Check that the move is not out of bounds
    if 0 <= col < 8 and 0 <= row < 8:
        
        # It saves the target piece
        target_piece = board[row][col]

        # Checks if the color of the target is not same as the pawn
        if target_piece != 0 and get_color(row, col, board) != color:
            moves[row][col] = 1

