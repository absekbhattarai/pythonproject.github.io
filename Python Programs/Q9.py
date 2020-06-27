def  exchange(string):
    str= string[-1:] +string[1:-1] + string[:1]
    return str

print(exchange('Apple'))