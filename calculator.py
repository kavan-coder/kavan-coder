print("Hi! Welcome to the calculator")

while True:
    instruction = {"+": "For addition",
                   "-": "For subtraction",
                   "*": "For multiplication",
                   "/": "For division",
                   "0": "To quit"}

    print(instruction)

    operation = input("Which operation you want from the above list: ")

    if operation == "+":
        number1 = float(input("Type a number: "))
        number2 = float(input("Type a another number: "))
        output = number1 + number2
        print("The answer is {}".format(output))
        print("=" * 80)
    elif operation == "-":
        number3 = float(input("Type a number: "))
        number4 = float(input("Type a another number: "))
        if number3 > number4:
            output2 = number3 - number4
            print("The answer is {}".format(output2))
            print("=" * 80)
        elif number4 > number3:
            output2 = number4 - number3
            print("The answer is {}".format(output2))
            print("=" * 80)
        elif number4 == number3:
            output2 = number3 - number4
            print("The answer is {}".format(output2))
            print("=" * 80)
    elif operation == "*":
        number5 = float(input("Type a number: "))
        number6 = float(input("Type a another number: "))
        output3 = number5 * number6
        print("The answer is {}".format(output3))
        print("=" * 80)
    elif operation == "/":
        number7 = float(input("Type a number: "))
        number8 = float(input("Type a another number: "))
        output4 = number7 / number8
        print("The answer is {}".format(output4))
        print("=" * 80)
    elif operation == "0":
        print("OK! Bye")
        print("=" * 80)
        break
