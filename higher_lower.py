import random
from itertools import count

from game_data import data
import art
"""
--Basic Game Layout and Actions--

Print Art.Logo
Compare A: {game_data}
Print Art.VS
Against B: {game_data}
Who has more followers? Type 'A' or 'B':

if answer CORRECT input score counter above Compare A
    You're right! Current score: {score}.
if answer INCORRECT update post
    Sorry, that's wrong. Final score: {score}
"""

# for each right answer the game data moves up to introduce a new comparison for B.


def random_index():
    return random.randint(0, len(data) - 1)

def compare_a():
    random_data = data[random_index()]
    name = random_data['name']
    description = random_data['description']
    country = random_data['country']
    follower_count = random_data['follower_count']
    comparison  = print(f'Compare A: {name}, {description}, from {country}')
    return comparison, follower_count

def compare_b():
    random_data = data[random_index()]
    name = random_data['name']
    description = random_data['description']
    country = random_data['country']
    follower_count = random_data['follower_count']
    comparison = print(f'Agains B: {name}, {description}, from {country}')
    return comparison, follower_count

    # print(gd.data[random_index()])

def higher_lower():
    print(art.logo)
    comparison_a, follower_count_a = compare_a()
    print(art.vs)
    comparison_b, follower_count_b = compare_b()
    more_followers = input("Who has more followers? Type 'A' or 'B': ")
    score = 0
    if more_followers == 'A':
        if follower_count_a > follower_count_b:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
    elif more_followers == 'B':
        if follower_count_b > follower_count_a:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
    else:
        print("Invalid choice")


def play_game():
    pass
    """ FIXME: Add logic for game state actions including updating CORRECT or INCORRECT status, Score, and Question changes."""

# name, follower_count, description, country = game_data()

#
higher_lower()
