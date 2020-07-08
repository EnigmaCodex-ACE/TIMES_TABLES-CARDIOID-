import turtle
import random
import math
turtle=turtle.Turtle()
points_on_circle=int(input('points'))
number=2
turtle.speed(10000)
pi=(2*math.pi)/points_on_circle
radius=300
list_of_coords=[]
for i in range(points_on_circle):
    list_of_coords.append([i,radius*math.cos(i*pi),radius*math.sin(i*pi)])

turtle.penup()

for i in list_of_coords:
    turtle.goto(i[1],i[2])
    l=(number*i[0])%points_on_circle
    turtle.pendown()
    for j in list_of_coords:
        if l == j[0]:
            turtle.goto(j[1],j[2])
    turtle.penup()
    
    
    
    
    
    
