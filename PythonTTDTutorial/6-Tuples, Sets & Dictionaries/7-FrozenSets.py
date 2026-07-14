# Normal Set - Mutable [Can change the state of the set]
s1 = {1, 2, 4, 0}
s1.add(3)
print(s1)

# Frozen Set - Immutable [Cannot change the state of the set]
fs1 = frozenset({10, 20, 30})
print(fs1, type(fs1))

fs2 = frozenset({10, 50, 100, 200})
print(fs2, type(fs2))

# fs1.add(10)
# print(fs1, type(fs1))

#Intersection
intersection = fs1.intersection(fs2)
print(f"intersection : {intersection}, type => {type(intersection)}")

#Union
union = fs1.union(fs2)
print(f"union : {union}, type =>  {type(union)}")

difference = fs1.difference(fs2)
print(f"difference : {difference}, type => {type(difference)}")
