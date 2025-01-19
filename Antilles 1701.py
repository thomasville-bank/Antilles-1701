#Antilles 1701

import turtle as trtl
import random as rand
from turtle import *

painter = trtl.Turtle()
painter.hideturtle()

wn = trtl.Screen()
wn.setup(width = 800, height = 800)
wn.title("Antilles 1701")
wn.bgcolor("moccasin")

#creates a function to create a rectangle with width w and height h
def rect(w, h):
    painter.pendown()
    painter.begin_fill()
    painter.setheading(0)
    painter.forward(w)
    painter.left(90)
    painter.forward(h)
    painter.left(90)
    painter.forward(w)
    painter.left(90)
    painter.forward(h)
    painter.left(90)
    painter.end_fill()
    painter.penup()

painter.speed(0)
painter.penup()
painter.goto(-250,50)
painter.pendown

#title screen
painter.write('Antilles 1701:', font=('Zapfino',40))
painter.write('\n\n\n\n\nA Les Incompetents Production', font=('Zapfino',0))

#creates a grid with grid_side rows and columns
square = 0
square_x = -400
grid_side = 10
SQUARE_SIZE = 800 / grid_side

for column in range (grid_side):
    square_y = -400
    for row in range (grid_side):
        painter.goto(square_x, square_y)
        #alternate between dodger blue and deep sky blue squares
        square_color = square % 2
        if square_color == 0:
            painter.color("dodger blue")
        elif square_color == 1:
            painter.color("deep sky blue")
        rect(80, 80)
        square += 1
        square_y += SQUARE_SIZE
    square_x += SQUARE_SIZE
    square += 1

#randomly place 13 islands throughout grid
def randomize_position():
    global island_row
    global island_column
    island_row = rand.randint(0, 9)
    island_column = rand.randint(0, 9)
    
island_rows = []
island_columns = []

wn.addshape("palm island.gif")
wn.addshape("inverted_palm_island.gif")

#randomly alternate between two types of palm islands
island_shape_num = rand.randint(1, 2)
if island_shape_num == 1:
    island_shape = "palm island.gif"
elif island_shape_num == 2:
    island_shape = "inverted_palm_island.gif"

island1 = trtl.Turtle(shape=island_shape)
randomize_position()
island1.penup()
island1.speed(0)
island_rows.append(island_row)
island_columns.append(island_column)
island1.goto((island_column * SQUARE_SIZE - 360), (island_row * SQUARE_SIZE - 360))

def check():
    island_collision = 0
    while island_collision < (len(island_rows)):
        if island_column == island_columns[island_collision]:
                if island_row == island_rows[island_collision]:
                    randomize_position()
                    check()
        island_collision += 1

for island in range((int(grid_side * grid_side * 0.13)) - 1):
    island_shape_num = rand.randint(1, 2)
    if island_shape_num == 1:
        island_shape = "palm island.gif"
    elif island_shape_num == 2:
        island_shape = "inverted_palm_island.gif"

    island = trtl.Turtle(shape=island_shape)
    randomize_position()
    check()
    island.penup()
    island.speed(0)
    island_rows.append(island_row)
    island_columns.append(island_column)
    island.goto((island_column * SQUARE_SIZE - 360), (island_row * SQUARE_SIZE - 360))

# creates variables for how many islands one has been to

player_one_score = 0
player_two_score = 0
player_three_score = 0

#creates a list of island claims
island_claims = []
for island in range(len(island_columns)):
    island_claims.append("unclaimed")

#determine row and column based on mouse location
def grid_clicked(x, y):
    column = int((x + 400) / 80)
    row = int((y + 400) / 80)
    print("You are in row", row, "and column", column)

# establishes three ships as movable entities

base_Move = 1
wn.addshape("red ship.gif")
wn.addshape("green ship.gif")
wn.addshape("yellow ship.gif")
playerOneship = trtl.Turtle(shape = "red ship.gif")
playerTwoship = trtl.Turtle(shape = "green ship.gif")
playerThreeship = trtl.Turtle(shape = "yellow ship.gif")


# this creates a list of the ships 

playerOnename=wn.textinput("Enter Name", "Ahoy, Player One, what be your name on the high seas?")
playerTwoname=wn.textinput("Enter Name", "Ahoy, Player Two, what be your name on the high seas?")
playerThreename=wn.textinput("Enter Name", "Ahoy, Player Three, what be your name on the high seas?")

player = [playerOnename,playerTwoname,playerThreename]
ship = [playerOneship, playerTwoship, playerThreeship]
ship_columns = []
ship_rows = []

#randomize ship locations
def randomize_ships():
    global ship_row
    global ship_column
    ship_row = rand.randint(0, 9)
    ship_column = rand.randint(0, 9)

def island_check():
    island_collision = 0
    while island_collision < (len(island_rows)):
        if ship_column == island_columns[island_collision]:
                if ship_row == island_rows[island_collision]:
                    randomize_ships()
                    island_check()
        island_collision += 1

randomize_ships()
island_check()

ship_rows.append(ship_row)
ship_columns.append(ship_column)

def island_ship_check():
    island_collision = 0
    while island_collision < (len(island_rows)):
        if ship_column == island_columns[island_collision]:
                if ship_row == island_rows[island_collision]:
                    randomize_ships()
                    island_ship_check()
        island_collision += 1

    ship_collision = 0
    while ship_collision < (len(ship_rows)):
        if ship_column == ship_columns[ship_collision]:
            if ship_row == ship_rows[ship_collision]:
                randomize_ships()
                island_ship_check()
        ship_collision += 1
            

for other_ship in range(2):
    randomize_ships()
    island_ship_check()

    ship_rows.append(ship_row)
    ship_columns.append(ship_column)

playerOneship.penup()
playerTwoship.penup()
playerThreeship.penup()
playerOneship.goto((ship_columns[0] * SQUARE_SIZE - 360), (ship_rows[0] * SQUARE_SIZE - 360))
playerTwoship.goto((ship_columns[1] * SQUARE_SIZE - 360), (ship_rows[1] * SQUARE_SIZE - 360))
playerThreeship.goto((ship_columns[2] * SQUARE_SIZE - 360), (ship_rows[2] * SQUARE_SIZE - 360))


# assign the treasure to a random island
treasure_island = rand.randint(0,((int(grid_side * grid_side * 0.13))) - 1)

# this starts the game on turn one

turn_index = 0
player_one_score = 0
player_two_score = 0
player_three_score = 0

# move function which asks for direction, then changes the ship's current x,y to the new coordinates, then resets the turn counter 
treasure = False
def move():
    global turn_index
    currentShip = ship[turn_index]
    x = ship_columns[turn_index] * SQUARE_SIZE - 360
    y = ship_rows[turn_index] * SQUARE_SIZE - 360

    def get_directions():
        global direction
        direction = wn.textinput(player[turn_index],'Which direction would you like to move? (up, down, left, right)')

    get_directions()
    if direction == "up":
        if ship_rows[turn_index] != 9:
            ship_rows[turn_index] += 1
        else:
                get_directions()
    elif direction == "down":
        if ship_rows[turn_index] != 0:
            ship_rows[turn_index] -= 1
        else:
                get_directions()
    elif direction == "left":
        if ship_columns[turn_index] != 0:
            ship_columns[turn_index] -= 1
        else:
                get_directions()
    elif direction == "right":
        if ship_columns[turn_index] != 9:
            ship_columns[turn_index] += 1
        else:
                get_directions()
    
    # def up():
    #     print("up!")
    
    # onkey(up, "Up")
    
    x = ship_columns[turn_index] * SQUARE_SIZE - 360
    y = ship_rows[turn_index] * SQUARE_SIZE - 360

    currentShip.goto(x,y)

    global player_one_score
    global player_two_score
    global player_three_score
    global island_columns
    global island_rows
    global treasure
    global treasure_island

# creates a function to draw a flag on claimed islands
    def plant_flag():
        painter.goto((ship_columns[turn_index] * SQUARE_SIZE - 340), (ship_rows[turn_index] * SQUARE_SIZE - 380))
        painter.setheading(90)
        painter.pencolor("black")
        painter.pendown()
        painter.forward(20)

        if turn_index == 0:
            painter.pencolor("red")
            painter.fillcolor("red")
        elif turn_index == 1:
            painter.pencolor("green")
            painter.fillcolor("green")
        elif turn_index == 2:
            painter.pencolor("yellow")
            painter.fillcolor("yellow")

        painter.begin_fill()
        painter.forward(10)
        painter.right(90)
        painter.forward(15)
        painter.right(90)
        painter.forward(10)
        painter.right(90)
        painter.forward(15)
        painter.end_fill()
        painter.penup()
        painter.pencolor("black")

    land_ho = 0
    while land_ho < (int(grid_side * grid_side * 0.13)):
        if island_columns[land_ho] == ship_columns[turn_index]:
            if island_rows[land_ho] == ship_rows[turn_index]:
                if island_claims[land_ho] == "unclaimed":
                    if turn_index == 0:
                        player_one_score += 1
                        plant_flag()
                        island_claims[land_ho] = 0
                    elif turn_index == 1:
                        player_two_score += 1
                        plant_flag()
                        island_claims[land_ho] = 1
                    elif turn_index == 2:
                        player_three_score += 1
                        plant_flag()
                        island_claims[land_ho] = 2
                    print(player_one_score, player_two_score,player_three_score)
                    if ship_columns[turn_index] == island_columns[treasure_island]:
                        if ship_rows[turn_index] == island_rows[treasure_island]:
                            treasure = player[turn_index]
                            if turn_index == 0:
                                player_one_score += 3
                            elif turn_index == 1:
                                player_two_score += 3
                            elif turn_index == 2:
                                player_three_score += 3
                            print(player_one_score, player_two_score,player_three_score)

        land_ho += 1

    turn_index = (turn_index + 1) % len(ship)

while treasure == False:
    move()

# create a leaderboard
painter.color("moccasin")
painter.goto(-400, -400)
rect(800, 800)

painter.goto(-350, 300)
painter.pendown
painter.color("black")
treasure_finder = treasure, "found the treasure"
painter.write(" ".join(treasure_finder), font=('Zapfino',20))
painter.goto(-350, 200)
player_one_final = str(player_one_score)
player_one = player[0], player_one_final
painter.write(": ".join(player_one), font=('Zapfino',20))
painter.goto(-350, 100)
player_two_final = str(player_two_score)
player_two = player[1], player_two_final
painter.write(": ".join(player_two), font=('Zapfino',20))
painter.goto(-350, 0)
player_three_final = str(player_three_score)
player_three = player[2], player_three_final
painter.write(": ".join(player_three), font=('Zapfino',20))

listen()
wn.mainloop()