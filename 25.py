# Number Guessing Game

import random

print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I am thinking of a number between 1 and 100.")
guessed_number = random.randint(1, 100)
attempts = 0
game_on = True
game_difficulty = input("Game difficulty(easy/hard): ").lower()
if game_difficulty == "easy":
    attempts = 10
    print("You have 10 attempts")
else:
    attempts = 5
    print("You have 5 attempts")
while game_on and attempts > 0:
    user_guess = int(input("Guess a number: "))
    if user_guess > guessed_number:
        print("Too high!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    elif user_guess < guessed_number:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    else:
        print(f"Congratulations! You guessed the correct number. It was {guessed_number}.")
        game_on = False

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct number was {guessed_number}.")
