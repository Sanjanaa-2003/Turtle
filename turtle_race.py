from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
            "Enter a color: ")      #user input when the game opens
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]   #positions to place the turtle
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):            #iterates through y_positions
    new_turtle = Turtle(shape="turtle")     #sets shape to turtle
    new_turtle.penup()      #doesn't draw anything
    new_turtle.color(colors[turtle_index])   #iterates through the range
    new_turtle.goto(x=-230, y=y_positions[turtle_index])    #final position is 250 but if tuttle reaches 230 it wins so place it -230 backwards from thw origin, which is the starting point
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        #This is because turtle is 40 by 40 and hence half the width is subtracted
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()   #color has 2 parameters,
            # fill and pen color hence returns both.so only the required one is called
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)   #random steps are chosen for the turtle to move
        turtle.forward(rand_distance)

screen.exitonclick()