import turtle
import random

# construct a screen object and name it window
window = turtle.Screen()

# construct three different turtle objects
picasso = turtle.Turtle()
clickbox = turtle.Turtle()
instruction = turtle.Turtle()

# hide the cursors for the clickbox and instruction turtles
clickbox.hideturtle()
instruction.hideturtle()

# make the cursor shape for the picasso turtle into a circle
picasso.shape("circle")

# function to move clickbox turtle into location and draw a square
def paint_clickbox():
    clickbox.speed(0)
    clickbox.up()
    clickbox.goto(-200, 200)
    clickbox.down()
    for i in range(4):
        clickbox.forward(50)
        clickbox.right(90)
        
# function to move instruction turtle into location and write text
def paint_instructions():
    instruction.up()
    instruction.goto(-225, 205)
    instruction.write("Click the Box", font = ("Arial", 20, "bold"))
    instruction.goto(-40, -40)
    instruction.write("Click and drag the circle.", font = ("Arial", 10))

# function to change draw color to random values, then repaint the clickbox
def color_control(x, y):
    # do this only if the user clicked in the clickbox coordinates...
    if (-200 <= x <= -150) and (150 <= y <= 200):
        # get three random values between 0 and 1
        R = random.random()
        G = random.random()
        B = random.random()
        # make the picasso turtle use the random numbers for its three color channels
        picasso.color(R, G, B)
        # repaint the clickbox with those same three random color channels
        clickbox.color(R, G, B)
        paint_clickbox()

# function to initially paint the clickbox and instructions, then listen for events
def main():
    paint_clickbox()
    paint_instructions()
    window.onclick(color_control)
    picasso.onrelease(picasso.goto)

# call the main function to get things started
main()
