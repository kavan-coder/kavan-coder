import turtle
import time
times = 0

print("Hi!")
time.sleep(2)
print("We will show you 7 shapes and ask you some questions. You will have to answer them correctly.")
time.sleep(2)
print("Otherwise you will fail")
time.sleep(2)
print("Ok! Let us start")
time.sleep(2)

turtle.circle(75)

turtle.pu()
turtle.forward(300)
turtle.pd()

turtle.forward(150)
turtle.right(250)
turtle.forward(150)
turtle.left(125)
turtle.forward(170)
turtle.left(305)

turtle.pu()
turtle.forward(450)
turtle.pd()

turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

turtle.pu()
turtle.forward(100)
turtle.pd()

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.pu()
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.pd()

turtle.forward(150)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(150)
turtle.left(120)
turtle.forward(100)
turtle.left(60)

turtle.pu()
turtle.forward(450)
turtle.pd()

turtle.forward(70)
turtle.left(130)
turtle.forward(100)
turtle.left(50)
turtle.forward(120)
turtle.left(50)
turtle.forward(100)
turtle.left(130)
turtle.forward(200)

turtle.pu()
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.pd()

turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(60)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(60)

turtle.done()

print("OK! Hope you have seen all the shapes")
time.sleep(2)
print("Now time to ask you some questions")

time.sleep(3)

q1 = input("What was the first shape: ")
case = q1.lower()
answer = "circle"
if case == answer:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is circle")

print("Here is next question")
time.sleep(2)

q2 = input("What was the second shape?: ")
case2 = q2.lower()
answer2 = "triangle"
if case2 == answer2:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is triangle")

print("Here is next question")
time.sleep(2)

q3 = input("What was the third shape?: ")
case3 = q3.lower()
answer3 = "rectangle"
if case3 == answer3:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is rectangle")

print("Here is next question")
time.sleep(2)

q4 = input("What was the fourth shape?: ")
case4 = q4.lower()
answer4 = "square"
if case4 == answer4:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is rectangle")

print("Here is next question")
time.sleep(2)

q5 = input("What was the fifth shape?: ")
case5 = q5.lower()
answer5 = "parallelogram"
if case5 == answer5:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is parallelogram")

print("Here is next question")
time.sleep(2)

q6 = input("What was the sixth shape?: ")
case6 = q6.lower()
answer6 = "trapezoid"
if case6 == answer6:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is trapezoid")

print("Here is next question")
time.sleep(2)

q7 = input("What was the seventh shape?: ")
case7 = q7.lower()
answer7 = "rhombus"
if case7 == answer7:
    print("Good Job!")
    times = times + 1
else:
    print("Incorrect answer! The answer is rhombus")

print("OK! The quiz has been finished")
time.sleep(5)
print("Your score is {}".format(times))
