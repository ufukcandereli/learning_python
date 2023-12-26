# Blackjack

import random


def who_is_winning():
    double_valued_number = 11

    for i in range(len(croupier_cards)):
        if croupier_cards[i] == double_valued_number and sum(croupier_cards) > 21:
            croupier_cards[i] = 1

    for i in range(len(user_cards)):
        if user_cards[i] == double_valued_number and sum(user_cards) > 21:
            user_cards[i] = 1

    while sum(croupier_cards) < 17:
        must_draw = random.choice(all_cards)
        croupier_cards.append(must_draw)
        print(f"Croupier drew another card. It is {croupier_cards[-1]} and It made {sum(croupier_cards)} in total.")
    if sum(user_cards) > 21 and sum(croupier_cards) > 21:
        print("Draw!")
    elif sum(user_cards) > 21 > sum(croupier_cards):
        print("Croupier wins!")
    elif sum(croupier_cards) > 21 > sum(user_cards):
        print("You win!")
    elif sum(user_cards) and sum(croupier_cards) < 21:
        if sum(user_cards) > sum(croupier_cards):
            print("You win!")
        elif sum(croupier_cards) > sum(user_cards):
            print("Croupier wins!")
        elif sum(croupier_cards) == sum(user_cards):
            print("Draw!")
    elif sum(croupier_cards) == 21 and sum(user_cards) < 21:
        print("Croupier wins!")
    elif sum(user_cards) == 21 and sum(croupier_cards) < 21:
        print("You win!")


print("Welcome to The Blackjack!")

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []

you_busted = False

while len(user_cards) < 2:
    random_card = random.choice(all_cards)
    user_cards.append(random_card)

print(f"Your cards are {user_cards}.")

croupier_cards = []

while len(croupier_cards) < 2:
    random_card = random.choice(all_cards)
    croupier_cards.append(random_card)

print(f"Croupier's first card is {croupier_cards[0]}")

while not you_busted:
    draw_card = input("Do you want another card? (yes/no): ").lower()
    if draw_card == "no":
        print(f"Croupier's second card is {croupier_cards[1]}.")
        print(f"Your cards are {sum(user_cards)} in total.")
        print(f"Croupier's cards are {sum(croupier_cards)} in total.")
        who_is_winning()
        break
    if draw_card == "yes":
        random_card = random.choice(all_cards)
        user_cards.append(random_card)
        print(f"You drew {user_cards[-1]}.")
        print(f"Your cards are {sum(user_cards)} in total.")
        if sum(user_cards) > 21:
            you_busted = True
        if you_busted:
            print(f"Croupier's second card is {croupier_cards[1]}.")
            print(f"Croupier's cards are {sum(croupier_cards)} in total.")
            who_is_winning()
            break
