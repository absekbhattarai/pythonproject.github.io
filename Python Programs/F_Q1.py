def max(a,b,c):

    if(a> b and a> c):
        print("Biggest: ",a)
    elif (b> a and b> c):
        print("biggest: ",b)
    elif(c>a and c>b):
        print("biggest: ",c)
    elif(a==b and a!=c):
        print("a = b")
    elif(b==c and a!=b):
        print("b = c")
    elif(a==c and b!=c):
        print("a = c")
    else:
        print("All are equal")
max(2,2,2)

