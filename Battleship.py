import time
import random

print("9 June 1941")
time.sleep(2)
print("Head: Hello Major!")
time.sleep(2)
print("Major: What is the matter, sir?")
time.sleep(2)
print("Head: There is a Japanese battleship Yamato which is going to attack us.")
time.sleep(2)
print("Head: It is a long range shooter. It is will shoot far away from us. We need you to destroy it.")
time.sleep(2)
print("Major: That ship is out of our radar.")
time.sleep(2)
print("Head: Take our USS Arizona. It has a really strong radar. It can easily detect that ship.")
time.sleep(2)
print("Head: Our soldier are fighting a war..... a war near the Gulf of Mexico.")
time.sleep(2)
print("Major: Ok sir! I will destroy it.")
time.sleep(2)


def coor():
    global plane
    global search1
    global search2

    whole = random.randint(23, 99)
    deci = random.randint(10, 99)

    search1 = whole
    search2 = whole

    cor1 = str(whole)
    cor2 = str(deci)

    plane = cor1 + "." + cor2


while True:
    y_coor = input("Type your ship's coordinate (Ex: 67.43): ")

    if len(y_coor) == 5:
        time.sleep(3)
        break
    else:
        print("Incorrect coordinates, type the coordinates again")


def think():
    global plane2

    whole2 = random.randint(23, 99)
    deci2 = random.randint(10, 99)

    cor3 = str(whole2)
    cor4 = str(deci2)

    plane2 = cor3 + "." + cor4

    print("??? typed {}".format(plane2))


coor()

while True:
    y_think = input("Type the enemy's ship's coordinates or type 1 for Advance Search: ")

    if y_think == "1":
        print("Finding the ship...")
        time.sleep(5)
        approx = random.randint(1, 3)
        print("The ship has been found near {}".format(plane))

    else:
        if y_think == plane:
            print()
            print("After a few months")
            time.sleep(2)
            print("Head: Major, what is your status?")
            time.sleep(2)
            print("Major: This is Franklin Van Valkenburgh, Japanese battleship Yamato has been destroyed.")
            time.sleep(2)
            print("Soldier: This is the Royal Navy. Gulf of Mexico is in our hands")
            time.sleep(2)
            print("Pilot: This is Edward Elliot. Pearl Harbor has been secured.")
            time.sleep(2)
            print("Bomber: This is Robert A. Lewis, pilot of Boeing B-29 Superfortress.")
            time.sleep(2)
            print("Bomber: We have successfully dropped our bomb at Nagasaki. We have won the war.")
            break
        else:
            print()
            print("Oh no! You got the incorrect coordinates")
            print()
    time.sleep(5)
    think()
    if plane2 == y_coor:
        print()
        print("Head: Major come in!")
        time.sleep(2)
        print("Japan: This is Kōsaku Aruga. I have destroyed your foolish Major. Be ready to loose")
        break
    else:
        print()
        print("Pheew! You got saved")
        print()
