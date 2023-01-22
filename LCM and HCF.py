while True:

    number1 = int(input("Type a number here: "))
    number2 = int(input("Type another number here: "))

    even_higher = None
    even_higher2 = None

    HCF = None

    if number1 > number2:
        smaller = number2
    else:
        smaller = number1

    for i in range(1, smaller + 1):
        if number1 % i == 0 and number2 % i == 0:
            HCF = i

    print("HCF of {} and {} is {}".format(number1, number2, HCF))

    number = number1 * number2
    LCM = number // HCF
    print("LCM of {} and {} is {}".format(number1, number2, LCM))
