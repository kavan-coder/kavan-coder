import random
import time
animal = None
word = None

print("Hi! Welcome to hangman")
time.sleep(2)
guess = 5
print("We are choosing the topic as animals")
time.sleep(2)
print("We have 10 names of animals.")
time.sleep(3)
print("We will move on to next animals after you complete the previous one.")
print("We are going to start soon. Just keeping the words ready and loading data")
print()
time.sleep(8)

highest = 10
number = random.randint(1, highest)

if number == 1:
    animal = "Bear"
elif number == 2:
    animal = "Wombat"
elif number == 3:
    animal = "Dog"
elif number == 4:
    animal = "Monkey"
elif number == 5:
    animal = "Bats"
elif number == 6:
    animal = "Chipmunk"
elif number == 7:
    animal = "Camel"
elif number == 8:
    animal = "Whale"
elif number == 9:
    animal = "Mole"
elif number == 10:
    animal = "Zebra"

length = len(animal)
lines = "_" * length
position = list(lines)
print(position)

while True:
    my_animal = input("Type the letter only or type quit: ")
    my_length = len(my_animal)
    case = my_animal.lower()
    case2 = animal.lower()
    if my_length > 1:
        print("Type letters only")
        print(position)
        print()
    else:
        if case in case2:
            word = case2.find(case)
            del position[word]
            position.insert(word, case)
            print(position)
            if "_" in position:
                print()
            else:
                print("Good job! You have got the word {}".format(animal))
                highest = 10
                number = random.randint(1, highest)
                if number == 1:
                    animal = "Bear"
                elif number == 2:
                    animal = "Wombat"
                elif number == 3:
                    animal = "Dog"
                elif number == 4:
                    animal = "Monkey"
                elif number == 5:
                    animal = "Bats"
                elif number == 6:
                    animal = "Chipmunk"
                elif number == 7:
                    animal = "Camel"
                elif number == 8:
                    animal = "Whale"
                elif number == 9:
                    animal = "Mole"
                elif number == 10:
                    animal = "Zebra"
                length = len(animal)
                lines = "_" * length
                position = list(lines)
                time.sleep(2)
                print()
                print(position)
        elif case == "quit":
            print("Ok! Bye")
            break
        else:
            print("There is no such letter here")
            print(position)
            print()