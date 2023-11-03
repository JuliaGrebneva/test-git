def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return  True

def play_game():
    board = [[' ']*3 for i in range(3)]
    current_player = 'X'
    winner = None
    while not winner and not is_board_full(board):
        print_board(board)
        print('Ход игрока {}'.format(current_player))
        row = int(input('Выберете номер строки (0, 1, 2): '))
        col = int(input('Выберете номер столбца (0, 1, 2): '))
        if board[row][col] != ' ':
            print('Данная ячейка уже занята. Попробуйте другую.')
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    print_board(board)
    if winner:
        print('Победитель {} выиграл!'.format(winner))
    else:
        print('Ничья!')

play_game()