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