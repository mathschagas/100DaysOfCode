import art
from game_data import data
import random
import os

def pick_random_celeb():
    '''Selects a random celeb from a dataset and return its information.'''
    return random.choice(data)

def most_popular_celeb(a, b):
    '''Returns which option, a or b, has greater amount of followers.'''
    if (a['follower_count'] >= b['follower_count']):
        return "a"
    else:
        return "b"


def main():

    game_over = False
    message = ""
    score = 0
    celeb_a = pick_random_celeb()
    celeb_b = pick_random_celeb()
    while celeb_b == celeb_a:
        celeb_b = pick_random_celeb()

    while not game_over:
        os.system('cls')
        print(art.logo)
        if score > 0:
            print(message)

        print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}.")
        print(art.vs)
        print(f"Against B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}.")
        user_guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

        if user_guess == most_popular_celeb(a=celeb_a, b=celeb_b):
            score += 1
            message = f"You're right! Current score: {score}."
            celeb_a = celeb_b
            while celeb_b == celeb_a:
                celeb_b = pick_random_celeb()
        else:
            message = f"Sorry, that's wrong. Final score: {score}"
            game_over = True
    
    os.system('cls')
    print(art.logo)
    print(message)

main()