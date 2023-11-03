# rastgele şifreler oluşturan kod

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

all_characters = []

selected_letters = random.sample(letters, number_of_letters)
selected_symbols = random.sample(symbols, number_of_symbols)
selected_numbers = random.sample(numbers, number_of_numbers)

all_characters.extend(selected_letters)
all_characters.extend(selected_symbols)
all_characters.extend(selected_numbers)

random.shuffle(all_characters)

password = ''.join(all_characters)
print("A strong password as you wish : ", password)
E3#tqC7*US65r9o   