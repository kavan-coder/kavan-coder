while True:
    word = input("Type a word here: ")
    letters = len(word)
    if letters % 2 == 0:
        print("{} is not balanced".format(word))
    else:
        find = letters // 2
        print("The word {} is balanced".format(word))
        seperate = list(word)
        centre = seperate[find]
        print("The centre of the word {} is {}".format(word, centre))