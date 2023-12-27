# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operation_end = False

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    first_number = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Choose an operator: ")
    second_number = int(input("What is the next number?: "))
    calc_function = operations[operation_symbol]
    result = calc_function(first_number, second_number)
    print(f"{result} is the result.")
    calc_continue = input("Do you want to continue?(yes/no): ").lower()
    if calc_continue == "no":
        operation_end = True
    while not operation_end:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose an operator: ")
        second_number = int(input("What is the next number?: "))
        calc_function = operations[operation_symbol]
        result = calc_function(result, second_number)
        print(f"{result} is the result.")
        calc_continue = input("Do you want to continue?(yes/no): ").lower()
        if calc_continue == "no":
            operation_end = True
            calculator()


calculator()
