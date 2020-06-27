myTuple = (1,2,3,4,5)
print(myTuple)
n = int(input("Enter the number to be removed: "))
myList = list(myTuple)
myList.remove(n)
myTuple=tuple(myList)

print(myTuple)
