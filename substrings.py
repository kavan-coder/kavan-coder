while True:
    check_word = input("Type a word: ")
    word = input("Type a another word here shorter than {} or type quit: ".format(check_word))
    case = word.lower()
    case2 = check_word.lower()
    if case == "quit".casefold():
        print("OK! Bye")
        break
    else:
        if case in case2:
            print("{} is a substring of {}".format(word, check_word))
        else:
            print("{} is not a substring of {}".format(word, check_word))