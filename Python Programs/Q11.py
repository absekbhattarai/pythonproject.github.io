def word_count(string):
    count = dict()
    words = string.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word]=1
    return count
print(word_count('The name of the movie is Avengers!'))