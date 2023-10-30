t = ("II am Groot","For","Krishna")
print("\n set with the use of tuple")
print(set(t))

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
my_set1 = set1.union(set2)
my_set2 =  set1.difference(set2)

print(my_set1)
print(my_set2)

set1 = {1,2,3,4,5,6}
set2 = {2,3,4}
subset = set2.issubset(set1)
print(subset)

set3 = {"II am Groot","For","Krishna"}
print(set3)

for i in set3:
    print(i)

set4 = set([1,2,3,4,5,6,7,8,9])
set4.remove(5)
set4.remove(7)
set4.remove(1)
print(set4)