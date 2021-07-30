# Sets are mutable, elements in sets are immutable.

p = {1,2,3,4,56,7888,888}
print(p)

k = {23,111}
k.add(2)
k.update([12,44,66,777,8,88])
print(k)
k.remove(12)
#Shallow Copy
j=k.copy()
print(j)


blue_eyes = {'Cherry','Terry', 'Lily', 'Amelia'}
blond_hair = {'Cherry', 'Kyala', 'Jackie', 'Rose'}
print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.difference(blond_hair))
print(blue_eyes.symmetric_difference(blond_hair))
print(blue_eyes.issubset(blond_hair))


