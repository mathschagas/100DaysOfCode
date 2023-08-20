# Code for getting the list of tuplets for colors
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day 018\\turtle\\hirst-painting\\image.jpg', 30)
# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
color_list = [(239, 218, 77),  (122, 176, 147), (165, 84, 45), (20, 118, 164), (96, 181, 209), (58, 21, 8), (199, 151, 157), (137, 167, 22), (9, 97, 37), (223, 93, 57), (167, 12, 20), (198, 145, 104), (150, 55, 62), (231, 175, 169), (72, 114, 69), (229, 177, 184), (102, 88, 11), (2, 48, 140), (156, 28, 27), (2, 46, 111), (12, 183, 227), (63, 186, 180), (6, 81, 110), (158, 205, 184), (35, 3, 5), (199, 64, 68)]
turtle_module.colormode(255)

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()