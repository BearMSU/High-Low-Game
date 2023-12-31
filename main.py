#Skill Test: Break the Larger Problem into Smaller Ones!
from art import logo, vs
from game_data import data
from replit import clear
import random

# Format data into printable version
def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_desc}, from {account_country}.")

## Use if statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
    '''Takes the user's guess and follower counts of A and B and returns if they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make game repeatable.
while game_should_continue == True:
    # Generate a random account from game_data.
    # Making position B account become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
        
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen.
    clear()
    print(logo)
    
    # Give user feedback on their guess.
    # Keep score.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        print("Thanks for playing!!!")
        game_should_continue = False
