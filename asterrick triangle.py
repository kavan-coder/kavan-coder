number = 5
even = 2

for i in range(1, 12, 2):
    print(" " * number, end=' ')
    asterick = "*" * i
    print(asterick)
    asterick2 = "*" * even
    print(" " * number, end=' ')
    print(asterick2)
    even = even + 2
    number = number - 1
