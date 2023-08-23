from turtle import Turtle
import random

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)

