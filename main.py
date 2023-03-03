import time
# import event as event
import keyboard
import threading
import sys

gamepiece = "|"
# The piece on the board being moved
bg = "_"
# Places the "gamepiece" can occupy
gameboard = [bg for x in range(0,30)]
# Create the gameboard using spaces/underscores
pieceposition = 3
# Set initial pieceposition
max_position = len(gameboard)
# Position of the piece should not exceed the length
# of the gameboard


gameinprogress = True
# Game will run while this variable is True

def get_event():
    '''Get the keyboard event in a separate thread
    to prevent blocking the main thread'''
    global event
    while True:
        event = keyboard.read_key()

def left_key():
    '''Left key event function:
    Moves the game piece left one position'''
    global pieceposition
    if pieceposition > 0:
        gameboard[pieceposition] = bg
        pieceposition -= 1
    gameboard[pieceposition] = gamepiece

def right_key():
    '''Right key event function:
    Moves the game piece left one position'''
    global pieceposition
    if pieceposition < max_position:
        gameboard[pieceposition] = bg
        pieceposition += 1
    gameboard[pieceposition] = gamepiece

def end_game():
    '''Up key event function:
    Ends the game'''
    global gameinprogress
    gameinprogress = False
    sys.exit()

event = None
    
event_thread = threading.Thread(target=get_event)

event_thread.start()
 
while gameinprogress:
    # print(pieceposition)
    # Monitoring the pieceposition

    print(*gameboard, sep='')
    
    time.sleep(0.10)
    
    # print(event)
    # Monitoring the event (pressed key)

    match event:
        case "left":
            left_key()
        case "right":
            right_key()
        case "up":
            end_game()

    event = None
    # Set the event to None to prevent
    #   the gamepiece from moving indefinitely
