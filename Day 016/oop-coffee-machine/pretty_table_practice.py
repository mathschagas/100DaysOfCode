# This code is not related to the work of the day

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Grass", "Fire", "Water"])
print(table)

