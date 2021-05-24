import random


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''

    while not (marker == 'x' or marker == 'o'):
        marker = input('Игрок 1 - выберите x или o: ').lower()

    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return player1, player2


def place_market(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark)):
        return True

    else:
        return False


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not \
            space_check(board, position):
        position = int(input('Укажите поле(1-9): '))

    return position


def replay():
    choise = input('Хотите играть снова? Yes or No: ').upper()
    return choise == 'YES'


print('Добро пожаловать в игру')
# цикл While
while True:
    # Игра
    # Настройка игры - игровове поле
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    # Кто ходит первым, выбор символа
    turn = choose_first()
    print(turn + ' ходит первым')

    play_game = input('Вы готовы играть? Yes or No: ').upper()
    if play_game == 'YES':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Игрок 1':
            # Ход игрока 1
            # игровое поле
            display_board(the_board)
            # выбор следующего хода
            position = player_choice(the_board)
            # поместить символ на игровое поле
            place_market(the_board, player1_marker, position)
            # проверить, выиграл ли игрок
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Игрок 1 выиграл!')
                game_on = False
            # или ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on = False
                else:
                    # если никто не выиграл и ничья
                    turn = 'Игрок 2'


        else:
            display_board(the_board)
            # выбор следующего хода
            position = player_choice(the_board)
            # поместить символ на игровое поле
            place_market(the_board, player2_marker, position)
            # проверить, выиграл ли игрок
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Игрок 2 выиграл!')
                game_on = False
            # или ничья
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья')
                    game_on = False
                else:
                    # если никто не выиграл и ничья
                    turn = 'Игрок 1'
    # Break
    if not replay():
        break
