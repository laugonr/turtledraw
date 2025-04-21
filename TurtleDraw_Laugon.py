# Turtle Draw 
# By: Ruben Laugon
# Credit: Eric Pouge, ChatGPT


import turtle
import math

print('TurtleDraw Starting...')

# Todo: Ask for the file name
filename = input("Enter the input file name: ")
tddata = open(filename, "r")

# Todo: setup the turtle screen
screen = turtle.Screen()
screen.setup(450, 450)

# Todo: setup turtle 
turtleDraw_Laugon = turtle.Turtle()
turtleDraw_Laugon.speed(0)
turtleDraw_Laugon.hideturtle()

# Todo: Turtle Drawing state
first_point = True
total_distance = 0.0
prev_coords = None

# Todo: Read and process the .txt file line by line
line = tddata.readline()

# Loop through the file
while line:
    line = line.strip()
    # Todo: handle stop command (lift pen, reset earlier coordinates)
    if line.lower() == "stop":
        turtleDraw_Laugon.penup()
        first_point = True
        prev_coords = None
        line = tddata.readline()
        continue

    parts = line.split(' ')
    if len(parts) == 3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw_Laugon.color(color)

        #Todo: Move without drawing to the first point
        if first_point:
            turtleDraw_Laugon.penup()
            turtleDraw_Laugon.goto(x, y)
            turtleDraw_Laugon.pendown()
            first_point = False
        else:

            #Todo: Draw a line to next point and calcuate the distance.
            px, py = prev_coords
            distance = math.dist((px, py), (x, y))
            total_distance += distance
            turtleDraw_Laugon.goto(x, y)

        prev_coords = (x, y)

    line = tddata.readline()

# Todo: Display total distance
turtleDraw_Laugon.penup()
turtleDraw_Laugon.goto(180, -220)
turtleDraw_Laugon.color("black")
turtleDraw_Laugon.write(f"Total Distance: {total_distance:.2f}", align="right", font=("Arial", 10, "normal"))

# Todo: close the file
tddata.close()

#Todo: Wait for the user response to press Enter, App closing state
input("Press Enter to close the window...")
