def three_digits():
    number = int(input("Insert a three digits number: "))
    dig1 = number // 10
    dig2 = number // 100
    num = str(number)
    a = (num[2:3])
    b = (num[1:2])
    c = (num[:1])
    A = int(a)
    B = int(b)
    C = int(c)

    if not (number < 100) and (number > 999):
        print("The number is invalid")

    elif (A + C) == B:
        print("The center is the winner")

    elif (a) == (c):
        print("The number is capicua")

    elif

three_digits()


