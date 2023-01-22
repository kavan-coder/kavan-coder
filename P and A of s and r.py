length = float(input("Type the length here: "))
breadth = float(input("Type the breadth here: "))

perimeter = None
area = None
extra = None

while True:
    if length == breadth:
        perimeter = length * 4
        area = length * breadth
        print("The perimeter of square is {}".format(perimeter))
        print("The area of the square is {}".format(area))
    else:
        perimeter = length + breadth
        extra = perimeter * 2
        area = length * breadth
        print("The perimeter of rectangle is {}".format(extra))
        print("The area of rectangle is {}".format(area))

    length = float(input("Type the length here: "))
    breadth = float(input("Type the breadth here: "))

    perimeter = None
    area = None
