def findLongest(words):
    wordLength = []
    for n in words:
        wordLength.append((len(n),n))
    wordLength.sort()
    return wordLength[-1][1]
print(findLongest(["Apple","Mango","Pineapple"]))