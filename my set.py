print("Here is a set")
my_set = {"burger", "pizza", "soda"}
print(my_set)

while True:
    print("Type a text here to add it: ")
    add = input()
    case = add.lower()
    if case == "quit".casefold():
        print("=" * 80)
        print()
        break
    else:
        my_set.add(case)
        print(my_set)
        print("{} has been added in your set".format(add))
        print("=" * 80)
        print()

while True:
    print("Type a text here to delete it: ")
    delete = input()
    case2 = delete.lower()
    if case2 == "quit".casefold():
        print("=" * 80)
        print()
        break
    else:
        if case2 in my_set:
            my_set.remove(case2)
            print(my_set)
            print("{} has been removed from your set".format(delete))
        else:
            print("{} is not in your set".format(delete))
            print("=" * 80)
            print()

while True:
    text1 = input("Type a text here or sentence or type quit: ")
    case3 = text1.lower()
    if case3 == "quit".casefold():
        print("=" * 80)
        print()
    else:
        text2 = input("Type a smaller text or sentence here than {}: ".format(text1))
        case3 = text1.lower()
        case4 = text2.lower()
        text_set = frozenset(case4)
        sorted_frozenset = sorted(text_set)
        subtracted_set = set(case3).difference(case4)
        sorted_text = sorted(subtracted_set)
        print(sorted_frozenset)
        print(subtracted_set)
        print(sorted_text)
        print("=" * 80)
        print()
