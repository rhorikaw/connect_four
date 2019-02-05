# Albert Lin: 73361915
# Richmond Horikawa: 18715219

from collections import namedtuple
import shared_functions
import socket
import connectfour

# Concepts and code based heavily off of the 10/26 lecture notes

PlayerConnection = namedtuple(
    'Connection',
    ['socket','socket_in', 'socket_out'])

class Connect4ProtocolError(Exception):
    pass

def connect(host: str, port: int) -> PlayerConnection:
    'Connects the player to the ConnectFour Server'
    player_socket = socket.socket()
    player_socket.connect((host,port))

    player_socket_in = player_socket.makefile('r')
    player_socket_out = player_socket.makefile('w')

    return PlayerConnection(
        socket = player_socket,
        socket_in = player_socket_in,
        socket_out = player_socket_out)

def close(connection: PlayerConnection) -> None:
    'Closes all sockets used to communicate with the server'
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()

def start(connection: PlayerConnection) -> bool:
    'Starts the game off by asking the player for its username'
    username  = input('Enter a username: ')
    while len(username) == 0 or len(username.split()) > 1:
        username = input('Please enter a valid username: ')
    write_line(connection, 'I32CFSP_HELLO ' + username)
    response = read_line(connection)
    
    if response == ('WELCOME ' + username):
        print(response)
        write_line(connection, 'AI_GAME')  
        return True
    else:
        return False 

def read_line(connection: PlayerConnection) -> str:
    'Reads a line of input from the server'
    return connection.socket_in.readline()[:-1]

def write_line(connection: PlayerConnection, line: str) -> None:
    'Writes a line of output to the server'
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()
