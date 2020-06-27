def smallest(list):
    small = list[0]
    for n in list:
        if n<small:
            small = n
    return small
print(smallest([1,2,3,4,10,-6]))