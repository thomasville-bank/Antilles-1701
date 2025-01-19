#Antilles 1701

import turtle as trtl
import random as rand

painter = trtl.Turtle()
painter.hideturtle()

wn = trtl.Screen()
wn.setup(width = 800, height = 800)
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
island1 = trtl.Turtle(shape="palm island.gif")
randomize_position()
island1.penup()
island1.speed(0)
island_rows.append(island_row)
island_columns.append(island_column)
island1.goto((island_column * SQUARE_SIZE - 360), (island_row * SQUARE_SIZE - 360))

for island in range((int(grid_side * grid_side * 0.13)) - 1):
    island = trtl.Turtle(shape="palm island.gif")
    min_spaces = 0
    randomize_position()
    island.penup()
    island.speed(0)
    island_rows.append(island_row)
    island_columns.append(island_column)
    island.goto((island_column * SQUARE_SIZE - 360), (island_row * SQUARE_SIZE - 360))

# creates variables for how many islands one has been to

player_one_score = 0
player_two_score = 0
player_three_score = 0

#determine row and column based on mouse location
def grid_clicked(x, y):
    column = int((x + 400) / 80)
    row = int((y + 400) / 80)
    print("You are in row", row, "and column", column)

wn.onclick(grid_clicked)

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
ship_column = [6, 7, 8]
ship_row = [9, 9, 9]

playerOneship.penup()
playerTwoship.penup()
playerThreeship.penup()
playerOneship.goto((ship_column[0] * SQUARE_SIZE - 360), (ship_row[0] * SQUARE_SIZE - 360))
playerTwoship.goto((ship_column[1] * SQUARE_SIZE - 360), (ship_row[1] * SQUARE_SIZE - 360))
playerThreeship.goto((ship_column[2] * SQUARE_SIZE - 360), (ship_row[2] * SQUARE_SIZE - 360))

# assign the treasure to a random island
treasure_island = rand.randint(0,((int(grid_side * grid_side * 0.13))) - 1)

# this starts thegame on turn one

turn_index = 0

#this chooses the active ship based on what turn it is. I.e. if it is turn one, the first ship will be active




# move function which asks for direction, then changes the ship's current x,y to the new coordinates, then resets the turn counter 

treasure = False
def move():
    global turn_index
    currentShip = ship[turn_index]
    x = ship_column[turn_index] * SQUARE_SIZE - 360
    y = ship_row[turn_index] * SQUARE_SIZE - 360

    def get_directions():
        global direction
        direction = wn.textinput(player[turn_index],'Which direction would you like to move? (up, down, left, right)')

    get_directions()
    if direction == "up":
        if ship_row[turn_index] != 9:
            ship_row[turn_index] += 1
        else:
                get_directions()
    elif direction == "down":
        if ship_row[turn_index] != 0:
            ship_row[turn_index] -= 1
        else:
                get_directions()
    elif direction == "left":
        if ship_column[turn_index] != 0:
            ship_column[turn_index] -= 1
        else:
                get_directions()
    elif direction == "right":
        if ship_column[turn_index] != 9:
            ship_column[turn_index] += 1
        else:
                get_directions()
    
    x = ship_column[turn_index] * SQUARE_SIZE - 360
    y = ship_row[turn_index] * SQUARE_SIZE - 360

    currentShip.goto(x, y)

    turn_index = (turn_index + 1) % len(ship)

while treasure == False:
    move()
    

#   update score for finding islands
if (abs(ship.xcor - (island_columns * SQUARE_SIZE - 360) == 0)):
    if (abs(ship.ycor - (island_rows * SQUARE_SIZE - 360) == 0)):
        
        if turn_index == 0:
            player_one_score += 1
        elif turn_index == 1:
            player_two_score += 1
        elif turn_index == 2:
            player_three_score += 1

# draw a flag on claimed islands
ship_column = 0
ship_row = 0

painter.goto((ship_column * SQUARE_SIZE - 360), (ship_row * SQUARE_SIZE - 380))
painter.setheading(90)
painter.pencolor("black")
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



# create a leaderboard
# def leaderboard():
    


wn.mainloop()