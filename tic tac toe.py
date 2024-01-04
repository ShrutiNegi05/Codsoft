import copy

EMPTY = ' '
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    return any(all(cell == player for cell in line) for line in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def evaluate(board):
    if is_winner(board, AI_PLAYER):
        return 1
    elif is_winner(board, HUMAN_PLAYER):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = AI_PLAYER
            eval = minimax(new_board, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = HUMAN_PLAYER
            eval = minimax(new_board, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = None

    for i, j in get_empty_cells(board):
        new_board = copy.deepcopy(board)
        new_board[i][j] = AI_PLAYER
        move_val = minimax(new_board, 0, False)
        if move_val > best_val:
            best_val = move_val
            move = (i, j)

    return move

def play_tic_tac_toe():
    board = [[EMPTY] * 3 for _ in range(3)]

    while True:
        print_board(board)

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != EMPTY:
            print("Cell already taken. Try again.")
            continue
        board[row][col] = HUMAN_PLAYER

        if is_winner(board, HUMAN_PLAYER):
            print_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print("AI's move:")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = AI_PLAYER

        if is_winner(board, AI_PLAYER):
            print_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
