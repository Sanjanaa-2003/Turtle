import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.pencolor("black")
    #No drawing while movimg
    tim.penup()
    tim.forward(10)
    tim.pencolor("red")
    #Drawing when moving
    tim.pendown()