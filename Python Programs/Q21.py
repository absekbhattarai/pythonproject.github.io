def last_items(n):
    return n[-1]

def sort_items(tuples):
    return sorted(tuples,key=last_items)

print(sort_items([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))