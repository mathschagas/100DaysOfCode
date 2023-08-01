#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return turns
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print("Too low.")
        return turns - 1

def game():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts_left = set_difficulty()
    guess = 0
    while guess != secret_number:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts_left = check_answer(guess, secret_number, attempts_left)
        if attempts_left == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != secret_number:
            print("Guess again.")

game()