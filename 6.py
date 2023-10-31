# BMI' ı hesapladıktan sonra kişinin kilosu hakkında bilgi veren kod

print("I would like to learn your height and weight for calculating your BMI and inform you about your situation. ")
Height = float(input("What's your height?"))
Weight = int(input("What is your weight?"))
BMI = Weight / Height ** 2
if BMI <= 18.5:
    print(f"Your BMI is {round(BMI, 2)}. You are underweight.")
elif 18.5 < BMI <= 25.0:
    print(f"Your BMI is {round(BMI, 2)}. You have a normal weight.")
elif 25.0 < BMI <= 30:
    print(f"Your BMI is {round(BMI, 2)}. You are slightly overweight.")
elif 30.0 < BMI <= 35.0:
    print(f"Your BMI is {round(BMI, 2)}. You are obese.")
else:
    print(f"Your BMI is {round(BMI, 2)}. You are clinically obese.")