def swap(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    return new_str1 + ' ' + new_str2
print (swap('abc','xyz'))

