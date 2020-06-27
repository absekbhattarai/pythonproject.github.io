def evenNumber(list):
    evenList = []
    for n in list:
        if n%2 == 0:
            evenList.append(n)
    return evenList
print(evenNumber([1,2,3,4,5,6,7,8,9,10]))