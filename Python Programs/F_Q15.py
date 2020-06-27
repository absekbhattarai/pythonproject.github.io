numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Old",numbers)
even_numbers = list(filter(lambda x : x%2==0,numbers))
print("Even: ",even_numbers)
odd_numbers = list(filter(lambda x: x%2==1,numbers))
print("Odd: ",odd_numbers)


