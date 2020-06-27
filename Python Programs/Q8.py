def removeChar(string,n):
    first=string[:n]
    last=string[n+1:]
    return first + last


print(removeChar('Assignment',0))
print(removeChar('Assignment',4))
