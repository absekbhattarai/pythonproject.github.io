def notPoor(string):
    forNot = string.find('not')
    forPoor = string.find('poor')

    if forPoor > forNot and forNot>0 and forPoor>0:
        string= string.replace(string[forNot:(forPoor+4)],'good')
        return string
    else:
        return string

print(notPoor('The lyrics is not that poor!'))
print(notPoor('The lyrics is poor!'))