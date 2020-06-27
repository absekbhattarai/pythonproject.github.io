def dollar(str):
    store = str[0]
    str= str.replace(store,'$')
    str=store+str[1:]

    return str
print(dollar('restart'))

