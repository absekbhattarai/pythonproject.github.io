letter = input("Enter a letter : ")[0]
starts_with = lambda x : True if x.startswith(letter) else False
print(starts_with('Hello'))