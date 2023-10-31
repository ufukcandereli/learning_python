# Amiral battı tadında bişeyler ( biraz amele işi oldu nasıl kısaltırım bilmem)

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

if (position == "A1"):
    map[0][0] = 'X'
elif (position == "A2"):
    map[1][0] = 'X'
elif (position == "A3"):
    map[2][0] = 'X'
elif (position == "B1"):
    map[0][1] = 'X'
elif (position == "B2"):
    map[1][1] = 'X'
elif (position == "B3"):
    map[2][1] = 'X'
elif (position == "C1"):
    map[0][2] = 'X'
elif (position == "C2"):
    map[1][2] = 'X'
elif (position == "C3"):
    map[2][2] = 'X'

print(f"{line1}\n{line2}\n{line3}")