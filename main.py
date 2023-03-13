import os

gamer = 'X'
flag_create_game = False
flag_win = False

while True:
    try:
        size_board = int(input('size board at least 3>> '))
        if size_board >= 3:
            flag_create_game = True
        break
    except ValueError:
        print('Wrong type ')

list_game = [[' ' for _ in range(size_board)] for _ in range(size_board)]
os.system("cls")

while flag_create_game:

    # print game board
    for row in range(size_board):
        print(' | '.join(list_game[row]))
        if row < size_board-1:
            print('-'*(size_board*3 + (size_board-2)))

    # gamer
    print('\nGamer : ', gamer)
    while True:
        try:
            row_index = int(input(' row   >> ')) - 1
            col_index = int(input('column >> ')) - 1

            if row_index >= size_board or col_index >= size_board:
                raise ValueError

            break
        except ValueError:
            print('point to a cell')

    os.system("cls")

    if list_game[row_index][col_index] == ' ':
        list_game[row_index][col_index] = gamer

        # check win
        if row_index == col_index and all([gamer == list_game[i][i] for i in range(size_board)]):
            flag_win = True
            flag_create_game = False
        elif all([gamer == list_game[row_index][i] for i in range(size_board)]):
            flag_win = True
            flag_create_game = False
        elif all([gamer == list_game[i][col_index] for i in range(size_board)]):
            flag_win = True
            flag_create_game = False

        if flag_win:
            for row in range(size_board):
                print(' | '.join(list_game[row]))
                if row < size_board-1:
                    print('-'*(size_board*3 + (size_board-2)))
            print('win >> ', gamer)

        flag_draw = True

        # change gamer
        if gamer == 'X':
            gamer = 'O'
        else:
            gamer = 'X'
