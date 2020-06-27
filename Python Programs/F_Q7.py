def calculateLetter (str):
    count = {"UPPERCASE": 0 , "lowercase": 0}
    for n in str:
        if n.isupper():
            count["UPPERCASE"]+=1
        elif n.islower():
            count["lowercase"]+=1
        else:
            pass
    print("String: ",str)
    print("Uppercase count: ",count["UPPERCASE"])
    print("lowercase count: ",count["lowercase"])

calculateLetter('My NaMe is AbseK')