# Albert Lin: 73361915
# Richmond Horikawa: 18715219

import connectfour

def print_game_board(game_state: connectfour.GameState) -> None:
    'Prints the current board'
    number_column = '' 
    for x in range(connectfour.BOARD_COLUMNS):
        number_column += str(x + 1) + '  '
    print(number_column)

    for row in range(connectfour.BOARD_ROWS): 
        line = ''
        for col in range(connectfour.BOARD_COLUMNS):
            if(game_state.board[col][row] == 1):
                line += 'R' + '  '
            elif(game_state.board[col][row] == 2):
                line += 'Y' + '  '
            else:
                line += '.' + '  '
        print(line)


def process_user_input(game_state: connectfour.GameState, string_input: str) -> connectfour.GameState: 
    'Takes in a string input and converts it into a move in the game'
    split_input = string_input.split() 
    while True:
        try:
            if(split_input[0] == 'DROP'):
                return connectfour.drop(game_state, int(split_input[1]) - 1)  
            elif(split_input[0] == 'POP'):
                return connectfour.pop(game_state, int(split_input[1]) - 1) 
            else:
                raise connectfour.InvalidMoveError
        except (connectfour.InvalidMoveError, ValueError):
            user_input = input('Your move was invalid. Please enter another move: ')
            split_input = user_input.split()
        except(connectfour.GameOverError):
            print('The game is already over.')
            break

def is_valid_input(string_input: str) -> bool:
    'Checks whether the input indicates a valid move'
    split_input = string_input.split() 
    if(len(split_input) == 2):
        if (split_input[0] == 'DROP' or split_input[0] == 'POP'):
            try:
                move = int(split_input[1])
                if 0 < move <= connectfour.BOARD_COLUMNS:
                    return True
                else:
                    return False
            except ValueError:
                return False
    else:
        return False

