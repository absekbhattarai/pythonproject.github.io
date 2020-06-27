tuple= [('One: ',1),('Two: ',2),('Four',4),('Three ',3)]
print("Old Tuple: ",tuple)
tuple.sort(key = lambda x: x[1])
print("New Tuple: ",tuple)