def get_color(row, col, board):

    piece = board[row][col]
    
    if piece == 0: 
        return None

    color = "white" if piece < 10 else "black"

    return color


def function_A():
    result = function_B()
    print(result)

def function_B():
    return "hello"

def find_king(color, board):
    piece_to_find = 6 if color == "white" else 16

    for row in range(8):
        for col in range(8):
            if board[row][col] == piece_to_find:
                return row, col
    