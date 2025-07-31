def get_color(row, col, board):
    color = "white" if board[row][col] < 10 else "black"
    return color
