# Prime Number Checker


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


n = int(input("Give me a number, i will check if it is a prime number or not: "))
prime_checker(number=n)
