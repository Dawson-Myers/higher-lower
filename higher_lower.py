import random
from game_data import data
import art
"""
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

def game_data():
    name = data[random_index()]['name']
    follower_count = data[random_index()]['follower_count']
    description = data[random_index()]['description']
    country = data[random_index()]['country']
    return name, follower_count, description, country


    # print(gd.data[random_index()])

def higher_lower():
    print(art.logo)

def play_game():
    pass
    """ FIXME: Add logic for game state actions including updating CORRECT or INCORRECT status, Score, and input changes."""

name, follower_count, description, country = game_data()

print(name)
print(follower_count)
print(description)
print(country)

