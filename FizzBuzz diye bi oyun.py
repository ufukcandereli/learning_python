""" FizzBuzz diye bi oyun: 1 den 100 e kadar sayıyosun; 3 ün katlarında Fizz, 5 in katlarında Buzz 15 in katlarında
    FizzBuzz diyosun """

for x in range(1, 101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(f"{x}")
