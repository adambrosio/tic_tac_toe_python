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
        marker = input('Player 1: Choose X or O').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')