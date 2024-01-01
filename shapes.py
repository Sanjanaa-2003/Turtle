import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):      #iterates as many times as the number of sides
    angle = 360 / num_sides     #eg:side is square = 4 --> angle is 90
    for _ in range(num_sides):  #range =0,1,2,3
        tim.forward(100)        #moves forward by 100
        tim.right(angle)        #turns by 90 degrees

for shapes in range(3, 10):     #draws shapes in the range of sides 3(triangle) to 10(decagon)
    tim.color(random.choice(colours))   #random colour
    draw_shape(shapes)  #draws a shape of size from 3 to 10