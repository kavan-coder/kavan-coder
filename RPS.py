import random

print("Hi! Let us play rock paper scissor")

Player1 = input("Type your name player 1: ")

object2 = None

point1 = 0
point2 = 0

highest = None
Stuff2 = None

while True:
    p1 = input("Type rock, paper, scissors or quit: ")
    case = p1.lower()
    if case == "rock":
        highest = 2
        Stuff2 = random.randint(1, highest)
        if Stuff2 == 1:
            object2 = "paper"
            print("Computer has chose paper")
        elif Stuff2 == 2:
            object2 = "scissors"
            print("Computer has chose scissors")

    if case == "paper":
        highest = 2
        Stuff2 = random.randint(1, highest)
        if Stuff2 == 1:
            object2 = "rock"
            print("Computer has chose rock")
        elif Stuff2 == 2:
            object2 = "scissors"
            print("Computer has chose scissors")

    if case == "scissors":
        highest = 2
        Stuff2 = random.randint(1, highest)
        if Stuff2 == 1:
            object2 = "paper"
            print("Computer has chose paper")
        elif Stuff2 == 2:
            object2 = "rock"
            print("Computer has chose rock")

    if case == "rock":
        if object2 == "scissors":
            point1 = point1 + 1
    elif object2 == "rock":
        if case == "scissors":
            point2 = point2 + 1

    if case == "paper":
        if object2 == "rock":
            point1 = point1 + 1
    elif object2 == "paper":
        if case == "rock":
            point2 = point2 + 1

    if case == "scissors":
        if object2 == "paper":
            point1 = point1 + 1
    elif object2 == "scissors":
        if case == "paper":
            point2 = point2 + 1
    if case == "quit":
        print("OK! Bye")
        print("{} has {} points".format(Player1, point1))
        print("Computer has {} points".format(point2))
        if point1 > point2:
            print("{} has won the game".format(Player1))
            print("Computer has won the game")
        break
    highest = None
    Stuff1 = None
