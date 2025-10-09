import math

# Board representation: 3x3 list with 'X', 'O', or None
def print_board(board):
    for row in board:
        print([' ' if x is None else x for x in row])
    print()

def check_winner(board):
    # Check rows, columns, diagonals
    lines = board + list(map(list, zip(*board)))  # rows + columns
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # anti-diagonal

    for line in lines:
        if line == ['X'] * 3:
            return 'X'
        elif line == ['O'] * 3:
            return 'O'
    return None

def is_board_full(board):
    return all(cell is not None for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = None
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'X'  # AI is 'X'
                score = minimax(board, False)
                board[i][j] = None
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Example game
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

# AI is X, human is O
print("Initial board:")
print_board(board)

# Simulate a move by AI
move = best_move(board)
print(f"AI chooses move: {move}")
board[move[0]][move[1]] = 'X'

print_board(board)

