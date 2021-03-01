from IPython.display import clear_output

def display_board(board):
    clear_output()

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():

    '''
    TUPLE UNPACKING
    OUTPUT = (Player 1 Marker, Player 2 Marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

'''
TAKES IN BOARD LIST OBJECT, THE MARKER ('X OR 'O), AND THE DESIRED POISITION (1-9)
'''
def place_marker(board, marker, position):
    board[position] = marker

'''
CHECKS FOR WINNER USING INDEXING
'''
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3]) == mark or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark))

'''
ESSENTIALLY A COINFLIP
'''
import random

def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

'''
CHECKS IF SPACE IS AVAILABLE
'''
def space_check(board, position):
    return board[position] == ' '

'''
FULL BOARD CHECK
'''
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

'''
USES space_check() TO CHECK USER INPUT AGAINST THE BOARD
'''
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int('Choose a position (1-9): ')

    return position