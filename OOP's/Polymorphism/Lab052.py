# Method Overloading:
# Python does not support method overloading in the traditional sense
# Same name of a function with different Parameter


class Mathutil:
    def add(self, a, b=1, c=0):
        return a + b + c


math = Mathutil()
sum = math.add(1, 2, 3)
print(sum)

sum1 = math.add(1, 2)
print(sum1)

sum2 = math.add(2)
print(sum2)
