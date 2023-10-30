num = 20

def multi_by_10(n):
    n *=10
    num = n
    print("Value of num inside function:",num)
    return n

multi_by_10(num)
print("Value of num outside function:",num)