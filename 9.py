# Iki kisi arasındakı askı hesaplayan kod (yersen)

print("I would like to calculate the love score between a couple. Let's give me two names and learn the truth -->")

the_one = input()
the_other = input()

we_are = the_one + the_other
we_are_lower = we_are.lower()

t = we_are_lower.count("t")
r = we_are_lower.count("r")
u = we_are_lower.count("u")
e = we_are_lower.count("e")

number1 = t + r + u + e

l = we_are_lower.count("l")
o = we_are_lower.count("o")
v = we_are_lower.count("v")
e = we_are_lower.count("e")

number2 = l + o + v + e

number = str(number1) + str(number2)

if 10 >= int(number) >= 90:

    print(f"Your love score is {number}. You are exactly like a bomb together.")

elif 40 <= int(number) <= 50:

    print(f"Your love score is {number}. You are fine together.")

elif int(number) > 100:
    print("Your love score is beyond the calculation!")

else:

    print(f"Your love score is {number}.")


