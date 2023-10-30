

my_dict = {'a':1,'b':2,'c':3}
print(my_dict)
val = my_dict.pop('a')
print(val)
print(my_dict)
# print(my_dict.pop('a'))
# print(my_dict)
my_dict['a']=val
print(my_dict)

# OrderedDict
# Key-Value pairs based on the order of insertion

# from collections import orderedDict

from collections import OrderedDict
od = OrderedDict()
od ['a']= 45
od ['b']= 46
od ['c']= 47
od ['d']= 48
print(od)

# Selenium - Inserts the web elements into a Dictionary
# we use to order login elements and dashboard elements

# Dict - It will not keep the order of insertion
# OrderDict - It will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sorted=sorted(keys)
print(keys_sorted)

keys_sor=list(reversed(keys))
print(keys_sor)

keys_sort_rev=(sorted(keys, reverse=True))
print(keys_sort_rev)


od2 = OrderedDict()
od2[keys_sorted[0]]=45
od2[keys_sorted[1]]=46
od2[keys_sorted[2]]=47
od2[keys_sorted[3]]=48
print(od2)
print(list(od2.values()))
print(tuple(od2.keys()))
print(set(od2.keys()))