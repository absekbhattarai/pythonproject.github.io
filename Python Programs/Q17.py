def multiply(items):
    multiplied = 1
    for n in items:
        multiplied = n * multiplied
    return multiplied
print(multiply([1,2,3,4,5]))