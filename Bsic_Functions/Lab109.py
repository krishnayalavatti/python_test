original_str = "Krishna"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("Krishna") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")


add1 = lambda x, y: x+y

print(add1(3, 4))
