import turtle
import random

wn=turtle.Screen()
wn.title("Playground")
tiegan=turtle.Turtle()
bot=turtle.Turtle()
wordBot=turtle.Turtle()
bot.speed(0)
wordBot.speed(0)
bot.hideturtle()
wordBot.hideturtle()

# functions to control your turtle
def forward():
    tiegan.fd(15)

def backwards():
    tiegan.backward(15)

def turnRight():
    tiegan.rt(45)

def turnLeft():
    tiegan.lt(45)

def penUp():
    tiegan.penup()

def penDown():
    tiegan.pendown()

def bgColor():
    r=random.random()
    g=random.random()
    b=random.random()
    wn.bgcolor(r,g,b)

def quit():
    wn.bye()

def come(x,y):
    if not(200<= x <=250) and not (200>= y >=150):
        tiegan.hideturtle()
        tiegan.penup()
        tiegan.goto(x,y)
        tiegan.pendown()
        tiegan.showturtle()


# Draws the click Box
def box():
    bot.penup()
    bot.goto(200,200)
    bot.pendown()
    for x in range(4):
        bot.fd(50)
        bot.rt(90)


# Makes click box work
def click_box(x,y):
    if (200<= x <= 250) and (200>= y >=150):
        R=random.random()
        G=random.random()
        B=random.random()




        #changes color of main bot (tiegan)
        tiegan.color(R,G,B)
        wordBot.color(R,G,B)
        click_box_ins()
        


#Draws instructions for click box

def click_box_ins():
    wordBot.penup()
    wordBot.goto(160,210)
    wordBot.pendown()
    wordBot.write("\Change Line Color/", font=("Arial", 15))

#draws player instructions

wordBot.penup()
wordBot.goto(-420,400)
wordBot.pendown()
wordBot.write("'Up arrow' to go straight", font=("Arial", 15))
wordBot.penup()
wordBot.goto(-420,380)
wordBot.pendown()
wordBot.write("'Down arrow' to go backwards", font=("Arial", 15))
wordBot.penup()
wordBot.goto(-420,360)
wordBot.pendown()
wordBot.write("'Right arrow' to turn right", font=("Arial", 15))
wordBot.penup()
wordBot.goto(-420,340)
wordBot.pendown()
wordBot.write("'Left arrow' to turn left", font=("Arial", 15))
wordBot.penup()
wordBot.goto(-420,320)
wordBot.pendown()
wordBot.write("'C' to change background color", font=("Arial",15))
wordBot.penup()
wordBot.goto(-420,300)
wordBot.pendown()
wordBot.write("'U' to stop drawing", font=("Arial",15))
wordBot.penup()
wordBot.goto(-420,280)
wordBot.pendown()
wordBot.write("'D' to start drawing", font=("Arial",15))
wordBot.penup()
wordBot.goto(-420,260)
wordBot.pendown()
wordBot.write("'Q' to quit playing", font=("Arial",15))
wordBot.penup()
wordBot.goto(-420,240)
wordBot.pendown()
wordBot.write("Click anywhere to teleport there", font=("Arial",15))



# Key presses that will activate the commands above
wn.onkey(forward,"Up")
wn.onkey(backwards,"Down")
wn.onkey(turnRight,"Right")
wn.onkey(turnLeft,"Left")
wn.onkey(penUp,"u")
wn.onkey(penDown,"d")
wn.onkey(bgColor,"c")
wn.onkey(quit,"q")


##These will read the script and wait for a keypress
click_box_ins()
box()
wn.onclick(come)
wn.onclick(click_box, add=True)
wn.listen()
wn.mainloop()


    
