products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]

print(type(products))
print(type(products[0]))

print(products[0])

def is_affordable(products):
    return products["price"] < 500
affordable_items_price = list(filter(is_affordable,products))
print(affordable_items_price)

def is_affordable_name(products):
    return len(products["name"]) > 6
affordable_items_name = list(filter(is_affordable_name,products))
print(affordable_items_name)

for i in affordable_items_price:
    print(i["price"],i["name"])

for i in affordable_items_name:
    print(i["price"],i["name"])



i=10
name = "Groot"
print(i)
print(name)
print(name+str(i))
# print(int(name)+i)

