def removeOddIndex(string):
    result = ""
    for n in range(len(string)):
        if n % 2 == 0:
            result = result+ string[n]
    return result

print(removeOddIndex('Basketball'))