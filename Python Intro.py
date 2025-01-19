import turtle as trtl
import sys as sys
import random as rand

painter = trtl.Turtle()
painter.speed(25)

wn = trtl.Screen()
wn.bgcolor("navy")
wn.screensize(800, 800)

painter.penup()
painter.goto(-400, -300)
painter.pendown()

painter.fillcolor("olivedrab")
painter.begin_fill()
painter.forward(800)
painter.left(90)
painter.forward(225)
painter.left(90)
painter.forward(800)
painter.left(90)
painter.forward(225)
painter.end_fill()
painter.left(90)

painter.penup()

num_stars = int(input("How many stars do you want in the sky?"))

sizes = [0.5, 0.75, 1, 1.25, 1.5]

for dots in range(num_stars):
    randx = rand.randint(-400, 400)
    randy = rand.randint(-50, 350)
    painter.goto(randx, randy)
    painter.shape("circle")
    painter.color("lemonchiffon")
    painter.shapesize(rand.choice(sizes))
    painter.stamp()

color1 = input("What color would you like the house to be?")

painter.goto(0, 0)
painter.shape("square")
painter.color(color1)
painter.shapesize(12)
painter.stamp()

painter.color("black")
painter.shape("arrow")
painter.shapesize(1)

startx = 0
starty = 0
color2 = ""
width = 0

fw1 = 0
fw2 = 0
fw3 = 0
fw4 = 0

def draw_box(startx, starty, width, color2, fw1, fw2, fw3, fw4):
    painter.penup()
    painter.width(width)
    painter.goto(startx, starty)
    painter.pendown()

    painter.color(color2)
    painter.forward(fw1)
    painter.left(90)
    painter.forward(fw2)
    painter.left(90)
    painter.forward(fw3)
    painter.left(90)
    painter.forward(fw4)
    painter.left(90)

    painter.width(1)
    painter.penup()

draw_box(20, -118, 8, "firebrick", 65, 100, 65, 100)

painter.shape("circle")
painter.color("firebrick")
painter.goto(62, -65)
painter.stamp()

if color1 == "black":
    draw_box(-70, -35, 7, "white", 50, 50, 50, 50)

else:
    draw_box(-70, -35, 7, "black", 50, 50, 50, 50)

painter.penup()
painter.goto(-75, 75)
painter.pendown()

painter.fillcolor("firebrick")
painter.begin_fill()
painter.forward(250)
painter.left(135)
painter.forward(250)
painter.forward(250)
painter.end_fill()
painter.left(135)

painter.penup()

painter.color("darkgrey")
painter.goto(70, -180)
painter.fillcolor("darkgrey")
painter.begin_fill()
painter.pendown()
painter.circle(25)
painter.end_fill()
painter.penup()

painter.goto(85, -245)
painter.begin_fill()
painter.pendown()
painter.circle(25)
painter.end_fill()
painter.penup()

painter.color("black")

font_setup = ("Times New Roman", 35, "normal")
painter.goto(-300, -250)
text = wn.textinput("What would like to title your drawing?", "Respond here:")
painter.write(text, font = font_setup)

painter.hideturtle()
quit = input("Press X in the upper right hand corner to close window.")
sys.exit()