#Pizza siparisi alıp icindeki malzemelere ve pizza boyutuna göre ucreti hesaplayan kod

print("WELCOME TO THE UFUK'S PIZZA PLACE!")
size = input("What size pizza you want? (S,M or L) -->")
add_pepperoni = input("Do you want pepperoni? (Y or N) -->")
extra_cheese = input("Do you want extra cheese? (Y or N) -->")

Bill = 0

if size == "S":
    Bill = 15
elif size == "M":
    Bill = 20
else:
    Bill = 25

if add_pepperoni == "Y":
    if size == "S":
        Bill = Bill + 2
    elif size == "M":
        Bill = Bill + 3
    else:
        Bill = Bill + 3
if extra_cheese == "Y":
    Bill = Bill + 1

print(f"The bill is ${Bill}. Enjoy your meal.")


