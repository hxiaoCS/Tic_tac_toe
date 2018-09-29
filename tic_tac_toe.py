# Han X Sep 10, 2018
import random

def show_board(board):
    
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def hold_point(board, point_holder, point):
    board[point] = point_holder

def go_first():
    if random.randint(0, 1) == 0:
        return 'Player ONE'
    else:
        return 'Player TWO'

def user_input():
    point_holder = ''

    while point_holder != 'x' and point_holder != 'o':
        point_holder = input('Player ONE: use X or O?').lower()

    if point_holder == 'x':
        return ('x', 'o')
    else:
        return ('o', 'x')


def  point_is_left(board, point):
     
    return board[point] == ' '

def  check_all_points(board):
    for x in range(1,10):
        if point_is_left(board, x):
            return False
    return True


def  choose_point(board):
    point = 0
    
    while point not in [1,2,3,4,5,6,7,8,9] or not point_is_left(board, point):
        point = int(input('What is your next step? (point 1 - 9)'))
        
    return point

def  validate_win_conditions (board,occupied_point):
    
    return ((board[1] == occupied_point and board[2] == occupied_point and board[3] == occupied_point) or # bottom
    (board[4] == occupied_point and board[5] == occupied_point and board[6] == occupied_point) or # middle
    (board[7] == occupied_point and board[8] == occupied_point and board[9] == occupied_point) or # top
    (board[7] == occupied_point and board[4] == occupied_point and board[1] == occupied_point) or # right column
    (board[8] == occupied_point and board[5] == occupied_point and board[2] == occupied_point) or # middle column
    (board[9] == occupied_point and board[6] == occupied_point and board[3] == occupied_point) or # right column
    (board[7] == occupied_point and board[5] == occupied_point and board[3] == occupied_point) or # diagonal 1
    (board[9] == occupied_point and board[5] == occupied_point and board[1] == occupied_point)) # diagonal 2


def play_again():
    
    return input('One more time? Yes or No: ').lower().startswith('y')




# Logic Part
print('Let us play Tic Tac Toe game!')

while True:
    # start a new board
    new_board = [' '] * 10
    playerOne_pointHolder, playerTwo_pointHolder = user_input()
    turn = go_first()
    print(turn + ' will go first.')
    
    start_game = input('Ready? Yes or No.')
    
    if start_game.lower()[0] == 'y':
        game_playing = True
    else:
        game_playing = False

    while game_playing:
        if turn == 'Player ONE':
            # Player ONE turn
            show_board(new_board)
            point = choose_point(new_board)
            hold_point(new_board, playerOne_pointHolder, point)

            if validate_win_conditions(new_board, playerOne_pointHolder):
                show_board(new_board)
                print('{0} have won the game!'.format(turn))
                game_playing = False
            else:
                if check_all_points(new_board):
                    show_board(new_board)
                    print('No one win this game!')
                    break
                else:
                    turn = 'Player TWO'

        else:
            # Player TWO
            show_board(new_board)
            point = choose_point(new_board)
            hold_point(new_board, playerTwo_pointHolder, point)

            if validate_win_conditions(new_board, playerTwo_pointHolder):
                show_board(new_board)
                print('{0} have won the game!'.format(turn))
                game_playing = False
            else:
                if check_all_points(new_board):
                    show_board(new_board)
                    print('{0} have won the game!'.format(turn))
                    break
                else:
                    turn = 'Player ONE'

    if not play_again():
        break