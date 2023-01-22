import random
import time
questions = 1

print("Hi! Welcome quiz area!")
time.sleep(2)
print("Today we will also ask you some question of mathematics")
time.sleep(2)
instruction = {"+": "For addition",
               "-": "For subtraction",
               "*": "For multiplication",
               "/": "for division",
               "0": "To quit"}

print(instruction)

operation = input("Which operation do you want: ")
highest = 1000
highest2 = 900
number1 = random.randint(1, highest)
number2 = random.randint(1, highest)

number3 = random.randint(1, highest)
number4 = random.randint(1, highest2)

number5 = random.randint(1, highest)
number6 = random.randint(1, highest)

number7 = random.randint(1, highest)
number8 = random.randint(1, highest2)

while True:
    if operation == "+":
        print("{} + {}".format(number1, number2))
        answer = float(input("Type your answer here: "))
        output = number1 + number2
        if answer == output:
            print("Good job!")
            print("=" * 80)
        else:
            print("This is the incorrect answer. The answer is {}".format(output))
            print("=" * 80)
    elif operation == "-":
        print("{} - {}".format(number3, number4))
        answer2 = float(input("Type your answer here: "))
        output2 = number3 - number4
        if answer2 == output2:
            print("Good job!")
            print("=" * 80)
        else:
            print("This is the incorrect answer. The answer is {}".format(output2))
            print("=" * 80)
    elif operation == "*":
        print("{} * {}".format(number5, number6))
        answer3 = float(input("Type your answer here: "))
        output3 = number5 - number6
        if answer3 == output3:
            print("Good job!")
            print("=" * 80)
        else:
            print("This is the incorrect answer. The answer is {}".format(output3))
            print("=" * 80)
    elif operation == "/":
        print("{} / {}".format(number7, number8))
        answer4 = float(input("Type your answer here: "))
        output4 = number7 - number8
        if answer4 == output4:
            print("Good job!")
            print("=" * 80)
        else:
            print("This is the incorrect answer. The answer is {}".format(output4))
            print("=" * 80)
    elif operation == "0":
        print("OK! Bye")
        print("=" * 80)
        break
    instruction = {"+": "For addition",
                   "-": "For subtraction",
                   "*": "For multiplication",
                   "/": "for division",
                   "0": "To quit"}

    print(instruction)

    operation = input("Which operation do you want: ")
    highest = 1000
    number1 = random.randint(1, highest)
    number2 = random.randint(1, highest)
    number3 = random.randint(1, highest)
    number4 = random.randint(1, highest)
    number5 = random.randint(1, highest)
    number6 = random.randint(1, highest)
    number7 = random.randint(1, highest)
    number8 = random.randint(1, highest)
