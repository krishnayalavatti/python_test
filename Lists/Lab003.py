# To validate list is empty or not

list = []
if not list:
    print("Empty")
else:
    print("Not Empty")

# To remove item from list
squares=[1,4,9,16,25]
# print(squares.pop(2)) # Pop will remove the index value
# print(squares)
print(squares.remove(2))  # Remove the value not the index
print(squares)
