import random
from game_data import data
from art import logo, vs

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

def format_data(account):
    """Takes the account data and formats it into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_ans(guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Makes game callable
def higher_lower():
    print(logo)
    score = 0
    play_game = True

    # Generate random data for account from game data
    account_b = random.choice(data)

    # Make game repeatable
    while play_game:

        # Setting account B the next position at account A. Then assigns new choice to account B
        account_a = account_b
        account_b = random.choice(data)

        # Secondary check if both randomized data sets are the same and assigns new random data for account B
        if account_b == account_a:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for guess
        guess = input("Who has more followers? 'A' or 'B': ").lower()
        
        # Adds a check for invalid inputs
        if guess != "a" and guess != "b":
            print("Invalid choice try again")
            guess = input("Who has more followers? 'A' or 'B': ").lower()

        # Clear Screen
        print("\n" * 20)
        print(logo)

        # Get follower count for each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = check_ans(guess, a_follower_count, b_follower_count)

        # Score keeping and user feedback
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            play_game = False

    # Create replay option for user
    while not play_game:
        replay = input("Would you like to play again? 'Y' or 'N': ").lower()
        if replay == "y":
            higher_lower()
        else:
            print("Thank you for playing Higher Lower!\n Developed by: Dawson Myers")

higher_lower()



