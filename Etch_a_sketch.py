from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed("fastest")
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()     #CLEARS EVERYTHING
    tim.penup()     #DOESN'T DRAW ANYTHING
    tim.home()      #GOES TO STARTING POSITION
    tim.pendown()   #STARTS DRAWING

screen.listen()
screen.onkey(move_forwards, "U")
screen.onkey(move_backwards, "D")
screen.onkey(turn_left, "L")
screen.onkey(turn_right, "R")
screen.onkey(clear, "C")
#CAPS LOCK SHOULD BE ON
screen.exitonclick()
