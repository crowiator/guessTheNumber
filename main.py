import random
"""Constant"""
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def introduction():
    logo = ''' ______     _________  ____  _  _     _____   _________  _     _____
    /  __/ \ /\/  __/ ___\/ ___\/ \/ \  //  __/  /  __/  _ \/ \__//  __/
    | |  | | |||  \ |    \|    \| || |\ || |  _  | |  | / \|| |\/||  \  
    | |_// \_/||  /_\___ |\___ || || | \|| |_//  | |_// |-||| |  ||  /_ 
    \____\____/\____\____/\____/\_/\_/  \\____\  \____\_/ \|\_/  \\____\                                                                   '''
    print(logo)
    print("Welcome to the Number Guessing Game!")


def set_attemps(difficulty):
    if difficulty == "easy":
        attemps = EASY_ATTEMPTS
    else:
        attemps = HARD_ATTEMPTS
    return attemps


def guessing(attemps, keep_guess,number):
    while attemps > 0 and keep_guess:
        print(f"You have {attemps} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too low.\nGuess again.")
        elif guess > number:
            print("Too high.\nGuess again")
        elif guess == number:
            keep_guess = False
        attemps -= 1
    if keep_guess:
        print(f"You've run out of guesses, you lose.")
    else:
        print(f"You got it! The answer was {number}")
def main():
    introduction()
    number = random.randint(1, 100)
    print(f"The number is {number}")
    print("I am thinking of the number between 1 and 100.")
    attemps = set_attemps(input("Choose a difficulty. Type 'easy' or 'hard': "))
    keep_guess = True
    guessing(attemps,keep_guess,number)
main()