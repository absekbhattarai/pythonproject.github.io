def countString(string):
    count= 0
    list = string.split()
    for n in list:
        if len(n)>2 and n[0]==n[-1]:
            count+=1
    return count
print(countString('abc xyz aba 12221'))