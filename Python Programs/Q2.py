def newString(string):
    if len(string)< 2:
        return ''

    return string[0:2]+string[-2:]

print(newString('Python'))
print(newString('PY'))
print(newString('w'))
