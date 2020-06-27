def largest(list):
    largest = list[0]
    for n in list:
        if n>largest:
            largest = n
    return largest
print(largest([1,2,3,4,10,-6]))