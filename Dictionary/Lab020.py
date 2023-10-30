my_dict = {'a':1,'b':2}

val = my_dict.pop('a')
print(val)

print(my_dict)

# API Testing -> JSON so we can use Dict which is similar data type as JSON

print(dir(my_dict))

# How to iterate over the Dict?

knights = {'gallahad':'the pure','robbin':'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k,v)