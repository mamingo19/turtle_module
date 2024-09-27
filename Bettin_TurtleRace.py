import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
screen = Screen()
screen.setup(width=500, height=400)
computer_choice = random.choice(colors).upper()
user_bet = screen.textinput(title = "MAKE YOUR DAMN BET", prompt = f"Which turtle will win the race?  Enter a color! psst! if I were you I will choose {computer_choice}: ")[0].lower()
all_turtles = []

position = 0
for color in colors:
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y =-100 + position)
    position += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color[0].lower() == user_bet:
                print(f"You have won! The {winning_color.upper()} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color.upper()} turtle is the winner")
            if winning_color[0].lower() == computer_choice[0].lower():
                print(f"I told you {computer_choice} would win!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)














screen.exitonclick()
