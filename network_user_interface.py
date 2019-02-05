# Albert Lin: 73361915
# Richmond Horikawa: 18715219

import shared_functions
import networking
import connectfour

def run_user_interface() -> None:
    'Starts the network version of connectfour'
    game_state = connectfour.new_game()
    connection = networking.connect('woodhouse.ics.uci.edu', 4444) 
    if (networking.start(connection) == True):
        print("Columns should be selected by typing a number between 1 and 7")
        print("Specify a move in the format of DROP col# or POP col#")
        print("replace col# with the column's number that you want selected")
        shared_functions.print_game_board(game_state)

        while(connectfour.winner(game_state) == connectfour.NONE): 
            response = networking.read_line(connection)
            if(response == 'READY'): 
                while True:
                    user_input = input('input your move: ')
                    if(shared_functions.is_valid_input(user_input)):
                        break
                    print('Your move was invalid.. please re-enter')
                networking.write_line(connection, user_input)
                response = networking.read_line(connection)
                if (response == 'OKAY'):
                    game_state = shared_functions.process_user_input(game_state, user_input)
                    shared_functions.print_game_board(game_state)
                    response = networking.read_line(connection)
                    print("server's response: " + response)
                    if shared_functions.is_valid_input(response):
                        game_state = shared_functions.process_user_input(game_state, response)
                        shared_functions.print_game_board(game_state)
                        if connectfour.winner(game_state) == connectfour.YELLOW:
                            print('Congrats WINNER_YELLOW')
                            networking.close(connection)
                    else:
                        networking.close(connection)
                elif (response == 'INVALID'):
                    print('Your move was invalid... please re-enter')
                elif response == 'WINNER_RED':
                    print('Congrats ' + response) 
                    networking.close(connection)
                    break
        
if __name__ == '__main__':
    run_user_interface()
