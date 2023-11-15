# try except
# try:
#     a = 10 / 0
# except ZeroDivisionError as e:
#     print(e)

# try except and nested except
try:
    n1 = int(input("enter a number"))
    n2 = int(input("enter another number"))
    result = n1/n2
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("n2 is zero")
else:
    print(f"Results {result}")
finally:
    print("I will be always executed!")

