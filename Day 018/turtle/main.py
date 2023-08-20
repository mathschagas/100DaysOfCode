from turtle import Turtle, Screen
import random

tim = Turtle()

# Challenge 1 - Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# Challenge 2 - Draw a Dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")


# Challenge 3 - Draw different shapes 
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# Challenge 4 - Draw a Random Walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pensize(15)
# tim.speed(0)
# for _ in range(100):
#     new_direction = random.choice([0, 90, 180, 270])
#     new_color = random.choice(colours)
#     tim.right(new_direction)
#     tim.pencolor(new_color)
#     tim.forward(30)

# Challenge 5 - Random RGB colours
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
    
# screen = Screen()
# screen.colormode(255)

# tim.pensize(15)
# tim.speed(0)
# for _ in range(100):
#     new_direction = random.choice([0, 90, 180, 270])
#     new_color = random_color()
#     tim.right(new_direction)
#     tim.pencolor(new_color)
#     tim.forward(30)

# screen.exitonclick()

# Challenge 6 - Make a Spirograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()
