fruits = {"orange": "a sweet orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

print("Here is a dictionary")
for f in fruits:
    print(f + ' - ' + fruits[f])

while True:
    print("Type a item from your dictionary or else type quit")
    dict_key = input("Please enter a fruit: ")
    case = dict_key.casefold()
    if case == "quit".casefold():
        print("-" * 40)
        print()
        break
    if case in fruits:
        description = fruits.get(case)
        print(description)
        print("-" * 80)
        print()
    else:
        print("we don't have a " + case)
        print("-" * 40)
        print()

while True:
    print("To add an item you have to type the fruit's name then type its description or type quit")
    name = input("Type fruit's name: ")
    case2 = name.casefold()
    if case2 == "quit".casefold():
        print("-" * 40)
        print()
        break
    else:
        meaning = input("Type the description of {}: ".format(case2))
        print("Let us see our shopping list")
        fruits[name] = meaning
        for g in fruits:
            print(g + ' - ' + fruits[g])
        print("The item {} has been added to your dictionary".format(case2))
        print("-" * 40)
        print()

while True:
    print("To edit an item you have to type a new fruit's name then type a new description description or type quit")
    name2 = input("Type fruit's name: ")
    case3 = name2.casefold()
    if case3 == "quit".casefold():
        print("-" * 40)
        print()
        break
    else:
        del fruits[name2]
        meaning2 = input("Type the description of {}: ".format(case3))
        fruits[name2] = meaning2
        print("Let us see our shopping list")
        for g in fruits:
            print(g + ' - ' + fruits[g])
        print("The item's description has been changed in your dictionary")
        print("-" * 40)
        print()
