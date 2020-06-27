number1 = [1,2,3,4,5,6,7,8,9]
number2 = [1,3,4,6,7,9]
print("Old: ")
print(number1)
print(number2)
result = list(filter(lambda x: x in number1, number2))
print("Intersection at: ",result)