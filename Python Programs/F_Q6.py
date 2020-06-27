def testrange(n):
    range1 = int(input("Enter first number in range: "))
    range2 = int(input("Enter second number in range: "))

    if n in range(range1, range2):
        print("%s is in range"%str(n))
    else:
        print("Not in range")
testrange(4)