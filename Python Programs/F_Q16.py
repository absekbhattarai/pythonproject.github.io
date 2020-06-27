numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Old: ",numbers)
square_numbers = list(map(lambda x: x*x, numbers))
print("Square: ",square_numbers)
cube_numbers = list(map(lambda x: x*x*x, numbers))
print("Cube: ",cube_numbers)
