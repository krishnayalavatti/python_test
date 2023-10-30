# Set

# Initial blank set
set1 = set()
print(set1)

set2 = set("Krishna")
print(set2)

set3 = {1,2,3,4,5,5}   # No duplicates allowed
print(set3)
print(type(set3))

# list of elements to store in web automation
# we can use set to store the value, so that we dont have duplicate

set3 = {1,2,3,4,5,5}
set3[1]=34    # Not possible, Immutable
print(set3)

set1 = set(["Krishna","For","Ram"])
print(set1)