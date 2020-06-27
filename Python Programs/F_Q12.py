def calculate(n):
    return lambda a: a * n
answer = calculate(2)
print("Double of 10 is ", answer(10))