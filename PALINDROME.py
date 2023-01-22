while True:
    word = str(input("Type a word or number here: "))
    reversed = word[::-1]
    case = word.lower()
    case2 = reversed.lower()
    if case == case2:
        print("{} is a palindrome".format(word))
    else:
        print("{} is not a palindrome".format(word))