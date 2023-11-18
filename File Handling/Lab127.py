with open('example.txt', 'a') as file:
    file.write("Hello, world!2")

with open('example.txt', 'r') as file:
    print(file.read())
