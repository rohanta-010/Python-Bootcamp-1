coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50, because tuples can't be modified
corlist = list(coordinates)
corlist[0] = 50
print(corlist)
newcoordinates = tuple(corlist)
print(newcoordinates)