# pc ile tas kagıt makas vs si attıran kod

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

decisions = [rock, paper, scissors]

my_decision = int((input("rock(0), paper(1), scissors(2)? ")))

print(f"Your decision is: {decisions[my_decision]}")
computer_decision = random.randint(0, 2)

print(f"Computer decided to go with:{decisions[computer_decision]} ")

if my_decision == 0 and computer_decision == 2:
    print("You win!")
elif computer_decision == 0 and my_decision == 2:
    print("You lose...")
elif computer_decision > my_decision:
    print("You lose...")
elif my_decision > computer_decision:
    print("You win!")
elif computer_decision == my_decision:
    print("It's a draw.")
