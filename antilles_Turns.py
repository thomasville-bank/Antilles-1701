
import turtle as trtl

base_Move = 1

SQUARE_SIZE = 80

playerOneship = trtl.Turtle()
playerTwoship = trtl.Turtle()
playerThreeship = trtl.Turtle()

ship = [playerOneship, playerTwoship, playerThreeship]

turn_index = 1

currentShip = ship[turn_index]


print("the current ship is", currentShip)


def move():
    global currentShip
    direction = input('which direction would you like to move ')

    if direction == "up":
        y += base_Move * SQUARE_SIZE
    elif direction == "down":
        y -= base_Move * SQUARE_SIZE
    elif direction == "left":
        x -= base_Move * SQUARE_SIZE
    elif direction == "right":
        x+= base_Move * SQUARE_SIZE
    
    currentShip.goto(x, y)

    turn_index = (turn_index + 1) % len(ship)


