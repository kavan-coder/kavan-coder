import math

height = int(input("Type your height in meters: "))
weight = int(input("Type your weight: "))


def bmi(w, h):
    sqr_h = math.pow(h, 2)
    y_bmi = w/sqr_h
    print("Your BMI is {}".format(y_bmi))
    if y_bmi < 18.5:
        print("You are underweight. Better start eating some food.")
    elif 18.5 > y_bmi < 24.9:
        print("You have a normal weight. You're just fine. Keep the same pace.")
    elif 25.0 > y_bmi < 29.9:
        print("You are overweight. Better to eat less fat.")
    elif 30.0 > y_bmi < 34.9:
        print("You are in Obesity Class 1. Sounds too bad.")
    elif 35.0 > y_bmi < 39.9:
        print("You are in Obesity Class 2. You're now getting to fat.")
    elif y_bmi > 40.0:
        print("You are in Obesity Class 3. Eat less food and exercise more.")


bmi(weight, height)
