import turtle
import sys

sys.setrecursionlimit(5000) 

ins_border = turtle.Turtle()      #Inside Border
ins_border.speed(0)

out_border = turtle.Turtle()      #Outside Border
out_border.speed(0)

moon = turtle.Turtle()            #To create the moon
moon.speed(0)

sun = turtle.Turtle()             #To create the sun
sun.speed(0)

#To create a screen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)

out_border.color("blue")

out_border.begin_fill()     #To begin filling up the outside border with color

#To make outside border
out_border.penup()
out_border.right(90)
out_border.forward(15)
out_border.pendown()
out_border.left(90)

out_border.forward(280)
out_border.left(145)
out_border.forward(530)
out_border.left(125)
out_border.forward(535)
out_border.left(90)
out_border.forward(420)
out_border.left(135)
out_border.forward(330)
out_border.right(135)

out_border.end_fill()      #To end filling up the outside border with color


#To make inside border
ins_border.color("red")
ins_border.begin_fill()   #To begin filling up the inside border with color

ins_border.forward(230)
ins_border.left(145)
ins_border.forward(450)
ins_border.left(125)
ins_border.forward(490)
ins_border.left(90)
ins_border.forward(370)
ins_border.left(135)
ins_border.forward(330)
ins_border.right(135)

ins_border.end_fill()     #To end filling up the inside border with color

ins_border.hideturtle()   # To hide the turtle

#To Draw the moon
moon.penup()
moon.goto(-100, 100)
moon.color("white")

moon.right(90)
angle = 1

moon.begin_fill()     # To fill the color of moon
for _ in range(180):
    moon.forward(1.07)  
    moon.left(angle)
    
moon.left(160)
for _ in range(35):
    moon.forward(1.1)  
    moon.right(angle)

moon.right(30)
for _ in range(25):
    moon.forward(75)
    moon.right(150)

moon.left(110)
for _ in range(40):
    moon.forward(1.1)  
    moon.right(angle)
moon.end_fill()       # To end the color fill to the moon

moon.hideturtle()     # To hide the turtle

#To Draw the sun
sun.penup()
sun.goto(-80, -100)  # To Adjust the position of the star
sun.color("white")   # To make the color of the sun white

sun.begin_fill()     # To begin the color filling of the sun

for _ in range(12):
    sun.forward(100)
    sun.right(150)
sun.end_fill()       # To end the color filling of the sun

sun.hideturtle()     # To hide the turtle

# Close the Turtle graphics window when clicked
screen.exitonclick()


