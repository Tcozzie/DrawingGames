import turtle
tiegan=turtle.Turtle()
tiegan.speed(30)
tiegan.penup()
tiegan.goto(60,0)


def tallOval(r):
    for loop in range(2):
        tiegan.circle(r,90)
        tiegan.circle(r/2,90)

def flatOval(r):
    tiegan.lt(90)
    for loop in range(2):
        tiegan.circle(r,90)
        tiegan.circle(r/2,90)




tiegan.pendown()
tiegan.lt(90)
tiegan.fd(100)
tiegan.fillcolor("#8B4513")
tiegan.begin_fill()
#semi-circle
for x in range(180):
    tiegan.fd(1)
    tiegan.lt(1)

tiegan.fd(100)
tiegan.lt(90)
tiegan.goto(61,0)
tiegan.end_fill()

#left eye
tiegan.penup()
tiegan.goto(-30,100)
tiegan.fillcolor("black")
tiegan.begin_fill()
tiegan.lt(45)
tallOval(20)
tiegan.end_fill()

#right eye
tiegan.goto(15,100)
tiegan.begin_fill()
tallOval(20)
tiegan.end_fill()

#Nose
tiegan.fillcolor("pink")
tiegan.penup()
tiegan.goto(0,90)
tiegan.begin_fill()
flatOval(25)
tiegan.end_fill()

#left eye white
tiegan.penup()
tiegan.goto(-42,125)
tiegan.pendown()
tiegan.fillcolor("#ECE7E7")
tiegan.begin_fill()
tiegan.lt(90)
tallOval(7)
tiegan.end_fill()

#right eye white
tiegan.penup()
tiegan.goto(2,125)
tiegan.pendown()
tiegan.begin_fill()
tallOval(7)
tiegan.end_fill()

#ground outline
tiegan.penup()
tiegan.goto(60,0)
tiegan.pendown()
tiegan.lt(225)
tiegan.fd(15)
tiegan.rt(90)
tiegan.fillcolor("#696969")
tiegan.begin_fill()
for loop in range(60):
    tiegan.fd(1)
    tiegan.rt(1)
for loop in range(25):
    tiegan.fd(1)
    tiegan.rt(4)
for loop in range(50):
    tiegan.fd(4)
    tiegan.rt(1)
for loop in range(25):
    tiegan.fd(1)
    tiegan.rt(4)
for loop in range(47):
    tiegan.fd(1)
    tiegan.rt(1)
tiegan.rt(95)
tiegan.fd(23)
tiegan.lt(90)
tiegan.goto(60,0)
tiegan.lt(90)
tiegan.fd(15)
tiegan.end_fill()

#ground details
tiegan.fillcolor("#D3D3D3")
tiegan.penup()
tiegan.goto(63,-10)
tiegan.pendown()
tiegan.begin_fill()
tiegan.rt(135)
tallOval(10)
tiegan.end_fill()
tiegan.penup()

tiegan.goto(45,-40)
tiegan.pendown()
tiegan.begin_fill()
tiegan.rt(45)
flatOval(20)
tiegan.end_fill()
tiegan.penup()

tiegan.goto(20,-20)
tiegan.pendown()
tiegan.begin_fill()
tiegan.lt(45)
flatOval(15)
tiegan.end_fill()
tiegan.penup()

tiegan.goto(-10,-25)
tiegan.pendown()
tiegan.begin_fill()
tallOval(10)
tiegan.end_fill()
tiegan.penup()

tiegan.goto(-45,-14)
tiegan.pendown()
tiegan.lt(90)
tiegan.begin_fill()
flatOval(15)
tiegan.end_fill()
tiegan.penup()

tiegan.goto(-65,-14)
tiegan.pendown()
tiegan.begin_fill()
flatOval(20)
tiegan.end_fill()
tiegan.penup()

