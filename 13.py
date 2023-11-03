# for loop ile boyları bilinen kişilerin boy ortalamasını alma

n = int(input("How many values will you enter?: "))

height_list = []

total_height = 0

for x in range(n):
    height = float(input(f"{x + 1}. person's height (metre type): "))
    height_list.append(height)
    total_height += height

avarage_height = total_height / n

print(f"Avarage height is {round(avarage_height, 3)}")
