# Create a Program
# Take 5 numbers from the Users
# Add 1-2 duplicates
# print the non duplicate numbers


n1 = input("Enter the number")
n2 = input("Enter the number")
n3 = input("Enter the number")
n4 = input("Enter the number")
n5 = input("Enter the number")

n6 = [n1, n2, n3, n4, n5]
print(n6)

n7 = set(n6)
print(n7)   # non duplicate numbers by converting into sets as sets hold unique values only

duplicates = [element for element in n6 if n6.count(element) > 1]

print(duplicates)



