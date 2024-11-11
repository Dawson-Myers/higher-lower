import random
import game_data as gd
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
data = gd.data

def random_index():
    return random.randint(0, len(gd.data) - 1)

def game_data():
    pass

def name():
    name = data[random_index()]['name']
    return name

def follower_count():
    follower_count = data[random_index()]['follower_count']
    return follower_count

def description():
    description = data[random_index()]['description']
    return description

def country():
    country = data[random_index()]['country']
    return country


    # print(gd.data[random_index()])

def higher_lower():
    print(art.logo)

def play_game():
    pass
    """ FIXME: Add logic for game state actions including updating CORRECT or INCORRECT status, Score, and Question changes."""


print(name())
print(follower_count())
print(description())
print(country())
