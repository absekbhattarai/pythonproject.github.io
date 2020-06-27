string = input("Enter comma seperated sentences: ")
words = [word for word in string.split(",")]
print(",".join(sorted(list(set(words)))))