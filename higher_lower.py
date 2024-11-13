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



def higher_lower():
    game_state = True
    score = 0
    output = ''
    while game_state:
        print(art.logo)
        print(output)
        comparison_a, follower_count_a = compare_a()
        print(art.vs)
        comparison_b, follower_count_b = compare_b()
        more_followers = input("Who has more followers? Type 'A' or 'B': ").lower()
        if more_followers == 'a':
            if follower_count_a > follower_count_b:
                score += 1
                output = f"You're right! Current Score: {score}"
                # FIXME: Need to reassign the comparison_a with the values of comparison_b then issue only a new comparison_b for the next wave.
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                game_state = False
        elif more_followers == 'b':
            if follower_count_b > follower_count_a:
                score += 1
                output = f"You're right! Current Score: {score}"
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                game_state = False
        else:
            print("Invalid choice")


higher_lower()
request_play = input("Would you like to play again? Type 'Y' or 'N': ").lower()
if request_play == 'y':
    higher_lower()
else:
    print("\n" * 5)
    print("Thanks for playing!")
    print(art.logo)