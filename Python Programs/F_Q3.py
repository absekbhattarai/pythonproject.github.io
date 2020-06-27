def multiply(numbers):
    totalProduct = 1
    for n in numbers:
        totalProduct =totalProduct* n
    return totalProduct
print(multiply((8,2,3,7)))