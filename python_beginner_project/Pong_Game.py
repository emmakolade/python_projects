
import turtle
import winsound

win = turtle.Screen()
win.title("Pong Game by Akolade")
win.bgcolor("black")
win.setup(width=900, height=700)
win.tracer(0) # stops windows from updating which in turn speeds up my game

# score tracker
score_1 = 0
score_2 = 0


# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0) #this speed is not the paddle speed, it is the animation speed and
                  # it is neccessary for the turtle module.
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid= 4, stretch_len= 1)
paddle_1.penup() # ensures line is not drawn
paddle_1.goto(-400, 0) # the position to place the paddle

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid= 4, stretch_len= 1)
paddle_2.penup()
paddle_2.goto(+400, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# seperate the ball movement into two parts
ball.dx = 0.4
ball.dy = -0.4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Cambria", 22, "bold"))
#  function
def paddle_1_up():
    # to move the paddle, i need to know the current y coordniate
    y = paddle_1.ycor()
    y += 40
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 40
    paddle_1.sety(y)

def paddle_2_up():
    # to move the paddle, i need to know the current y coordniate
    y = paddle_2.ycor()
    y += 40
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 40
    paddle_2.sety(y)

# keyboard binding
win.listen() #listen for keyboard inputs
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "z")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# main game loop
while True:
    win.update() # everytime a loop runs, it updates the screen

    # to move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 340:
        ball.sety(340) # set the ball
        ball.dy *= -1 # reverses the ball when it gets to the y border
        winsound.PlaySound("Click.wav", winsound.SND_ASYNC)

    if ball.ycor() < -340:
        ball.sety(-340) # set the ball
        ball.dy *= -1 # reverses the ball when it gets to the y border
        winsound.PlaySound("Click.wav", winsound.SND_ASYNC)

    # for the left and right border
    if ball.xcor() > 420:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Cambria", 22, "bold"))

    if ball.xcor() < -420:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_2 += 1
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Cambria", 22, "bold"))

    #getting the paddles to bounce the ball

    if ball.xcor() > 390 and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.dx *= -1
        winsound.PlaySound("Click.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390 and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.dx *= -1
        winsound.PlaySound("Click.wav", winsound.SND_ASYNC)

