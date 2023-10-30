#  Map and Filter in the list

sq = lambda x: x * x
result = sq(5)
print(result)

# Map Functions
numbers1 = [1, 2, 3, 4, 5]
sq_numbers = []

for i in numbers1:
    sq_numbers.append(sq(i))
print(sq_numbers)

# Map Functions
sq_numbers2 = list(map(lambda x: x * x, numbers1))
print(sq_numbers2)


def triple(a):
    return a * 3


tr_numbers2 = list(map(triple,numbers1))
print(tr_numbers2)
