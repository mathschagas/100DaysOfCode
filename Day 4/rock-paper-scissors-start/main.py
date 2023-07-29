rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if players_choice != "0" and players_choice != "1" and players_choice != "2":
  print("You provided an invalid input")
else:
  players_choice = int(players_choice)
  rock_paper_scissors_art = [rock, paper, scissors]
  print(rock_paper_scissors_art[players_choice])
  computers_choice = random.randint(0, 2)
  print("Computer chose:")
  print(rock_paper_scissors_art[computers_choice])
  
  if players_choice == 0:
    if computers_choice == 0:
      print("It's a draw")
    elif computers_choice == 1:
      print("You lose")
    else:
      print("You win")
  elif players_choice == 1:
    if computers_choice == 0:
      print("You win")
    elif computers_choice == 1:
      print("It's a draw")
    else:
      print("You lose")
  else:
    if computers_choice == 0:
      print("You lose")
    elif computers_choice == 1:
      print("You win")
    else:
      print("It's a draw")
  