import random
import time

print("Hi! We have chosen a number")
time.sleep(2)
print("You will have to type a number and that number will get added to our number")
time.sleep(2)
print("You have to find the number we have chosen")
time.sleep(2)

p_number = int(input("Type your number: "))

print("Your number is {}".format(p_number))
print()
time.sleep(2)

highest = 100
number = random.randint(1, highest)


def add():
    p_total = number + p_number
    print("We have got {} by doing some addition".format(p_total))
    time.sleep(2)


add()

print("Hope you have found our number. Type it below.")
print()
time.sleep(2)

while True:
    o_number = int(input("Type it here: "))

    if o_number == number:
        print("Good job! You have got the number.")
        print("=" * 80)
        break
    else:
        if o_number > number:
            print("Type a number less than {}".format(o_number))
            print("=" * 80)
        else:
            print("Type a number more than {}".format(o_number))
            print("=" * 80)
