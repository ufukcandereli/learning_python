# Hangman
import random

word_list = ["araba", "astronot", "antilop", "anakonda"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

pure_display = "".join(display)
print(pure_display)
live = 6
print("You have 6 lives")
while "_" in display:
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guessed_letter:
                display[letter] = guessed_letter
    else:
        print("Incorrect guess!")
        live -= 1
        print(f"You have {live} life left.")
    print(f"Current word is: {"".join(display)}")

if live == 0:
    print("You lose!")

if "_" not in display:
    print(f"You win! The word was: {"".join(display)}")

