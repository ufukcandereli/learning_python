# Bir yılın artık yıl olup olmadıgını bulan kod

year = int(input("I would like to tell you if the year you are going to tell me is a leap year or not."
                 "Give me a random year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")

        else:
            print(f"{year} is not a leap year.")

    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")