from turtle import *
import random
import turtle

direction = [0,90,180,270]

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)























screen = Screen()
screen.exitonclick()