import turtle

radius = int(input("Type the radius of the circle: "))

diameter = None
perimeter = None
area = None
pi = 3.14

turtle.circle(radius)
turtle.done()

while True:
    diameter = radius * 2
    print("The diameter of the circle is {}".format(diameter))
    perimeter = diameter * pi
    print("The perimeter of the circle is {}".format(perimeter))
    area = pi * radius**2
    print("The area of the circle is {}".format(area))

    radius = int(input("Type the radius of the circle: "))
