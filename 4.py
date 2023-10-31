# Hesabı, bahsisi de dahil ederek kisi sayısına pay eden kod

print("I want to calculate have many dollars you need to pay for the bill.Tip equals to %15 of the "
      "bill. How much did bill cost?")
bill = input()
tip = float(bill) * 0.15
total = float(bill) + tip
print(f"It's ${round(total, 2)} in total. How many of you going to pay for it?")
person_number = input()
money_for_each = total / float(person_number)
print(f"It is ${round(money_for_each, 2)} for each one of you.")

