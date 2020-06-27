myTuple = (1,2,3,4,5,6,7,8,9,10)
print(myTuple)
index1 = int(input("Enter the index from where to be sliced: "))
index2 = int(input("Enter the index from where to be sliced: "))
ind1 = index1
ind2 = index2-1
print('New Tuple: ', myTuple[ind1: ind2])
