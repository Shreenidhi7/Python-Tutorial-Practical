# List inside a list
l1 = [5, 1.5, "Python", True, None, [1,2,3], 10]
print(l1)
print(len(l1))
# printing 2nd last element
print(l1[-2])
# can we fetch the element/item from the internal list
print(l1[-2][0])

l2 = [[1,2],[3,4],[5,6,[0,7]]]
print(l2)
print(len(l2))
l2a = l2[-1]
print(l2a)
l2a1 = l2a[-1]
print(l2a1)
l2a2 = l2a1[-1]
print(l2a2)
# direct way to fetch
print(l2[-1][-1][-1])