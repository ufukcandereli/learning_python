# BMI hesaplayan kod

print("What Is Your Weight?")
Weight = int(input())
print("What Is Your Height?")
Height = (float(input()))

BMI = Weight // Height ** 2
NEW_BMI = str(BMI)
print("Your Current BMI IS" + " " + NEW_BMI)
