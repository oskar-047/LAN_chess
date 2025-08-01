def get_color(row, col, board):
    color = "white" if board[row][col] < 10 else "black"
    return color


def function_A():
    result = function_B()
    print(result)

def function_B():
    return "hello"