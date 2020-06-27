def addString(string):
    length = len(string)
    if length > 2:
        if string[-3:]=='ing':
            string += 'ly'
        else:
            string += 'ing'

    return string
print(addString('ab'))
print(addString('abc'))
print(addString('string'))