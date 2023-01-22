print("Here are all the tables from 1 to 10")

for i in range(1, 11):
    print()
    print()
    print("Here is the table of {}".format(i))
    print()
    for j in range(1, 11):
        print("{0} * {1} = {2}".format(i, j, i * j), end=' ')
