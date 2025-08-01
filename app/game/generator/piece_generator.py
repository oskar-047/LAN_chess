from game.utils import get_color

def generate_piece_moves(row, col, board, color, directions, infinite):

    moves = [[0 for _ in range(8)] for _ in range(8)]
    
    # Traversing the direction array
    for direction in directions:

        new_row = row
        new_col = col

        while True:
            # Calculating the new position
            new_row += direction[0]
            new_col += direction[1]

            # Checking if new position is out of bounds
            if not (0 <= new_row < 8 and 0 <= new_col < 8):
                break                

            # Saving the piece on the square of the next move
            piece = board[new_row][new_col]

            if piece == 0:
                moves[new_row][new_col] = 1

                if not infinite:
                    break

                continue

            piece_color = get_color(new_row, new_col, board)

            if color != piece_color:
                moves[new_row][new_col] = 1
                
            break

    return moves
