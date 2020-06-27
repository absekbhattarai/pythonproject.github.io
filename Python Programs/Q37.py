#Write a Python program to multiply all the items in a dictionary.



dict = {'Apple':13,'Banana':23,'Carrot':5}
number = 1

for key in dict:
    number = number * dict[key]
print(number)