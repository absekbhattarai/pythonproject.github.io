def reverse(str):
    reverseStr = ''
    index = len(str)
    while index > 0:
        reverseStr += str[index - 1]
        index = index -1
    return reverseStr
print(reverse('hello'))