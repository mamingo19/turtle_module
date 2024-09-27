from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Flags to track if the keys are pressed
is_moving_forwards = False
is_moving_backwards = False
is_turning_left = False
is_turning_right = False

# Function to move the turtle forward continuously
def move_forwards():
    global is_moving_forwards
    is_moving_forwards = True
    while is_moving_forwards:
        tim.forward(10)


# Function to stop moving forward
def stop_moving_forwards():
    global is_moving_forwards
    is_moving_forwards = False

# Function to move the turtle backward continuously
def move_backwards():
    global is_moving_backwards
    is_moving_backwards = True
    while is_moving_backwards:
        tim.backward(10)


# Function to stop moving backward
def stop_moving_backwards():
    global is_moving_backwards
    is_moving_backwards = False

# Function to turn left continuously
def turn_left():
    global is_turning_left
    is_turning_left = True
    while is_turning_left:
        new_heading = tim.heading() + 10
        tim.setheading(new_heading)


# Function to stop turning left
def stop_turning_left():
    global is_turning_left
    is_turning_left = False

# Function to turn right continuously
def turn_right():
    global is_turning_right
    is_turning_right = True
    while is_turning_right:
        new_heading = tim.heading() - 10
        tim.setheading(new_heading)


# Function to stop turning right
def stop_turning_right():
    global is_turning_right
    is_turning_right = False

# Function to clear the screen and reset turtle's position
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set up key bindings
screen.listen()

# Movement bindings
screen.onkeypress(move_forwards, "w")  # Start moving forwards when 'w' is pressed
screen.onkeyrelease(stop_moving_forwards, "w")  # Stop moving forwards when 'w' is released
screen.onkeypress(move_backwards, "s")  # Start moving backwards when 's' is pressed
screen.onkeyrelease(stop_moving_backwards, "s")  # Stop moving backwards when 's' is released

# Turning bindings
screen.onkeypress(turn_left, "a")  # Start turning left when 'a' is pressed
screen.onkeyrelease(stop_turning_left, "a")  # Stop turning left when 'a' is released
screen.onkeypress(turn_right, "d")  # Start turning right when 'd' is pressed
screen.onkeyrelease(stop_turning_right, "d")  # Stop turning right when 'd' is released

# Clear the screen binding
screen.onkey(clear, "c")  # Clear the screen when 'c' is pressed

# Main loop to keep the window open and listen for key events
screen.exitonclick()
