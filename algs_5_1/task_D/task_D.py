"""Task D"""


def safe_places(board: str) -> str:
    """For chess board 8x8"""
    board = [list(string) for string in board.split('\n')]
    for i0 in range(8):
        for j0 in range(8):
            if board[i0][j0] == 'B':
                board = check_for_bishop(i0, j0, board)
            elif board[i0][j0] == 'R':
                board = check_for_rook(i0, j0, board)
    result = 0
    for i1 in range(8):
        for j1 in range(8):
            if board[i1][j1] == '*':
                result += 1
    # print(board)
    return str(result)


def check_for_bishop(i: int, j: int, board: list[list[str]]) -> list[list[str]]:
    # go up-left
    m = j - 1
    for k in range(i - 1, -1, -1):
        if m < 0 or board[k][m] == 'R' or board[k][m] == 'B':
            break
        else:
            board[k][m] = "X"
            m -= 1
    # go down-left
    m = j - 1
    for k in range(i + 1, 8):
        if m < 0 or board[k][m] == 'R' or board[k][m] == 'B':
            break
        else:
            board[k][m] = "X"
            m -= 1
    # go up-right
    m = i - 1
    for k in range(j + 1, 8):
        if m < 0 or board[m][k] == 'R' or board[m][k] == 'B':
            break
        else:
            board[m][k] = "X"
            m -= 1
    # go down-right
    m = i + 1
    for k in range(j + 1, 8):
        if m > 7 or board[m][k] == 'R' or board[m][k] == 'B':
            break
        else:
            board[m][k] = "X"
            m += 1

    return board


def check_for_rook(i: int, j: int, board: list[list[str]]) -> list[list[str]]:
    # go up
    for k in range(i - 1, -1, -1):
        if board[k][j] == 'R' or board[k][j] == 'B':
            break
        else:
            board[k][j] = "X"
    # go down
    for k in range(i + 1, 8):
        if board[k][j] == 'R' or board[k][j] == 'B':
            break
        else:
            board[k][j] = "X"
    # go left
    for k in range(j - 1, -1, -1):
        if board[i][k] == 'R' or board[i][k] == 'B':
            break
        else:
            board[i][k] = "X"
    # go right
    for k in range(j + 1, 8):
        if board[i][k] == 'R' or board[i][k] == 'B':
            break
        else:
            board[i][k] = "X"
    return board


chess_board = ''
for i in range(8):
    chess_board += input() + "\n"

print(safe_places(chess_board))


b1 = """********
********
*R******
********
********
********
********
********"""

# print(safe_places(b1))
