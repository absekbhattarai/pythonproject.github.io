bikes = [{'ktm':'duke','color':'orange'},{'yamaha':'R3','color':'blue'},{'crosfire':'rm250','color':'red'}]
print("Old: ",bikes)
sorted_bikes = sorted(bikes, key = lambda x : x['color'])
print("New: ",sorted_bikes)