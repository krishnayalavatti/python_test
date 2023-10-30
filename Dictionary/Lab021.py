my_dict = {'a':1,'b':2,'c':3}

val=my_dict.pop('a')
print(val)

# popitem() is used to remove and return an arbitrary key-value pair
val = my_dict.popitem()
print(val)

del my_dict
print(my_dict)