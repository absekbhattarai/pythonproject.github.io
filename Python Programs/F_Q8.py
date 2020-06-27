def uniqueList(list):
    x = []
    for n in list:
        if n not in x:
            x.append(n)
    return x

print(uniqueList([1,2,3,4,5,5,5,6,7]))