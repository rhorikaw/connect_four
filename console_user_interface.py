# Albert Lin: 73361915
# Richmond Horikawa: 18715219

import shared_functions
import connectfour

def run_user_interface() -> None:
    'Starts the console veresion of connectfour'
    game_state = connectfour.new_game()
    print("Columns should be selected by typing a number between 1 and 7")
    print("Specify a move in the format of DROP col# or POP col#")
    print("replace col# with the column's number that you want selected")
    turn = 0
    while(connectfour.winner(game_state) == connectfour.NONE):
        if turn % 2 == 0:
            print('______________________')
            print("PLAYER RED'S TURN")
        else:
            print('______________________')
            print("PLAYER YELLOW'S TURN")
        user_input = input('Enter a move: ') 
        game_state = shared_functions.process_user_input(game_state, user_input) 
        shared_functions.print_game_board(game_state)
        turn += 1
    winner = connectfour.winner(game_state)
    if winner == 1:
        winner_color = 'PLAYER RED'
    else:
        winner_color = 'PLAYER YELLOW'
    print('Congratulations ' + winner_color + ', you are the winner!')

if __name__ == '__main__':
    run_user_interface()
    
    
