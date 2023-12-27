# Bir sayının tek mi cift mi oldugunu bulan kod

print("I would like to tell you if the number you are going to tell me is odd or even. Let's give me a number!")
number = int(input())
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
