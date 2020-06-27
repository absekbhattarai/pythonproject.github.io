d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def keyCheck(n):
    if n in d:
        print('Key is present')
    else:
        print('key is not present')
keyCheck(1)
keyCheck(7)