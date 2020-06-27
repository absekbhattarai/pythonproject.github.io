def remove(list):
    removedList = []
    for n in list:
        if n not in removedList:
            removedList.append(n)
    return removedList

print(remove([2,3,4,5,2,3]))